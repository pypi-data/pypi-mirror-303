from typing import TypeAlias

Jsonish: TypeAlias = (
  list["Jsonish"] | dict[str, "Jsonish"] | str | int | float | None
)
