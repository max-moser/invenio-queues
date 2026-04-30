..
    This file is part of Invenio.
    Copyright (C) 2017-2023 CERN.
    Copyright (C) 2025 Graz University of Technology.

    Invenio is free software; you can redistribute it and/or modify it
    under the terms of the MIT License; see LICENSE file for more details.


Changes
=======

Version v1.0.3 (released 2026-04-30)

- fix(ext): make `current_queues.queues` property thread-safe

Version v1.0.2 (released 2025-10-28)

- fix: reusable workflows
- fix(tests): removed deprecation warnings
- fix: tests for python 3.9
- fix: Replaced pkg_resources with importlib
- chore: updated dependencies

Version 1.0.1 (release 2024-01-15)
----------------------------------

- Fix consumer and producer connection closing

Version 1.0.0a2 (release 2020-10-08)
------------------------------------

- Changes license to MIT
- Adds support for Python 3 and dependencies upgrade
- Improves documentation
- Integrates pytest-invenio 1.4

Version 1.0.0a2 (release 2019-11-08)
------------------------------------

- Removes amqp dependency because it breaks pip dependency resolution
  and the same version is already included in kombu

Version 1.0.0a1 (release 2017-08-19)
------------------------------------

- Initial public release.
