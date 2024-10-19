from ..state.model_to_itf import model_to_itf_state_jsonish
from ..state.model_to_reasonable_json import (
  model_to_reasonable_jsonish as state_model_to_reasonable_jsonish,
)
from ..state.model_to_simple_structured_json import (
  model_to_simple_structured_state_jsonish,
)
from ..state.tlaplus_to_model import tlaplus_state_to_dataclasses
from ..utils.jsonish import Jsonish
from .model import TransitionDiagram


# TODO Instead of N booleans for N possible state outputs, come up with system
#   that allows a list of outputters here (which each define their own key, so
#   maybe a dict?)
def model_to_reasonable_jsonish(
  model: TransitionDiagram,
  structured_state: bool,
  simple_structured_state: bool,
  itf_state: bool,
) -> Jsonish:
  return {
    "metadata": {
      "format": {
        "name": "reasonable-tlaplus-state-graph-json",
        "version": "0.1.1",
      },
    },
    "states": [
      {
        "id": state.id,
        "labelTlaPlus": state.label_tlaplus,
        **(
          {
            "structuredState": state_model_to_reasonable_jsonish(
              tlaplus_state_to_dataclasses(state.label_tlaplus)
            )
          }
          if structured_state
          else {}
        ),
        **(
          {
            "simpleStructuredState": model_to_simple_structured_state_jsonish(
              tlaplus_state_to_dataclasses(state.label_tlaplus)
            )
          }
          if simple_structured_state
          else {}
        ),
        **(
          {
            "itfState": model_to_itf_state_jsonish(
              tlaplus_state_to_dataclasses(state.label_tlaplus)
            )
          }
          if itf_state
          else {}
        ),
      }
      for state in model.states
    ],
    "steps": [
      {
        "id": step.id,
        "actionName": step.action_name,
        "fromStateId": step.from_state_id,
        "toStateId": step.to_state_id,
        "colorId": step.color_id,
      }
      for step in model.steps
    ],
  }
