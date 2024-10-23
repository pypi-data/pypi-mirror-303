# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

from celery import Celery

from .settings import BROKER_URL, MODULES, NAME, TIME_ZONE

app = Celery(
    f"lens:focal:{NAME}",
    task_cls="lens_focal.tasks:FocalTask",
    broker_url=BROKER_URL,
    timezone=TIME_ZONE,
    broker_connection_retry_on_startup=True,
    imports=MODULES,
)
app.autodiscover_tasks()
