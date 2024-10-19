from ..utils.jsonish import Jsonish
from .model import (
  FunctionMerge,
  Record,
  RecordField,
  SealedValue,
  SimpleValue,
  SingleElemDomainFunction,
)

# TODO Move to model_to_structured_json or sth. b/c this is not strictly part
# of the reasonable-json format


def model_to_reasonable_jsonish(model: dict[str, SealedValue]) -> Jsonish:
  return {
    key: _sealed_value_to_reasonable_jsonish(value)
    for key, value in model.items()
  }


def _sealed_value_to_reasonable_jsonish(model: SealedValue) -> Jsonish:
  match model:
    case Record(fields):
      return {
        "type": "record",
        "fields": [_record_field_to_reasonable_jsonish(rf) for rf in fields],
      }
    case FunctionMerge(functions):
      return {
        "type": "functionMerge",
        "functions": [
          _single_elem_domain_function_to_reasonable_jsonish(fu)
          for fu in functions
        ],
      }
    case SimpleValue(value):
      return {"type": "simpleValue", "value": value}


def _record_field_to_reasonable_jsonish(model: RecordField) -> Jsonish:
  return {
    "type": "recordField",
    "key": model.key,
    "value": _sealed_value_to_reasonable_jsonish(model.value),
  }


def _single_elem_domain_function_to_reasonable_jsonish(
  model: SingleElemDomainFunction,
) -> Jsonish:
  return {
    "type": "singleElemDomainFunction",
    "elem": model.elem,
    "value": _sealed_value_to_reasonable_jsonish(model.value),
  }
