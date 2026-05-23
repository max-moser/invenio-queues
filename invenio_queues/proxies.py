# SPDX-FileCopyrightText: 2016-2022 CERN.
# SPDX-License-Identifier: MIT

"""Proxy to the current queues module."""

from flask import current_app
from werkzeug.local import LocalProxy

current_queues = LocalProxy(lambda: current_app.extensions["invenio-queues"])
