from importlib.abc import Traversable
from io import StringIO

import pytest
from tlaplus_state_graph_utils.graph.any_to_model import (
  CouldNotDetermineInputFormatError,
  any_file_to_model,
)
from tlaplus_state_graph_utils.graph.model import TransitionDiagram


def test_dot_json(
  long_example_dot_json_traversable: Traversable,
  long_example_model: TransitionDiagram,
) -> None:
  with long_example_dot_json_traversable.open() as f:
    model = any_file_to_model(f)
  assert model == long_example_model


def test_reasonable_json(
  long_example_reasonable_json_traversable: Traversable,
  long_example_model: TransitionDiagram,
) -> None:
  with long_example_reasonable_json_traversable.open() as f:
    model = any_file_to_model(f)
  assert model == long_example_model


def test_d2_unsupported(
  long_example_d2_containers_simple_values_inline_traversable: Traversable,
  long_example_model: TransitionDiagram,
) -> None:
  with long_example_d2_containers_simple_values_inline_traversable.open() as f, (
    pytest.raises(CouldNotDetermineInputFormatError)
  ):
    any_file_to_model(f)


def test_random_garbage_unsupported(
  long_example_model: TransitionDiagram,
) -> None:
  with pytest.raises(CouldNotDetermineInputFormatError):
    any_file_to_model(StringIO("nonsense"))
