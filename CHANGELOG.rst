=============================================
middleware\_automation.keycloak Release Notes
=============================================

.. contents:: Topics

This changelog describes changes after version 0.2.6.

v2.1.1
======

Minor Changes
-------------

- Add reverse ``proxy_headers`` config, supersedes ``proxy_mode`` `#187 <https://github.com/ansible-middleware/keycloak/pull/187>`_
- Debian/Ubuntu compatibility `#178 <https://github.com/ansible-middleware/keycloak/pull/178>`_
- Use ``keycloak_realm`` as default for sub-entities `#180 <https://github.com/ansible-middleware/keycloak/pull/180>`_

Bugfixes
--------

- Fix permissions on controller-side downloaded artifacts `#184 <https://github.com/ansible-middleware/keycloak/pull/184>`_
- JVM args moved to ``JAVA_OPTS`` envvar (instead of JAVA_OPTS_APPEND) `#186 <https://github.com/ansible-middleware/keycloak/pull/186>`_
- Unrelax configuration file permissions `#191 <https://github.com/ansible-middleware/keycloak/pull/191>`_
- Utilize comment filter for ``ansible_managed`` annotations `#176 <https://github.com/ansible-middleware/keycloak/pull/176>`_

v2.1.0
======

Major Changes
-------------

- Implement infinispan TCPPING discovery protocol `#159 <https://github.com/ansible-middleware/keycloak/pull/159>`_

Minor Changes
-------------

- Set enable-recovery when xa transactions are enabled `#167 <https://github.com/ansible-middleware/keycloak/pull/167>`_
- keycloak_quarkus: Allow configuring log rotate options in quarkus configuration `#161 <https://github.com/ansible-middleware/keycloak/pull/161>`_
- keycloak_quarkus: ``sticky-session`` for infinispan routes `#163 <https://github.com/ansible-middleware/keycloak/pull/163>`_

Breaking Changes / Porting Guide
--------------------------------

- keycloak_quarkus: renamed infinispan host list configuration `#157 <https://github.com/ansible-middleware/keycloak/pull/157>`_

Bugfixes
--------

- keycloak_quarkus: fix custom JAVA_HOME parameter name `#171 <https://github.com/ansible-middleware/keycloak/pull/171>`_

v2.0.2
======

Minor Changes
-------------

- keycloak_quarkus: Add support for sqlserver jdbc driver `#148 <https://github.com/ansible-middleware/keycloak/pull/148>`_
- keycloak_quarkus: allow configuration of ``hostname-strict-backchannel`` `#152 <https://github.com/ansible-middleware/keycloak/pull/152>`_
- keycloak_quarkus: systemd restart behavior `#145 <https://github.com/ansible-middleware/keycloak/pull/145>`_

Bugfixes
--------

- keycloak_quarkus: Use ``keycloak_quarkus_java_opts`` `#154 <https://github.com/ansible-middleware/keycloak/pull/154>`_
- keycloak_quarkus: allow ports <1024 (e.g. :443) in systemd unit `#150 <https://github.com/ansible-middleware/keycloak/pull/150>`_

v2.0.1
======

Minor Changes
-------------

- keycloak_quarkus: add hostname-strict parameter `#139 <https://github.com/ansible-middleware/keycloak/pull/139>`_
- keycloak_quarkus: update to version 23.0.1 `#133 <https://github.com/ansible-middleware/keycloak/pull/133>`_

Bugfixes
--------

- keycloak_quarkus: template requires lowercase boolean values `#138 <https://github.com/ansible-middleware/keycloak/pull/138>`_

v2.0.0
======

Minor Changes
-------------

- Add new parameter for port offset configuration `#124 <https://github.com/ansible-middleware/keycloak/pull/124>`_
- Update Keycloak to version 22.0.5 `#122 <https://github.com/ansible-middleware/keycloak/pull/122>`_

Breaking Changes / Porting Guide
--------------------------------

- Add support for more http-related configs `#115 <https://github.com/ansible-middleware/keycloak/pull/115>`_
- Update minimum ansible-core version > 2.14 `#119 <https://github.com/ansible-middleware/keycloak/pull/119>`_
- keycloak_quarkus: enable config of key store and trust store `#116 <https://github.com/ansible-middleware/keycloak/pull/116>`_

v1.3.0
======

Major Changes
-------------

- Run service as ``keycloak_service_user`` `#106 <https://github.com/ansible-middleware/keycloak/pull/106>`_

Minor Changes
-------------

- keycloak_quarkus: Update Keycloak to version 22.0.3 `#112 <https://github.com/ansible-middleware/keycloak/pull/112>`_
- keycloak_quarkus: fix admin console redirect when running locally `#111 <https://github.com/ansible-middleware/keycloak/pull/111>`_
- keycloak_quarkus: skip proxy config if ``keycloak_quarkus_proxy_mode`` is ``none`` `#109 <https://github.com/ansible-middleware/keycloak/pull/109>`_

Bugfixes
--------

- keycloak_quarkus: fix validation failure upon port configuration change `#113 <https://github.com/ansible-middleware/keycloak/pull/113>`_

