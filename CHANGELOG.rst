=============================================
middleware\_automation.keycloak Release Notes
=============================================

.. contents:: Topics

This changelog describes changes after version 0.2.6.

v3.0.2
======

Minor Changes
-------------

- New ``checksum`` property for keycloak_quarkus_providers `#280 <https://github.com/ansible-middleware/keycloak/pull/280>`_
- New parameter to set the jgroups host IP address `#281 <https://github.com/ansible-middleware/keycloak/pull/281>`_
- Session storage / distributed caches `#287 <https://github.com/ansible-middleware/keycloak/pull/287>`_
- Update keycloak/RHBK to v26.2.4 `#283 <https://github.com/ansible-middleware/keycloak/pull/283>`_

Bugfixes
--------

- Fix ``keycloak_quarkus_force_install`` parameter being ignored by install `#296 <https://github.com/ansible-middleware/keycloak/pull/296>`_
- Fix alternate download location being ignored (JBossNeworkAPI always used) `#298 <https://github.com/ansible-middleware/keycloak/pull/298>`_
- Run config rebuild after SPI providers update `#285 <https://github.com/ansible-middleware/keycloak/pull/285>`_
- Use jdk21 as default in debian `#289 <https://github.com/ansible-middleware/keycloak/pull/289>`_
- keycloak_realm: federation default provider type should be a string `#302 <https://github.com/ansible-middleware/keycloak/pull/302>`_

v3.0.1
======

Minor Changes
-------------

- Version update to 26.0.8 / rhbk 26.0.11 `#277 <https://github.com/ansible-middleware/keycloak/pull/277>`_

Bugfixes
--------

- Trigger rebuild handler on envvars file change `#276 <https://github.com/ansible-middleware/keycloak/pull/276>`_

v3.0.0
======

Minor Changes
-------------

- Add theme cache invalidation handler `#252 <https://github.com/ansible-middleware/keycloak/pull/252>`_
- keycloak_realm: change url variables to defaults `#268 <https://github.com/ansible-middleware/keycloak/pull/268>`_

Breaking Changes / Porting Guide
--------------------------------

- Bump major and ansible-core versions `#266 <https://github.com/ansible-middleware/keycloak/pull/266>`_
- Rename parameters to follow upstream `#270 <https://github.com/ansible-middleware/keycloak/pull/270>`_
- Update for keycloak v26 `#254 <https://github.com/ansible-middleware/keycloak/pull/254>`_

Bugfixes
--------

- Access token lifespan is too short for ansible run `#251 <https://github.com/ansible-middleware/keycloak/pull/251>`_
- Load environment vars during kc rebuild `#274 <https://github.com/ansible-middleware/keycloak/pull/274>`_
- Rebuild config and restart service for local providers `#250 <https://github.com/ansible-middleware/keycloak/pull/250>`_
- Rename and honour parameter ``keycloak_quarkus_http_host`` `#271 <https://github.com/ansible-middleware/keycloak/pull/271>`_

New Modules
-----------

- middleware_automation.keycloak.keycloak_realm - Allows administration of Keycloak realm via Keycloak API

v2.4.3
======

Minor Changes
-------------

- Update keycloak to 24.0.5 `#241 <https://github.com/ansible-middleware/keycloak/pull/241>`_

v2.4.2
======

Minor Changes
-------------

- New parameter ``keycloak_quarkus_download_path``  `#239 <https://github.com/ansible-middleware/keycloak/pull/239>`_

Bugfixes
--------

- Add wait_for_port number parameter `#237 <https://github.com/ansible-middleware/keycloak/pull/237>`_

v2.4.1
======

Release Summary
---------------

Internal release, documentation or test changes only.

v2.4.0
======

Major Changes
-------------

- Enable by default health check on restart `#234 <https://github.com/ansible-middleware/keycloak/pull/234>`_
- Update minimum ansible-core version > 2.15 `#232 <https://github.com/ansible-middleware/keycloak/pull/232>`_

v2.3.0
======

Major Changes
-------------

- Allow for custom providers hosted on maven repositories `#223 <https://github.com/ansible-middleware/keycloak/pull/223>`_
- Restart handler strategy behaviour `#231 <https://github.com/ansible-middleware/keycloak/pull/231>`_

Minor Changes
-------------

- Add support for policy files `#225 <https://github.com/ansible-middleware/keycloak/pull/225>`_
- Allow to add extra custom env vars in sysconfig file `#229 <https://github.com/ansible-middleware/keycloak/pull/229>`_
- Download from alternate URL with optional http authentication `#220 <https://github.com/ansible-middleware/keycloak/pull/220>`_
- Update Keycloak to version 24.0.4 `#218 <https://github.com/ansible-middleware/keycloak/pull/218>`_
- ``proxy-header`` enhancement `#227 <https://github.com/ansible-middleware/keycloak/pull/227>`_

Bugfixes
--------

- ``kc.sh build`` uses configured jdk `#211 <https://github.com/ansible-middleware/keycloak/pull/211>`_

v2.2.2
======

Minor Changes
-------------

- Copying of key material for TLS configuration `#210 <https://github.com/ansible-middleware/keycloak/pull/210>`_
- Validate certs parameter for JDBC driver downloads `#207 <https://github.com/ansible-middleware/keycloak/pull/207>`_

Bugfixes
--------

- Turn off controller privilege escalation `#209 <https://github.com/ansible-middleware/keycloak/pull/209>`_

v2.2.1
======

Release Summary
---------------

Internal release, documentation or test changes only.

Bugfixes
--------

- JDBC provider: fix clause in argument validation `#204 <https://github.com/ansible-middleware/keycloak/pull/204>`_

v2.2.0
======

Major Changes
-------------

- Support java keystore for configuration of sensitive options `#189 <https://github.com/ansible-middleware/keycloak/pull/189>`_

Minor Changes
-------------

- Add ``wait_for_port`` and ``wait_for_log`` systemd unit logic `#199 <https://github.com/ansible-middleware/keycloak/pull/199>`_
- Customize jdbc driver downloads, optional authentication `#202 <https://github.com/ansible-middleware/keycloak/pull/202>`_
- Keystore-based vault SPI configuration `#196 <https://github.com/ansible-middleware/keycloak/pull/196>`_
- New ``keycloak_quarkus_hostname_strict_https`` parameter `#195 <https://github.com/ansible-middleware/keycloak/pull/195>`_
- Providers config and custom providers `#201 <https://github.com/ansible-middleware/keycloak/pull/201>`_
- Remove administrator credentials from files once keycloak is bootstrapped `#197 <https://github.com/ansible-middleware/keycloak/pull/197>`_
- Update keycloak to 24.0 `#194 <https://github.com/ansible-middleware/keycloak/pull/194>`_

v2.1.2
======

Release Summary
---------------

Internal release, documentation or test changes only.

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

Release Summary
---------------

Internal release, documentation or test changes only.

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
