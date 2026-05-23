# SPDX-FileCopyrightText: 2017-2020 CERN.
# SPDX-License-Identifier: MIT

"""Invenio Queues utility functions."""

from flask import current_app
from kombu import Connection
from kombu.pools import connections


def get_connection_pool():
    """Retrieve the broker connection pool."""
    broker_url = current_app.config.get("QUEUES_BROKER_URL") or current_app.config.get(
        "BROKER_URL", "amqp://"
    )
    return connections[Connection(broker_url)]
