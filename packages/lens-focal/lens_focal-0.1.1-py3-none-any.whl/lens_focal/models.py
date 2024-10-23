# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Resource:
    uri: str
    scheme: str
    host: Optional[str] = None
    port: Optional[int] = None
    path: str = ""
    query: str = ""
    fragment: str = ""


@dataclass
class Finding:
    description: str
    name: str
    url: str
