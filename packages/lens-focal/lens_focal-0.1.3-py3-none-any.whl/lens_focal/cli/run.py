# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

import subprocess

from ..settings import NAME


def run_command(parser, args, extra):
    if not extra:
        extra = ["-l", "INFO"]
    subprocess.run(
        [
            "celery",
            "-A",
            "lens_focal.runner",
            "worker",
            "--hostname",
            f"{NAME}@%h",
            "-Q",
            NAME,
        ]
        + extra
    )


def run_parser(subparsers):
    parser = subparsers.add_parser("run", help="run lens focal")
    parser.set_defaults(func=run_command)
    return parser
