import json
from typing import IO, Any

from .model import State, Step, TransitionDiagram


def reasonable_json_file_to_model(file: IO[Any]) -> TransitionDiagram:
  # Parse JSON
  d = json.load(file)

  # Check metadata version
  try:
    version_str = d["metadata"]["format"]["version"]
    version = tuple(int(x) for x in version_str.split("."))
    if len(version) < 3:
      version = (*version, 0)
  except Exception as e:
    raise ValueError(
      "Couldn't determine format version (see errors above)"
    ) from e
  if not (0, 1, 0) <= version < (0, 2, 0):
    raise ValueError(f"Can't handle format version {version_str}")

  # Construct dataclass instances
  states = [
    State(
      id=state_d["id"],
      label_tlaplus=state_d["labelTlaPlus"],
      style_class=state_d.get("styleClass"),
    )
    for state_d in d["states"]
  ]
  steps = [
    Step(
      id=step_d["id"],
      action_name=step_d["actionName"],
      from_state_id=step_d["fromStateId"],
      to_state_id=step_d["toStateId"],
      color_id=step_d["colorId"],
    )
    for step_d in d["steps"]
  ]

  return TransitionDiagram(states, steps)
