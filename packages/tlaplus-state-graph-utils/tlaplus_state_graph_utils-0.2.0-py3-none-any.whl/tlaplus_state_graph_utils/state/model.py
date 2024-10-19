from dataclasses import dataclass
from typing import TypeAlias


@dataclass
class RecordField:
  key: str
  value: "SealedValue"


@dataclass
class Record:
  fields: list[RecordField]


@dataclass
class SingleElemDomainFunction:
  elem: str
  value: "SealedValue"


@dataclass
class FunctionMerge:
  functions: list[SingleElemDomainFunction]


@dataclass
class SimpleValue:
  value: str | bool | int


SealedValue: TypeAlias = Record | FunctionMerge | SimpleValue
