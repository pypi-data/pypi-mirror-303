from argparse import ArgumentParser

__version__ = "0.1.0"

arg_parser = ArgumentParser(
  description="utilities for working with TLA+ state graphs"
)
arg_parser.add_argument(
  "--version", action="version", version=f"%(prog)s {__version__}"
)

subparsers = arg_parser.add_subparsers(
  required=True,
  metavar="COMMAND",
  title="subcommands",
  help="description",
)
