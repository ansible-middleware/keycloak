============================================
middleware_automation.keycloak Release Notes
============================================

.. contents:: Topics

This changelog describes changes after version 0.2.6.

v1.0.7
======

Breaking Changes / Porting Guide
--------------------------------

- keycloak_quarkus: use absolute path for certificate files `#39 <https://github.com/ansible-middleware/keycloak/pull/39>`_

Bugfixes
--------

- keycloak_quarkus: use become for tasks that will otherwise fail `#38 <https://github.com/ansible-middleware/keycloak/pull/38>`_

v1.0.6
======

Bugfixes
--------

- keycloak_quarkus: add selected java to PATH in systemd unit `#34 <https://github.com/ansible-middleware/keycloak/pull/34>`_
- keycloak_quarkus: set logfile path correctly under keycloak home `#35 <https://github.com/ansible-middleware/keycloak/pull/35>`_

v1.0.5
======

Minor Changes
-------------

- Update config options: keycloak and quarkus `#32 <https://github.com/ansible-middleware/keycloak/pull/32>`_

v1.0.4
======

v1.0.3
======

Major Changes
-------------

- New role for installing keycloak >= 17.0.0 (quarkus) `#29 <https://github.com/ansible-middleware/keycloak/pull/29>`_

Minor Changes
-------------

- Add ``keycloak_config_override_template`` parameter for passing a custom xml config template `#30 <https://github.com/ansible-middleware/keycloak/pull/30>`_

Bugfixes
--------

- Make sure systemd unit starts with selected java JVM `#31 <https://github.com/ansible-middleware/keycloak/pull/31>`_

v1.0.2
======

Minor Changes
-------------

- Make ``keycloak_admin_password`` a default with assert (was: role variable) `#26 <https://github.com/ansible-middleware/keycloak/pull/26>`_
- Simplify dependency install logic and reduce play execution time `#19 <https://github.com/ansible-middleware/keycloak/pull/19>`_

Bugfixes
--------

- Set ``keycloak_frontend_url`` default according to other defaults `#25 <https://github.com/ansible-middleware/keycloak/pull/25>`_

v1.0.1
======

Release Summary
---------------

Minor enhancements, bug and documentation fixes.


Major Changes
-------------

- Apply latest cumulative patch of RH-SSO automatically when new parameter ``keycloak_rhsso_apply_patches`` is ``true`` `#18 <https://github.com/ansible-middleware/keycloak/pull/18>`_

Minor Changes
-------------

- Clustered installs now perform database initialization on first node to avoid locking issues `#17 <https://github.com/ansible-middleware/keycloak/pull/17>`_

v1.0.0
======

Release Summary
---------------

This is the first stable release of the ``middleware_automation.keycloak`` collection.

