from enum import StrEnum, auto


class GraphFormat(StrEnum):
  # Input only
  tlaplus_dot_json = auto()

  # Input and output
  reasonable_json = auto()

  # Output only
  d2 = auto()
