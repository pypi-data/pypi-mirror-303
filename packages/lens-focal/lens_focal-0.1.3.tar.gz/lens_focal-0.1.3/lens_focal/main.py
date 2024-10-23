# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

import argparse
from importlib import import_module

from ._version import __version__
from .constants import COMMANDS


def get_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--version", action="version", version=f"lens-focal {__version__}"
    )

    subparsers = parser.add_subparsers(required=True)

    for command_name in COMMANDS:
        command = import_module(f".{command_name}", "lens_focal.cli")
        getattr(command, f"{command_name}_parser")(subparsers=subparsers)

    return parser


def main(args=None):
    parser = get_parser()
    args, extra = parser.parse_known_args(args)
    args.func(parser=parser, args=args, extra=extra)
