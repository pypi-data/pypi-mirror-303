# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

import datetime

import psycopg
from celery import Task as _Task
from celery import shared_task as _shared_task

from .models import Resource
from .settings import DATABASE_URL, NAME


def focal_task(func):
    @_shared_task(name=NAME, bind=True)
    def wrapper(self, resource_id):
        resource = self.get_resource(resource_id)
        findings = func(resource)
        if findings:
            self.save_findings(resource_id, findings)

    return wrapper


class FocalTask(_Task):
    def __init__(self):
        self._conn = psycopg.connect(DATABASE_URL)
        self._conn.autocommit = True
        self._cursor = self._conn.cursor()

    def get_resource(self, resource_id):
        self._cursor.execute(
            (
                "SELECT uri, scheme, host, port, path, query, fragment FROM core_resources WHERE id = %s"
            ),
            [resource_id],
        )
        values = self._cursor.fetchone()
        return Resource(
            uri=values[0],
            scheme=values[1],
            host=values[2],
            port=values[3],
            path=values[4],
            query=values[5],
            fragment=values[6],
        )

    def save_findings(self, resource_id, findings):
        self._cursor.executemany(
            (
                "INSERT INTO core_findings (resource_id, focal_id, description, name, url, created) "
                "VALUES (%s, %s, %s, %s, %s, %s)"
            ),
            [
                (
                    resource_id,
                    NAME,
                    finding.description,
                    finding.name,
                    finding.url,
                    datetime.datetime.now(datetime.timezone.utc),
                )
                for finding in findings
            ],
        )
