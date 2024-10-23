# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

from decouple import Csv, config

BROKER_URL = config("LENS_BROKER_URL", cast=str, default="redis://localhost:6379/0")

DATABASE_URL = config(
    "LENS_DATABASE_URL", cast=str, default="postgres://localhost:5432/lens"
)

MODULES = config("LENS_MODULES", cast=Csv(), default="main")

NAME = config("LENS_NAME", cast=str)

TIME_ZONE = config("LENS_TIME_ZONE", cast=str, default="Etc/UTC")
