import json
from typing import IO, Any

from ..utils.jsonish import Jsonish
from .model import State, Step, TransitionDiagram


def dot_json_file_to_model(file: IO[Any]) -> TransitionDiagram:
  "Convenience function to parse file as JSON & call `dot_jsonish_to_model`."
  return dot_jsonish_to_model(json.load(file))


def dot_jsonish_to_model(d: Jsonish) -> TransitionDiagram:
  # There is little point getting static types right for dynamically loaded
  # data - if something is wrong here, an exception gets raised. So:
  d_: Any = d
  # Extract relevant parts
  edge_ds = d_["edges"]
  object_ds = d_["objects"]
  state_object_ds = [
    o
    for o in object_ds
    if o["label"]
    and o.get("shape") != "record"
    and o.get("name") != "cluster_legend"
  ]
  legend_ds = [d for d in object_ds if d.get("shape") == "record"]
  legend_color_to_action_name = {d["fillcolor"]: d["name"] for d in legend_ds}

  # Construct dataclass instances
  states = [
    State(
      id=d["_gvid"],
      label_tlaplus=d["label"]
      .replace("\\\\", "\\")
      .replace("\\n", "\n")
      .replace("\\\\", "\\"),
      style_class=None,
    )
    for d in state_object_ds
  ]
  steps = [
    Step(
      id=d["_gvid"],
      action_name=legend_color_to_action_name[d["color"]],
      from_state_id=d["tail"],
      to_state_id=d["head"],
      color_id=d["color"],
    )
    for d in edge_ds
  ]
  return TransitionDiagram(states, steps)
