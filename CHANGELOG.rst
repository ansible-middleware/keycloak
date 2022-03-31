============================================
middleware_automation.keycloak Release Notes
============================================

.. contents:: Topics

This changelog describes changes after version 0.2.6.

v1.0.1
======

Release Summary
---------------

Minor enhancements, bug and documentation fixes.


Minor Changes
-------------

- apply latest cumulative patch of RH-SSO automatically when new parameter ``keycloak_rhsso_apply_patches`` is ``true``

Bugfixes
--------

- clustered installs now perform database initialization on first node to avoid locking issues

v1.0.0
======

Release Summary
---------------

This is the first stable release of the ``middleware_automation.keycloak`` collection.

