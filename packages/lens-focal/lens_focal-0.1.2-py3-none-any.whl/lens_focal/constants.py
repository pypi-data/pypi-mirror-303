# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

BASE_DIR = Path(__file__).parent.absolute()

COMMAND_DIR = BASE_DIR / "cli"

COMMANDS = sorted(
    [path.stem for path in COMMAND_DIR.glob("*.py") if not path.stem.startswith("_")]
)
