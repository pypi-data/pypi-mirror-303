# SPDX-FileCopyrightText: 2024 UL Research Institutes
# SPDX-License-Identifier: Apache-2.0

from lens_focal import Finding, focal_task


@focal_task
def minimal_task(resource):
    """
    This is likely the simplest task. It does nothing and always produces a
    finding.
    """
    return [
        Finding(
            description="Everything is wrong!",
            name="minimal",
            url="https://example.com",
        )
    ]
