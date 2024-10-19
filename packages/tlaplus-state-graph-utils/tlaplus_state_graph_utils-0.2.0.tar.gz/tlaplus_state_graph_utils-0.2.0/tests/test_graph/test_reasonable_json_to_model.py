# More tests for this can be found in test_any_to_model, these are just the
# ones for specialized features.
# TODO: Move/duplicate a lot of the ones from test_any_to_model here.

import json
from io import StringIO

from tlaplus_state_graph_utils.graph.model import State, TransitionDiagram
from tlaplus_state_graph_utils.graph.reasonable_json_to_model import (
  reasonable_json_file_to_model,
)


def test_style_class() -> None:
  # Setup
  reasonable_json = {
    "metadata": {
      "format": {
        "name": "reasonable-tlaplus-state-graph-json",
        "version": "0.1.1",
      }
    },
    "states": [
      {"id": 1, "labelTlaPlus": r"/\ a = 1", "styleClass": "someclass"},
    ],
    "steps": [],
  }
  # Run
  model = reasonable_json_file_to_model(StringIO(json.dumps(reasonable_json)))
  # Check
  assert model == TransitionDiagram(
    states=[State(id=1, label_tlaplus=r"/\ a = 1", style_class="someclass")],
    steps=[],
  )
