from typing import IO, Any


def get_file_filename(file: IO[Any]) -> str | None:
  """
  Get a file-like object's filename if available or `None` otherwise.

  May return "pseudo-filenames" such as `"<stdin>"` for standard input, so the
  returned filename **must not** be relied upon as representing anything in the
  actual filesystem.
  """
  # `name` is as-yet undocumented but present in `typing.IO` so should be fine:
  # https://github.com/python/cpython/issues/124565
  try:
    return str(file.name)
  # AttributeError-catching is preferred over hasattr() b/c many file-like
  # objects implement `name` as a property delegating to a wrapped file-like
  # object, but a hasattr() for a property always returns True even when it's
  # not available on the wrapped object.
  except AttributeError:
    return None
