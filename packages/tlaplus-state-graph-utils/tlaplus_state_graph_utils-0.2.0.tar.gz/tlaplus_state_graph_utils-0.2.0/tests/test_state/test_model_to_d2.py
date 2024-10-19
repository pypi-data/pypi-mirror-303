from textwrap import dedent

from tlaplus_state_graph_utils.state.model_to_d2 import (
  ContainersSimpleValuesInlineNewlineSepStateToD2Renderer,
  ContainersSimpleValuesInlineStateToD2Renderer,
  ContainersStateToD2Renderer,
)
from tlaplus_state_graph_utils.state.tlaplus_to_model import (
  tlaplus_state_to_dataclasses,
)


def test_state_as_d2() -> None:
  # Setup
  state_as_tlaplus = dedent(
    r"""
    /\ a = "b"
    /\ c = [ d |-> "e", d2 |-> "e2" ]
    /\ f = ( G :> "H" @@ I :> FALSE )
    """
  )
  renderer = ContainersStateToD2Renderer()

  # Run
  d2 = renderer(tlaplus_state_to_dataclasses(state_as_tlaplus))

  # Check
  print(d2)
  assert d2 == dedent(
    """\
    var0: "a" {
      value: '"b"'
    }
    var1: "c" {
      var0: "d |->" {
        value: '"e"'
      }
      var1: "d2 |->" {
        value: '"e2"'
      }
    }
    var2: "f" {
      var0: "G :>" {
        value: '"H"'
      }
      var1: "I :>" {
        value: 'FALSE'
      }
    }"""
  )


def test_state_as_d2_simple_values_inline() -> None:
  # Setup
  state_as_tlaplus = dedent(
    r"""
    /\ a = "b"
    /\ c = [ d |-> "e", d2 |-> "e2" ]
    /\ f = ( G :> "H" @@ I :> FALSE )
    """
  )
  renderer = ContainersSimpleValuesInlineStateToD2Renderer()

  # Run
  d2 = renderer(tlaplus_state_to_dataclasses(state_as_tlaplus))

  # Check
  print(d2)
  assert d2 == dedent(
    """\
    var0: "a \\"b\\""
    var1: "c" {
      var0: "d |-> \\"e\\""
      var1: "d2 |-> \\"e2\\""
    }
    var2: "f" {
      var0: "G :> \\"H\\""
      var1: "I :> FALSE"
    }"""
  )


def test_state_as_d2_simple_values_inline_newline() -> None:
  # Setup
  state_as_tlaplus = dedent(
    r"""
    /\ a = "b"
    /\ c = [ d |-> "e", d2 |-> "e2" ]
    /\ f = ( G :> "H" @@ I :> FALSE )
    """
  )
  renderer = ContainersSimpleValuesInlineNewlineSepStateToD2Renderer()

  # Run
  d2 = renderer(tlaplus_state_to_dataclasses(state_as_tlaplus))

  # Check
  print(d2)
  assert d2 == dedent(
    """\
    var0: "a\\n \\"b\\""
    var1: "c" {
      var0: "d |->\\n \\"e\\""
      var1: "d2 |->\\n \\"e2\\""
    }
    var2: "f" {
      var0: "G :>\\n \\"H\\""
      var1: "I :>\\n FALSE"
    }"""
  )
