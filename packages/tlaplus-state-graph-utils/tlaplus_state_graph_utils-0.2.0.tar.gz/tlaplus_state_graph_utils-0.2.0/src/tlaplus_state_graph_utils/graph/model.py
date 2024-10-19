from dataclasses import dataclass


@dataclass
class State:
  id: int
  label_tlaplus: str

  # styling
  style_class: str | None


@dataclass
class Step:
  id: int
  action_name: str
  from_state_id: int
  to_state_id: int
  color_id: str


@dataclass
class TransitionDiagram:
  states: list[State]
  steps: list[Step]
