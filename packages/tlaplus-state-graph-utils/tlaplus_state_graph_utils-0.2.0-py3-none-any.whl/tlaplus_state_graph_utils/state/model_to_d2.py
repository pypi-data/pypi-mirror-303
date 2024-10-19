from abc import ABC, abstractmethod
from collections.abc import Mapping
from dataclasses import dataclass
from typing import Any, assert_never

from ..utils.package_extras import RequiredExtraNotInstalled

try:
  from py_d2 import D2Diagram, D2Shape  # type: ignore
except ModuleNotFoundError as e:
  e2 = e

  class RaiseD2MissingIfUsed:
    def __init__(self, *a: Any, **kw: Any) -> None:
      raise RequiredExtraNotInstalled("py_d2", "D2", "d2") from e2

  D2Diagram = RaiseD2MissingIfUsed
  D2Shape = RaiseD2MissingIfUsed

from .model import FunctionMerge, Record, SealedValue, SimpleValue


@dataclass
class BaseStateToD2Renderer(ABC):
  def __call__(self, var_name_to_dc: Mapping[str, SealedValue | str]) -> str:
    diag = D2Diagram(shapes=self.to_d2_shapes(var_name_to_dc))
    return str(diag)

  def to_d2_shapes(
    self, var_name_to_dc: Mapping[str, SealedValue | str]
  ) -> list[D2Shape]:
    return self._dataclasses_state_to_d2_recursive(var_name_to_dc)

  def _dataclasses_state_to_d2_recursive(
    self, var_name_to_dc: Mapping[str, SealedValue | str]
  ) -> list[D2Shape]:
    shapes = [
      self._dataclass_state_to_d2_recursive(var_name, dc, i)
      for i, (var_name, dc) in enumerate(var_name_to_dc.items())
    ]

    return shapes

  @abstractmethod
  def _dataclass_state_to_d2_recursive(
    self, var_name: str, dc: SealedValue | str, i: int
  ) -> D2Shape:
    ...

  def _inner_simple_value_to_tla(self, value: str | int | bool) -> str:
    match value:
      case str(string):
        return '"' + repr(string).strip("'").replace('"', r"\"") + '"'
      # Super important that this comes before int, because bool is a subtype
      # of int as far as typing is concerned... m(
      case bool(b) if b is False:
        return "FALSE"
      case bool(b) if b is True:
        return "TRUE"
      case int(integer):
        return str(integer)
      case _ as unreachable:
        assert_never(unreachable)


class ContainersStateToD2Renderer(BaseStateToD2Renderer):
  def _dataclass_state_to_d2_recursive(
    self, var_name: str, dc: SealedValue | str, i: int
  ) -> D2Shape:
    subshapes = []
    match dc:
      case Record(fields=fields):
        subshapes = self._dataclasses_state_to_d2_recursive(
          {f"{field.key} |->": field.value for field in fields},
        )
      case FunctionMerge(functions=functions):
        subshapes = self._dataclasses_state_to_d2_recursive(
          {f"{function.elem} :>": function.value for function in functions},
        )
      case SimpleValue(value=value):
        subshapes = [
          D2Shape(
            name="value",
            label=f"{self._inner_simple_value_to_tla(value)!r}",
          )
        ]
      case str() as value:
        subshapes = [D2Shape(name="value", label=f"{value!r}")]
      case _ as unreachable:
        assert_never(unreachable)

    label = f"{var_name}"
    label = '"' + label.strip("'").replace('"', '\\"') + '"'
    shape = D2Shape(name=f"var{i}", label=label)
    for subshape in subshapes:
      shape.add_shape(subshape)

    return shape


class ContainersSimpleValuesInlineStateToD2Renderer(BaseStateToD2Renderer):
  def _dataclass_state_to_d2_recursive(
    self, var_name: str, dc: SealedValue | str, i: int
  ) -> D2Shape:
    subshapes = []
    simple_value = ""
    match dc:
      case Record(fields=fields):
        subshapes = self._dataclasses_state_to_d2_recursive(
          {f"{field.key} |->": field.value for field in fields},
        )
      case FunctionMerge(functions=functions):
        subshapes = self._dataclasses_state_to_d2_recursive(
          {f"{function.elem} :>": function.value for function in functions},
        )
      case SimpleValue(value=value):
        simple_value = f" {self._inner_simple_value_to_tla(value)}"
      case str() as value:
        simple_value = f" {value}"
      case _ as unreachable:
        assert_never(unreachable)

    label = f"{var_name}{simple_value}".replace('"', r"\"")
    label = f'"{label}"'
    shape = D2Shape(name=f"var{i}", label=label)
    for subshape in subshapes:
      shape.add_shape(subshape)

    return shape


class ContainersSimpleValuesInlineNewlineSepStateToD2Renderer(
  BaseStateToD2Renderer
):
  def _dataclass_state_to_d2_recursive(
    self, var_name: str, dc: SealedValue | str, i: int
  ) -> D2Shape:
    subshapes = []
    simple_value = ""
    match dc:
      case Record(fields=fields):
        subshapes = self._dataclasses_state_to_d2_recursive(
          {f"{field.key} |->": field.value for field in fields},
        )
      case FunctionMerge(functions=functions):
        subshapes = self._dataclasses_state_to_d2_recursive(
          {f"{function.elem} :>": function.value for function in functions},
        )
      case SimpleValue(value=value):
        simple_value = f"\\n {self._inner_simple_value_to_tla(value)}"
      case str() as value:
        simple_value = f" {value}"
      case _ as unreachable:
        assert_never(unreachable)

    label = f"{var_name}{simple_value}".strip("'").replace('"', r"\"")
    label = f'"{label}"'
    shape = D2Shape(name=f"var{i}", label=label)
    for subshape in subshapes:
      shape.add_shape(subshape)

    return shape
