import re
from importlib.abc import Traversable
from importlib.resources import as_file
from pathlib import Path

import pytest
from pytest import CaptureFixture
from tlaplus_state_graph_utils.cli import run_cli
from tlaplus_state_graph_utils.graph.model import TransitionDiagram
from tlaplus_state_graph_utils.graph.reasonable_json_to_model import (
  reasonable_json_file_to_model,
)


def test_cli_version(capsys: CaptureFixture[str]) -> None:
  with pytest.raises(SystemExit) as exc_info:
    run_cli(["--version"])

  assert exc_info.value.code == 0
  out, err = capsys.readouterr()
  assert re.match("[a-zA-Z]+ [0-9]+[.][0-9]+[.][0-9]+", out)


def test_convert_dot_json(
  long_example_model: TransitionDiagram,
  long_example_dot_json_traversable: Traversable,
  tmp_path: Path,
) -> None:
  output_path = tmp_path / "out.reasonable.json"

  with as_file(long_example_dot_json_traversable) as input_path:
    run_cli(["convert", str(input_path), "-o", str(output_path)])

  with output_path.open() as f:
    output_model = reasonable_json_file_to_model(f)
  assert output_model == long_example_model
