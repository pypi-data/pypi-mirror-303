from string import Template
from textwrap import dedent, indent
from typing import TYPE_CHECKING, Any

from ..utils.package_extras import RequiredExtraNotInstalled

try:
  import tree_sitter_tlaplus as tstla
except ModuleNotFoundError as e:
  e2 = e

  class RaiseTstlaMissingIfUsed:
    def __init__(self, *a: Any, **kw: Any) -> None:
      raise RequiredExtraNotInstalled(
        "tree_sitter_tlaplus", "TLA+ state parsing", "state-parsing"
      ) from e2

  class Tstla:
    def __getattr__(self, *a: Any, **kw: Any) -> Any:
      RaiseTstlaMissingIfUsed()

  if not TYPE_CHECKING:
    tstla = Tstla()

try:
  from tree_sitter import Language, Node, Parser, Tree
except ModuleNotFoundError as e:
  e2 = e

  class RaiseTreeSitterMissingIfUsed:
    def __init__(self, *a: Any, **kw: Any) -> None:
      raise RequiredExtraNotInstalled(
        "tree_sitter", "TLA+ state parsing", "state-parsing"
      ) from e2

  if not TYPE_CHECKING:
    Language = RaiseTreeSitterMissingIfUsed
    Node = RaiseTreeSitterMissingIfUsed
    Parser = RaiseTreeSitterMissingIfUsed
    Tree = RaiseTreeSitterMissingIfUsed

from .model import (
  FunctionMerge,
  Record,
  RecordField,
  SealedValue,
  SimpleValue,
  SingleElemDomainFunction,
)


def pretty_print_tree_sitter_tree(tree: Tree) -> None:
  "For debugging"
  cursor = tree.root_node.walk()
  level = 0
  while True:
    node = cursor.node
    assert node is not None
    text = "" if node.children else f" {node.text!r}"
    field_name = cursor.field_name
    field_name = f"[field: {field_name}] " if field_name is not None else ""
    print("  " * level + f"{field_name}{node.type}:{text}")

    if cursor.goto_first_child():
      level += 1
      continue
    else:
      if cursor.goto_next_sibling():
        continue
      else:
        at_root = False
        while True:
          if cursor.goto_parent():
            level -= 1
            # field_name = cursor.field_name
            # field_name = f"[field: {field_name}] " if field_name is not None else ""
            # print("  "*level + f"end of {field_name}{cursor.node.type}")
            if cursor.goto_next_sibling():
              break
          else:
            at_root = True
            break
        if at_root:
          break


def tlaplus_state_to_dataclasses(
  tlaplus_state: str,
) -> dict[str, SealedValue]:
  # Create dummy module to facilitate parsing
  # (TODO: Does tree-sitter support parsing sub-grammars somehow?)
  tlaplus_module = Template(
    dedent(
      """\
      ---- MODULE Dummy ----
      State ==
      $state
      ====
      """
    )
  ).substitute(state=indent(tlaplus_state, "  "))

  # Parse with tree-sitter
  TLAPLUS_LANGUAGE = Language(tstla.language())
  parser = Parser(TLAPLUS_LANGUAGE)

  tree = parser.parse(bytes(tlaplus_module, "utf8"))

  # pretty_print_tree_sitter_tree(tree)

  # Extract relevant part (State RHS)
  query = TLAPLUS_LANGUAGE.query(
    dedent(
      """\
      (
        source_file (
          module (
            operator_definition (
              (identifier) @state_name
              (#eq? @state_name "State")
            )
            (def_eq)
            definition: (_) @definition
          )
        )
      )
    """
    )
  )
  query.disable_capture("state_name")  # only used inside query
  for capture_name, captures in query.captures(tree.root_node).items():
    break
  else:
    assert False, "definition not found"
  assert capture_name == "definition"
  assert len(captures) == 1

  definition = captures[0]

  # TODO: Figure out if we can actually assert this or if a single-var state
  #   doesn't have a wrapping conj_list
  assert definition.type == "conj_list"

  # Queries stop working here b/c no way to limit to direct children:
  var_name_to_rhs = {}
  for item in definition.children:
    assert item.type == "conj_item"
    item_children_iter = iter(item.children)

    bullet_conj = next(item_children_iter)
    assert bullet_conj.type == "bullet_conj"

    bound_infix_op = next(item_children_iter)
    assert bound_infix_op.type == "bound_infix_op"

    lhs = bound_infix_op.child_by_field_name("lhs")
    assert lhs is not None, "no lhs found"
    assert lhs.type == "identifier_ref"
    var_name = lhs.text
    assert var_name is not None, "invalid variable name (None)"

    rhs = bound_infix_op.child_by_field_name("rhs")
    assert rhs is not None, "invalid rhs (None)"

    assert var_name not in var_name_to_rhs
    var_name_to_rhs[var_name] = rhs

  var_name_to_dc: dict[str, SealedValue] = {}
  for var_name, rhs in var_name_to_rhs.items():
    var_name_to_dc[var_name.decode("utf-8")] = tlaplus_value_to_dataclass(rhs)

  return var_name_to_dc