v1.2.8
======

Minor Changes
-------------

- keycloak_quarkus: set openjdk 17 as default `#103 <https://github.com/ansible-middleware/keycloak/pull/103>`_
- keycloak_quarkus: update to version 22.0.1 `#107 <https://github.com/ansible-middleware/keycloak/pull/107>`_

Bugfixes
--------

- Fix incorrect checks for ``keycloak_jgroups_subnet`` `#98 <https://github.com/ansible-middleware/keycloak/pull/98>`_
- Undefine ``keycloak_db_valid_conn_sql`` default `#91 <https://github.com/ansible-middleware/keycloak/pull/91>`_
- Update bindep.txt package python3-devel to support RHEL9 `#105 <https://github.com/ansible-middleware/keycloak/pull/105>`_

v1.2.7
======

Minor Changes
-------------

- Allow to override jgroups subnet `#93 <https://github.com/ansible-middleware/keycloak/pull/93>`_
- keycloak-quarkus: update keycloakx to v21.1.1 `#92 <https://github.com/ansible-middleware/keycloak/pull/92>`_

v1.2.6
======

Minor Changes
-------------

- Add profile features enabling/disabling `#87 <https://github.com/ansible-middleware/keycloak/pull/87>`_
- Improve service restart behavior configuration `#88 <https://github.com/ansible-middleware/keycloak/pull/88>`_
- Update default xa_datasource_class value for mariadb jdbc configuration `#89 <https://github.com/ansible-middleware/keycloak/pull/89>`_

Bugfixes
--------

- Handle WFLYCTL0117 when background validation millis is 0 `#90 <https://github.com/ansible-middleware/keycloak/pull/90>`_

v1.2.5
======

Minor Changes
-------------

- Add configuration for database connection pool validation `#85 <https://github.com/ansible-middleware/keycloak/pull/85>`_
- Allow to configure administration endpoint URL `#86 <https://github.com/ansible-middleware/keycloak/pull/86>`_
- Allow to force backend URLs to frontend URLs `#84 <https://github.com/ansible-middleware/keycloak/pull/84>`_
- Introduce systemd unit restart behavior `#81 <https://github.com/ansible-middleware/keycloak/pull/81>`_

v1.2.4
======

Minor Changes
-------------

- Add ``sqlserver`` to keycloak role jdbc configurations `#78 <https://github.com/ansible-middleware/keycloak/pull/78>`_
- Add configurability for XA transactions `#73 <https://github.com/ansible-middleware/keycloak/pull/73>`_

Bugfixes
--------

- Fix deprecation warning for ``ipaddr`` `#77 <https://github.com/ansible-middleware/keycloak/pull/77>`_
- Fix undefined facts when offline patching sso `#71 <https://github.com/ansible-middleware/keycloak/pull/71>`_

v1.2.1
======

Minor Changes
-------------

- Allow to setup keycloak HA cluster without remote cache store `#68 <https://github.com/ansible-middleware/keycloak/pull/68>`_

Bugfixes
--------

- Pass attributes to realm clients `#69 <https://github.com/ansible-middleware/keycloak/pull/69>`_

v1.2.0
======

Major Changes
-------------

- Provide config for multiple modcluster proxies `#60 <https://github.com/ansible-middleware/keycloak/pull/60>`_

Minor Changes
-------------

- Allow to configure TCPPING for cluster discovery `#62 <https://github.com/ansible-middleware/keycloak/pull/62>`_
- Drop community.general from dependencies `#61 <https://github.com/ansible-middleware/keycloak/pull/61>`_
- Switch middleware_automation.redhat_csp_download for middleware_automation.common `#63 <https://github.com/ansible-middleware/keycloak/pull/63>`_
- Switch to middleware_automation.common for rh-sso patching `#64 <https://github.com/ansible-middleware/keycloak/pull/64>`_

v1.1.1
======

Bugfixes
--------

- keycloak-quarkus: fix ``cache-config-file`` path in keycloak.conf.j2 template `#53 <https://github.com/ansible-middleware/keycloak/pull/53>`_

v1.1.0
======

Minor Changes
-------------

- Update keycloak to 18.0.2 - sso to 7.6.1 `#46 <https://github.com/ansible-middleware/keycloak/pull/46>`_
- Variable ``keycloak_no_log`` controls ansible ``no_log`` parameter (for debugging purposes) `#47 <https://github.com/ansible-middleware/keycloak/pull/47>`_
- Variables to override service start retries and delay `#51 <https://github.com/ansible-middleware/keycloak/pull/51>`_
- keycloak_quarkus: variable to enable development mode `#45 <https://github.com/ansible-middleware/keycloak/pull/45>`_

Breaking Changes / Porting Guide
--------------------------------

- Rename variables from ``infinispan_`` prefix to ``keycloak_infinispan_`` `#42 <https://github.com/ansible-middleware/keycloak/pull/42>`_

Bugfixes
--------

- keycloak_quarkus: fix /var/log/keycloak symlink to keycloak log directory `#44 <https://github.com/ansible-middleware/keycloak/pull/44>`_

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
