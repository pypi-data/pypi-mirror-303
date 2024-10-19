import subprocess as sp
from textwrap import dedent

import pytest

from tlaplus_state_graph_utils.graph.model import State, Step, TransitionDiagram
from tlaplus_state_graph_utils.graph.model_to_d2 import (
  ContainersStateDiagramToD2Renderer,
  LatexStateDiagramToD2Renderer,
  SimpleStateDiagramToD2Renderer,
  model_to_d2_str,
)
from tlaplus_state_graph_utils.state.model_to_d2 import (
  ContainersSimpleValuesInlineNewlineSepStateToD2Renderer,
  ContainersSimpleValuesInlineStateToD2Renderer,
  ContainersStateToD2Renderer,
)


def format_d2(d2: str) -> str:
  cp = sp.run(
    ["d2", "fmt", "-"], input=d2, check=True, encoding="utf-8", stdout=sp.PIPE
  )
  return cp.stdout


# Tests based on long example:


def test_long_example_containers_simple_values_inline_against_reference(
  long_example_model: TransitionDiagram,
  long_example_d2_containers_simple_values_inline: str,
) -> None:
  # Run
  d2 = format_d2(
    model_to_d2_str(
      long_example_model,
      renderer=ContainersStateDiagramToD2Renderer(
        ContainersSimpleValuesInlineStateToD2Renderer()
      ),
    )
  )

  # Uncomment to regenerate:
  # from pathlib import Path
  # Path("tests/data/long-example/containers-simple-values-inline.d2").write_text(d2)

  # Check
  assert d2 == long_example_d2_containers_simple_values_inline


def test_long_example_containers_simple_values_inline_newline_against_reference(
  long_example_model: TransitionDiagram,
  long_example_d2_containers_simple_values_inline_newline: str,
) -> None:
  # Run
  d2 = format_d2(
    model_to_d2_str(
      long_example_model,
      renderer=ContainersStateDiagramToD2Renderer(
        ContainersSimpleValuesInlineNewlineSepStateToD2Renderer()
      ),
    )
  )

  # Uncomment to regenerate:
  # from pathlib import Path
  # Path(
  # "tests/data/long-example/containers-simple-values-inline-newline.d2"
  # ).write_text(d2)

  # Check
  assert d2 == long_example_d2_containers_simple_values_inline_newline


def test_long_example_containers_simple_values_not_inline_against_reference(
  long_example_model: TransitionDiagram,
  long_example_d2_containers_simple_values_not_inline: str,
) -> None:
  # Run
  d2 = format_d2(
    model_to_d2_str(
      long_example_model,
      renderer=ContainersStateDiagramToD2Renderer(
        ContainersStateToD2Renderer()
      ),
    )
  )

  # Uncomment to regenerate:
  # from pathlib import Path
  # Path("tests/data/long-example/containers-simple-values-not-inline.d2").write_text(
  # d2
  # )

  # Check
  assert d2 == long_example_d2_containers_simple_values_not_inline


def test_long_example_latex_against_reference(
  long_example_model: TransitionDiagram,
  long_example_d2_latex: str,
) -> None:
  # Run
  d2 = format_d2(
    model_to_d2_str(
      long_example_model, renderer=LatexStateDiagramToD2Renderer()
    )
  )

  # Uncomment to regenerate:
  # from pathlib import Path
  # Path("tests/data/long-example/latex.d2").write_text(d2)

  # Check
  assert d2 == long_example_d2_latex


def test_long_example_non_latex_against_reference(
  long_example_model: TransitionDiagram,
  long_example_d2_non_latex: str,
) -> None:
  # Run
  d2 = format_d2(
    model_to_d2_str(
      long_example_model, renderer=SimpleStateDiagramToD2Renderer()
    )
  )

  # Uncomment to regenerate:
  # from pathlib import Path
  # Path("tests/data/long-example/non-latex.d2").write_text(d2)

  # Check
  assert d2 == long_example_d2_non_latex


# Shorter, more focused tests for individual features:


def test_style_class() -> None:
  # Setup
  # TODO Simplify to use single state, cf. test
  model = TransitionDiagram(
    states=[
      State(id=1, label_tlaplus=r"/\ a = 1", style_class="someclass"),
      State(id=2, label_tlaplus=r"/\ a = 2", style_class="someclass"),
    ],
    steps=[
      Step(
        id=1,
        action_name="Action",
        from_state_id=1,
        to_state_id=2,
        color_id="1",
      )
    ],
  )
  # Run
  d2 = format_d2(
    model_to_d2_str(
      model,
      renderer=ContainersStateDiagramToD2Renderer(
        ContainersSimpleValuesInlineStateToD2Renderer()
      ),
    )
  )

  # Check
  assert d2 == dedent(
    """\
    state1: "" {
      class: someclass
      var0: "a 1"
    }
    state2: "" {
      class: someclass
      var0: "a 2"
    }
    state1 -> state2: "Action" {
      style: {
        stroke: blue
      }
    }
    """
  )


# TODO: As soon as this becomes XPASS due to the d2 bug being fixed, we can
#   use the possibility to have just single states to simplify the test
@pytest.mark.xfail(
  reason="d2 fmt bug: https://github.com/terrastruct/d2/issues/1577"
)
def test_single_state_no_steps() -> None:
  """
  This tests the test setup or rather d2 fmt more than anything
  """
  # Setup
  model = TransitionDiagram(
    states=[
      State(id=1, label_tlaplus=r"/\ a = 1", style_class="someclass"),
    ],
    steps=[],
  )
  # Run
  d2 = format_d2(
    model_to_d2_str(
      model,
      renderer=ContainersStateDiagramToD2Renderer(
        ContainersSimpleValuesInlineStateToD2Renderer()
      ),
    )
  )

  # Check
  assert d2 == dedent(
    """\
    state1: "" {
      class: someclass
      var0: "a 1"
    }
    """
  )
