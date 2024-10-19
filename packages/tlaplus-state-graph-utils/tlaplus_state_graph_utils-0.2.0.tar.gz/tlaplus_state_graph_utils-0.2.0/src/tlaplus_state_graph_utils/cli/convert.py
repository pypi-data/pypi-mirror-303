import json
from argparse import FileType
from sys import stdout
from typing import Any

from ..format_determination import GraphFormat, guess_graph_file_format
from ..graph.any_to_model import (
  CouldNotDetermineInputFormatError,
  any_file_to_model,
)
from ..graph.dot_json_to_model import dot_json_file_to_model
from ..graph.model_to_d2 import (
  BaseDiagramToD2Renderer,
  ContainersStateDiagramToD2Renderer,
  LatexStateDiagramToD2Renderer,
  SimpleStateDiagramToD2Renderer,
)
from ..graph.model_to_reasonable_json import model_to_reasonable_jsonish
from ..graph.reasonable_json_to_model import reasonable_json_file_to_model
from ..state.model_to_d2 import (
  ContainersSimpleValuesInlineNewlineSepStateToD2Renderer,
  ContainersSimpleValuesInlineStateToD2Renderer,
  ContainersStateToD2Renderer,
)
from .root import subparsers

arg_parser = subparsers.add_parser(
  name="convert",
  # Short help in subcommands list:
  help="convert between state graph formats",
  # Long help in subcommand's own --help:
  description="convert between TLA+ state graph formats/representations",
)
arg_parser.add_argument(
  "input",
  type=FileType("r"),
  default="-",
  nargs="?",
  help="input file path or '-' to use stdin (the default)",
)
arg_parser.add_argument(
  "--output",
  "-o",
  type=FileType("w"),
  default="-",
  help="output file path or '-' to use stdout (the default)",
)
arg_parser.add_argument(
  "--from",
  "-f",
  type=str,
  default=None,
  choices=["reasonable-json", "tlaplus-dot-json"],
  help="input format (guessed from extension & content if not given)",
  dest="input_format",
)
arg_parser.add_argument(
  "--to",
  "-t",
  type=str,
  default=None,
  choices=["reasonable-json", "d2"],
  help="output format (if not given, defaults to reasonable-json when "
  "outputting to stdout, otherwise guessed from extension)",
  dest="output_format",
)
arg_parser.add_argument(
  "--pretty",
  action="store_true",
  help="produce pretty-printed rather than compact output",
)

# Options only relevant for reasonable-json output:
reasonable_json_arg_parser = arg_parser.add_argument_group(
  "reasonable-json options",
  description="options relevant when outputting in reasonable-json format",
)
reasonable_json_arg_parser.add_argument(
  "--reasonable-json-structured-state",
  action="store_true",
  help="include state contents represented as structured JSON",
)
reasonable_json_arg_parser.add_argument(
  "--reasonable-json-simple-structured-state",
  action="store_true",
  help="include state contents represented as simplified structured JSON "
  "(lossy, i.e. doesn't encode all details of TLA+, but easy to work with)",
)
reasonable_json_arg_parser.add_argument(
  "--reasonable-json-itf-state",
  action="store_true",
  help="include state contents represented in ITF state format "
  "(see: https://apalache-mc.org/docs/adr/015adr-trace.html)",
)

# Options only relevant for D2 output:
d2_arg_parser = arg_parser.add_argument_group(
  "D2 options", description="options relevant when outputting in D2 format"
)
d2_arg_parser.add_argument(
  "--d2-output-state-as",
  choices=[
    "label",
    "latex",
    "nested-containers",
    "nested-containers-simple-values-inline",
    "nested-containers-simple-values-inline-newline",
  ],
  default="label",
  help="how to represent individual states in the D2 output: "
  "label: without modification as a D2 node label; "
  "latex: as a LaTeX equation which D2 will render; "
  "nested-containers: as nested containers, one per variable, record, etc.; "
  "nested-containers-simple-values-inline: as above but with terminal/simple "
  "values not getting their own container; "
  "nested-containers-simple-values-inline-newline: as above but with keys "
  "and terminal values separated by newlines",
  metavar="D2_OUTPUT_STATE_AS",
)


def run_for_cli_args(args: Any) -> None:
  # Normalize input_format arg:
  input_format: GraphFormat | None
  match args.input_format:
    case "reasonable-json":
      input_format = GraphFormat.reasonable_json
    case "tlaplus-dot-json":
      input_format = GraphFormat.tlaplus_dot_json
    case _:
      input_format = None

  match args.output_format:
    case "reasonable-json":
      output_format = GraphFormat.reasonable_json
    case "d2":
      output_format = GraphFormat.d2
    case _:
      if args.output == stdout:
        output_format = GraphFormat.reasonable_json
      else:
        guessed_output_format = guess_graph_file_format(args.output)
        if guessed_output_format is None:
          arg_parser.exit(
            status=1,
            message="ERROR: Could not guess output format from filename or "
            "contents.\nPlease specify it explicitly with --to/-t or use "
            "an output filename that makes it unambiguous.\n",
          )
        output_format = guessed_output_format

  match input_format:
    case GraphFormat.tlaplus_dot_json:
      model = dot_json_file_to_model(args.input)
    case GraphFormat.reasonable_json:
      model = reasonable_json_file_to_model(args.input)
    case None:
      try:
        model = any_file_to_model(args.input)
      except CouldNotDetermineInputFormatError:
        arg_parser.exit(
          status=1,
          message="ERROR: Could not guess input format from filename or "
          "contents.\nPlease specify it explicitly with --from/-f or use "
          "an input filename that makes it unambiguous.\n",
        )
    case _ as other:
      arg_parser.exit(
        status=1,
        message=f"ERROR: Input in format {other} is not currently supported.",
      )

  match output_format:
    case GraphFormat.reasonable_json:
      jsonish = model_to_reasonable_jsonish(
        model,
        args.reasonable_json_structured_state,
        args.reasonable_json_simple_structured_state,
        args.reasonable_json_itf_state,
      )
      if args.pretty:
        json.dump(jsonish, args.output, indent=2)
      else:
        json.dump(jsonish, args.output)
    case GraphFormat.d2:
      renderer: BaseDiagramToD2Renderer
      match args.d2_output_state_as:
        case "label":
          renderer = SimpleStateDiagramToD2Renderer()
        case "latex":
          renderer = LatexStateDiagramToD2Renderer()
        case "nested-containers":
          renderer = ContainersStateDiagramToD2Renderer(
            box_state_render=ContainersStateToD2Renderer()
          )
        case "nested-containers-simple-values-inline":
          renderer = ContainersStateDiagramToD2Renderer(
            box_state_render=ContainersSimpleValuesInlineStateToD2Renderer()
          )
        case "nested-containers-simple-values-inline-newline":
          renderer = ContainersStateDiagramToD2Renderer(
            box_state_render=(
              ContainersSimpleValuesInlineNewlineSepStateToD2Renderer()
            )
          )
        case _ as other:  # should never happen => exception fine
          raise ValueError(f"Unsupported --d2-output-state-as option: {other}")
      d2_diag = renderer(model)
      args.output.write(str(d2_diag))
    case _ as other:  # should never happen => exception fine
      raise NotImplementedError(
        f"Output in format {other} is not currently supported."
      )


arg_parser.set_defaults(func=run_for_cli_args)


def run_cli() -> None:
  args = arg_parser.parse_args()
  run_for_cli_args(args)


def main() -> None:
  run_cli()


if __name__ == "__main__":
  main()
