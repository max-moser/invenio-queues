# SPDX-FileCopyrightText: 2017-2022 CERN.
# SPDX-License-Identifier: MIT

"""Errors used in Invenio-Queues."""


class DuplicateQueueError(Exception):
    """Error raised when a duplicate queue is detected."""
