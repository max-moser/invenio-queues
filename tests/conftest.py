# SPDX-FileCopyrightText: 2017-2022 CERN.
# SPDX-License-Identifier: MIT

"""Pytest configuration."""

from collections import namedtuple
from unittest.mock import patch

import pytest
from flask import Flask
from invenio_base.utils import entry_points
from kombu import Exchange

MOCK_MQ_EXCHANGE = Exchange(
    "test_events",
    type="direct",
    delivery_mode="transient",  # in-memory queue
    durable=True,
)


def remove_queues(app):
    """Delete all queues declared on the current app."""
    with app.app_context():
        ext = app.extensions["invenio-queues"]
        for name, queue in ext.queues.items():
            if queue.exists:
                queue.queue.delete()


def mock_iter_entry_points_factory(data):
    """Create a mock iter_entry_points function."""

    def entrypoints(group=None, name=None):
        if group is None or group == "invenio_queues.queues":
            for entrypoint in data:
                yield entrypoint
        else:
            for x in entry_points(group=group):
                if name is None or x.name == name:
                    yield x

    return entrypoints


@pytest.fixture
def MockEntryPoint():
    """Mock entry point for testing."""
    return namedtuple("MockEntryPoint", ["name", "value", "group", "load"])


@pytest.fixture()
def test_queues_entrypoints(app, MockEntryPoint):
    """Declare some queues by mocking the invenio_queues.queues entrypoint.

    It yields a list like [{name: queue_name, exchange: conf}, ...].
    """
    data = []
    result = []
    for idx in range(5):
        queue_name = "queue{}".format(idx)
        conf = dict(name=queue_name, exchange=MOCK_MQ_EXCHANGE)
        entrypoint = MockEntryPoint(
            name=queue_name,
            value=queue_name,
            group="invenio_queues.queues",
            load=lambda conf=conf: (lambda: [conf]),
        )
        data.append(entrypoint)
        result.append(conf)

    entrypoints = mock_iter_entry_points_factory(data)

    with patch("importlib.metadata.entry_points", entrypoints):
        try:
            yield result
        finally:
            remove_queues(app)


@pytest.fixture()
def test_queues(app, test_queues_entrypoints):
    """Declare test queues."""
    with app.app_context():
        ext = app.extensions["invenio-queues"]
        for conf in test_queues_entrypoints:
            queue = ext.queues[conf["name"]]
            queue.queue.declare()
            assert queue.exists
    yield test_queues_entrypoints


@pytest.fixture()
def app():
    """Flask application fixture."""
    from invenio_queues import InvenioQueues

    app_ = Flask("testapp")
    app_.config.update(
        SECRET_KEY="SECRET_KEY",
        TESTING=True,
    )
    InvenioQueues(app_)
    return app_
