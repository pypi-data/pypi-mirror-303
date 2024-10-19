from typing import IO, Any

from .formats import GraphFormat
from .utils.io import get_file_filename


def guess_graph_file_format(file: IO[Any]) -> GraphFormat | None:
  filename = get_file_filename(file)
  if filename is None:
    return None
  lower_filename = filename.lower()
  if lower_filename.endswith(".dot.json"):
    return GraphFormat.tlaplus_dot_json
  elif lower_filename.endswith(".reasonable.json"):
    return GraphFormat.reasonable_json
  elif lower_filename.endswith(".d2"):
    return GraphFormat.d2
  else:  # give up
    return None


__all__ = ["guess_graph_file_format", "GraphFormat"]
