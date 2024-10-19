from ..utils.jsonish import Jsonish
from .model import (
  FunctionMerge,
  Record,
  RecordField,
  SealedValue,
  SimpleValue,
  SingleElemDomainFunction,
)


def model_to_itf_state_jsonish(model: dict[str, SealedValue]) -> Jsonish:
  return {
    key: _sealed_value_to_reasonable_jsonish(value)
    for key, value in model.items()
  }


def _sealed_value_to_reasonable_jsonish(
  model: SealedValue,
) -> dict[str, Jsonish] | str | int | bool:
  match model:
    case Record(fields):
      return dict(_record_field_to_key_value_tuple(rf) for rf in fields)
    case FunctionMerge(functions):
      return {
        "#map": [
          list(_single_elem_domain_function_to_key_value_tuple(fu))
          for fu in functions
        ]
      }
    case SimpleValue(value):
      return value


def _record_field_to_key_value_tuple(
  model: RecordField,
) -> tuple[str, Jsonish]:
  return model.key, _sealed_value_to_reasonable_jsonish(model.value)


def _single_elem_domain_function_to_key_value_tuple(
  model: SingleElemDomainFunction,
) -> tuple[str, Jsonish]:
  return model.elem, _sealed_value_to_reasonable_jsonish(model.value)
