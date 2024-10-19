from . import convert
from .root import arg_parser


def run_cli(input_args: list[str] | None = None) -> None:
  arg_parser.set_defaults(func=convert.run_for_cli_args)

  args = arg_parser.parse_args(input_args)

  args.func(args)


def main() -> None:
  run_cli()


__all__ = ["convert"]