def tlaplus_value_to_dataclass(rhs: Node) -> SealedValue:
  assert rhs is not None, "invalid rhs (None)"
  match rhs.type:
    case "record_literal":
      record_fields = []

      record_children_iter = iter(rhs.children)

      openbracket = next(record_children_iter)
      assert openbracket.type == "["

      node = next(record_children_iter)
      while node.type != "]":
        identifier = node

        assert identifier.type == "identifier"
        key = identifier.text
        assert key is not None, "invalid record key (None)"

        all_map_to = next(record_children_iter)
        assert all_map_to.type == "all_map_to"

        value_nodes: list[Node] = []
        node = next(record_children_iter)
        while True:
          if node.type in {",", "]"}:
            assert len(value_nodes) == 1
            value_node = value_nodes[0]
            value_dc = tlaplus_value_to_dataclass(value_node)
            record_fields.append(RecordField(key.decode("utf-8"), value_dc))
            value_nodes = []
            if node.type == ",":
              node = next(record_children_iter)
            break
          else:
            value_nodes.append(node)
            node = next(record_children_iter)

      return Record(record_fields)
    case "parentheses" if len(rhs.children) == 3 and (
      inner := rhs.children[1]
    ).type == "bound_infix_op":
      symbol = inner.child_by_field_name("symbol")
      assert symbol is not None, "invalid symbol (None)"
      match symbol.type:
        case "compose":
          return _compose_to_dataclasses(inner)
        case _:
          assert rhs.text is not None, "invalid rhs text (None)"
          return _simple_value_to_dataclass(rhs)
    case _:
      assert rhs.text is not None, "invalid variable rhs (None)"
      return _simple_value_to_dataclass(rhs)


def _compose_to_dataclasses(node: Node) -> FunctionMerge | SimpleValue:
  lhs = node.child_by_field_name("lhs")
  assert lhs is not None, "invalid lhs (None)"
  rhs = node.child_by_field_name("rhs")
  assert rhs is not None, "invalid rhs (None)"
  lhs_dc = _compose_operand_to_dataclasses(lhs)
  rhs_dc = _compose_operand_to_dataclasses(rhs)
  if isinstance(lhs_dc, SingleElemDomainFunction) and isinstance(
    rhs_dc, SingleElemDomainFunction
  ):
    return FunctionMerge([lhs_dc, rhs_dc])
  elif isinstance(lhs_dc, FunctionMerge) and isinstance(
    rhs_dc, SingleElemDomainFunction
  ):
    return FunctionMerge(lhs_dc.functions + [rhs_dc])
  elif isinstance(rhs_dc, FunctionMerge) and isinstance(
    lhs_dc, SingleElemDomainFunction
  ):
    return FunctionMerge(rhs_dc.functions + [lhs_dc])
  else:  # can't make sense of it so hope it's a simple value
    return _simple_value_to_dataclass(node)


def _compose_operand_to_dataclasses(
  node: Node,
) -> FunctionMerge | SingleElemDomainFunction | SimpleValue | None:
  if node.type != "bound_infix_op":
    # can't make sense of it, give up
    return None

  symbol = node.child_by_field_name("symbol")
  assert symbol is not None, "invalid symbol (None)"
  match symbol.type:
    case "compose":
      return _compose_to_dataclasses(node)
    case "map_to":
      lhs = node.child_by_field_name("lhs")
      assert lhs is not None, "invalid lhs (None)"
      assert lhs.type == "identifier_ref", f"invalid lhs ({lhs.type})"
      rhs = node.child_by_field_name("rhs")
      assert rhs is not None, "invalid lhs (None)"
      assert lhs.text is not None, "invalid lhs text (None)"
      return SingleElemDomainFunction(
        lhs.text.decode("utf-8"), tlaplus_value_to_dataclass(rhs)
      )
    case _:
      return None


def _simple_value_to_dataclass(node: Node) -> SimpleValue:
  match node.type:
    case "string":
      assert node.text is not None, "invalid simple value text (None)"
      return SimpleValue(node.text[1:-1].decode("utf-8"))
    case "boolean":
      match node.text:
        case b"FALSE":
          return SimpleValue(False)
        case b"TRUE":
          return SimpleValue(True)
        case _:
          raise ValueError(
            f"node type was boolean but got value {node.text!r}"
          )
    case "nat_number":
      assert node.text is not None, "invalid simple value text (None)"
      return SimpleValue(int(node.text.decode("utf-8")))
    case _:
      raise ValueError(
        f"expected simple value but got {node.text!r} which is of "
        f"type {node.type}"
      )
