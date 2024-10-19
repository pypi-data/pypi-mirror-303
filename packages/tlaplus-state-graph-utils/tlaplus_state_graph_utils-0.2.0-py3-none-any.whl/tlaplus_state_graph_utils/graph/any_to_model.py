from dataclasses import dataclass
from io import StringIO
from typing import IO, Any

from ..format_determination import GraphFormat, guess_graph_file_format
from .dot_json_to_model import dot_json_file_to_model
from .model import TransitionDiagram
from .reasonable_json_to_model import reasonable_json_file_to_model


@dataclass
class CouldNotDetermineInputFormatError(Exception):
  file: IO[Any]


def any_file_to_model(file: IO[Any]) -> TransitionDiagram:
  """
  Raises:
    CouldNotDetermineInputFormatError: If the format of `file` could not be
      determined from its name and contents.
  """
  input_format = guess_graph_file_format(file)
  match input_format:
    case GraphFormat.tlaplus_dot_json:
      return dot_json_file_to_model(file)
    case GraphFormat.reasonable_json:
      return reasonable_json_file_to_model(file)
    case _:
      # TODO Refactor w/r/t to ^
      # Fall back to guessing based on content, which we do by just trying one
      # option after another:
      file = StringIO(file.read())  # TODO: Replace w/ seekable wrapper (lib?)
      start_pos = file.tell()  # remember current position for rewinding
      try:
        return dot_json_file_to_model(file)
      except Exception:
        file.seek(start_pos)  # rewind & move on
      try:
        return reasonable_json_file_to_model(file)
      except Exception:
        file.seek(start_pos)  # rewind & move on
      # We've exhausted all options, so give up:
      raise CouldNotDetermineInputFormatError(file)
