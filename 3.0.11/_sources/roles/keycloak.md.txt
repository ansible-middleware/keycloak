keycloak
========

Install [keycloak](https://keycloak.org/) or [Red Hat Single Sign-On](https://access.redhat.com/products/red-hat-single-sign-on) server configurations.


Requirements
------------

This role requires the `python3-netaddr` library installed on the controller node.

* to install via yum/dnf: `dnf install python3-netaddr`
* to install via apt: `apt install python3-netaddr`
* or via pip: `pip install netaddr==0.8.0`
* or via the collection: `pip install -r requirements.txt`


Dependencies
------------

The roles depends on:

* [middleware_automation.common](https://github.com/ansible-middleware/common)
* [ansible-posix](https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html)

To install all the dependencies via galaxy:

    ansible-galaxy collection install -r requirements.yml


Versions
--------

| RH-SSO VERSION | Release Date      | Keycloak Version | EAP Version | Notes           |
|:---------------|:------------------|:-----------------|:------------|:----------------|
|`7.5.0 GA`      |September 20, 2021 |`15.0.2`          | `7.4.6`     |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_single_sign-on/7.5/html/release_notes/index)|
|`7.6.0 GA`      |June 30, 2022      |`18.0.3`          | `7.4.6`     |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_single_sign-on/7.6/html-single/release_notes/index)|


Patching
--------

When variable `keycloak_rhsso_apply_patches` is `true` (default: `false`), the role will automatically apply the latest cumulative patch for the selected base version.

| RH-SSO VERSION | Release Date      | RH-SSO LATEST CP | Notes           |
|:---------------|:------------------|:-----------------|:----------------|
|`7.5.0 GA`      |January 20, 2022   |`7.5.3 GA`        |[Release Notes](https://access.redhat.com/articles/6646321)|
|`7.6.0 GA`      |November 11, 2022  |`7.6.1 GA`        |[Release Notes](https://access.redhat.com/articles/6982711)|


Role Defaults
-------------

* Service configuration

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_ha_enabled`| Enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_ha_discovery`| Discovery protocol for HA cluster members | `JDBC_PING` if `keycloak_db_enabled` else `TCPPING` |
|`keycloak_db_enabled`| Enable auto configuration for database backend | `True` if `keycloak_ha_enabled` is True, else `False` |
|`keycloak_remote_cache_enabled`| Enable remote cache store when in clustered ha configurations | `True` if `keycloak_ha_enabled` else `False` |
|`keycloak_admin_user`| Administration console user account | `admin` |
|`keycloak_bind_address`| Address for binding service ports | `0.0.0.0` |
|`keycloak_management_port_bind_address`| Address for binding management ports | `127.0.0.1` |
|`keycloak_host`| hostname | `localhost` |
|`keycloak_http_port`| HTTP port | `8080` |
|`keycloak_https_port`| TLS HTTP port | `8443` |
|`keycloak_ajp_port`| AJP port | `8009` |
|`keycloak_jgroups_port`| jgroups cluster tcp port | `7600` |
|`keycloak_management_http_port`| Management port | `9990` |
|`keycloak_management_https_port`| TLS management port | `9993` |
|`keycloak_prefer_ipv4`| Prefer IPv4 stack and addresses for port binding | `true` |
|`keycloak_config_standalone_xml`| filename for configuration | `keycloak.xml` |
|`keycloak_service_user`| posix account username | `keycloak` |
|`keycloak_service_group`| posix account group | `keycloak` |
|`keycloak_service_restart_always`| systemd restart always behavior activation | `False` |
|`keycloak_service_restart_on_failure`| systemd restart on-failure behavior activation | `False` |
|`keycloak_service_startlimitintervalsec`| systemd StartLimitIntervalSec | `300` |
|`keycloak_service_startlimitburst`| systemd StartLimitBurst | `5` |
|`keycloak_service_restartsec`| systemd RestartSec | `10s` |
|`keycloak_service_pidfile`| pid file path for service | `/run/keycloak/keycloak.pid` |
|`keycloak_features` | List of `name`/`status` pairs of features (also known as profiles on RH-SSO) to `enable` or `disable`, example: `[ { name: 'docker', status: 'enabled' } ]` | `[]`
|`keycloak_jvm_package`| RHEL java package runtime | `java-1.8.0-openjdk-headless` |
|`keycloak_java_home`| `JAVA_HOME` of installed JRE, leave empty for using RPM path at `keycloak_jvm_package` | `None` |
|`keycloak_java_opts`| Additional JVM options | `-Xms1024m -Xmx2048m` |


* Install options

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_offline_install` | perform an offline install | `false`|
|`keycloak_download_url`| Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/<version>/<archive>`|
|`keycloak_version`| keycloak.org package version | `18.0.2` |
|`keycloak_dest`| Installation root path | `/opt/keycloak` |
|`keycloak_download_url` | Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/{{ keycloak_version }}/{{ keycloak_archive }}` |
|`keycloak_configure_firewalld` | Ensure firewalld is running and configure keycloak ports | `false` |


* Miscellaneous configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_archive` | keycloak install archive filename | `keycloak-legacy-{{ keycloak_version }}.zip` |
|`keycloak_download_url_9x` | Download URL for keycloak (deprecated) | `https://downloads.jboss.org/keycloak/{{ keycloak_version }}/{{ keycloak_archive }}` |
|`keycloak_installdir` | Installation path | `{{ keycloak_dest }}/keycloak-{{ keycloak_version }}` |
|`keycloak_jboss_home` | Installation work directory | `{{ keycloak_rhsso_installdir }}` |
|`keycloak_jboss_port_offset` | Port offset for the JBoss socket binding | `0` |
|`keycloak_config_dir` | Path for configuration | `{{ keycloak_jboss_home }}/standalone/configuration` |
|`keycloak_config_path_to_standalone_xml` | Custom path for configuration | `{{ keycloak_jboss_home }}/standalone/configuration/{{ keycloak_config_standalone_xml }}` |
|`keycloak_config_override_template` | Path to custom template for standalone.xml configuration | `''` |
|`keycloak_auth_realm` | Name for rest authentication realm | `master` |
|`keycloak_auth_client` | Authentication client for configuration REST calls | `admin-cli` |
|`keycloak_force_install` | Remove pre-existing versions of service | `false` |
|`keycloak_url` | URL for configuration rest calls | `http://{{ keycloak_host }}:{{ keycloak_http_port + keycloak_jboss_port_offset }}` |
|`keycloak_management_url` | URL for management console rest calls | `http://{{ keycloak_host }}:{{ keycloak_management_http_port + keycloak_jboss_port_offset }}` |
|`keycloak_frontend_url_force` | Force backend requests to use the frontend URL | `false` |
|`keycloak_db_background_validation` | Enable background validation of database connection | `false` |
|`keycloak_db_background_validation_millis`| How frequenly the connection pool is validated in the background | `10000` if background validation enabled |
|`keycloak_db_background_validate_on_match` | Enable validate on match for database connections | `false` |
|`keycloak_frontend_url` | frontend URL for keycloak endpoint | `http://localhost:8080/auth/` |
|`keycloak_log_target`| Set the destination of the keycloak log folder link | `/var/log/keycloak` |


Role Variables
--------------

The following are a set of _required_ variables for the role:

| Variable | Description |
|:---------|:------------|
|`keycloak_admin_password`| Password for the administration console user account (minimum 12 characters) |
|`keycloak_frontend_url` | frontend URL for keycloak endpoint | `http://localhost:8080/auth/` |


The following parameters are _required_ only when `keycloak_ha_enabled` is true:

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_modcluster_enabled`| Enable configuration for modcluster subsystem | `True` if `keycloak_ha_enabled` is True, else `False` |
|`keycloak_modcluster_url` | _deprecated_ Host for the modcluster reverse proxy | `localhost` |
|`keycloak_modcluster_port` | _deprecated_ Port for the modcluster reverse proxy | `6666` |
|`keycloak_modcluster_urls` | List of {host,port} dicts for the modcluster reverse proxies | `[ { localhost:6666 } ]` |
|`keycloak_jdbc_engine` | backend database engine when db is enabled: [ postgres, mariadb, sqlserver ] | `postgres` |
|`keycloak_infinispan_url` | URL for the infinispan remote-cache server | `localhost:11122` |
|`keycloak_infinispan_user` | username for connecting to infinispan | `supervisor` |
|`keycloak_infinispan_pass` | password for connecting to infinispan | `supervisor` |
|`keycloak_infinispan_sasl_mechanism`| Authentication type | `SCRAM-SHA-512` |
|`keycloak_infinispan_use_ssl`| Enable hotrod TLS communication | `False` |
|`keycloak_infinispan_trust_store_path`| Path to truststore with infinispan server certificate | `/etc/pki/java/cacerts` |
|`keycloak_infinispan_trust_store_password`| Password for opening truststore | `changeit` |


The following parameters are _required_ only when `keycloak_db_enabled` is true:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_jdbc_url` | URL for the postgres backend database | `jdbc:postgresql://localhost:5432/keycloak` |
|`keycloak_jdbc_driver_version`| Version for the JDBC driver to download | `9.4.1212` |
|`keycloak_db_user` | username for connecting to postgres | `keycloak-user` |
|`keycloak_db_pass` | password for connecting to postgres | `keycloak-pass` |


The following variables are _optional_:

| Variable | Description |
|:---------|:------------|
|`keycloak_db_valid_conn_sql` | Override the default database connection validation query sql |
|`keycloak_admin_url` | Override the default administration endpoint URL |
|`keycloak_jgroups_subnet`| Override the subnet match for jgroups cluster formation; if not defined, it will be inferred from local machine route configuration |

Example Playbook
-----------------

* The following is an example playbook that makes use of the role to install keycloak from remote:

```yaml
---
- hosts: ...
      vars:
        keycloak_admin_password: "remembertochangeme"
      roles:
        - middleware_automation.keycloak.keycloak
```


* The following example playbook makes use of the role to install keycloak from the controller node:

```yaml
---
- hosts: ...
      collections:
        - middleware_automation.keycloak
      tasks:
        - name: Include keycloak role
          include_role:
            name: keycloak
          vars:
            keycloak_admin_password: "remembertochangeme"
            keycloak_offline_install: true
            # This should be the filename of keycloak archive on Ansible node: keycloak-16.1.0.zip
```

License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
* [Romain Pelisse](https://github.com/rpelisse)
* [Pavan Kumar Motaparthi](https://github.com/motaparthipavankumar)
