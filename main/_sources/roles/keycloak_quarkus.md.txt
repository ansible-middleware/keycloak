keycloak_quarkus
================

Install [keycloak](https://keycloak.org/) >= 17.0.0 (quarkus) server configurations.


Role Defaults
-------------

* Service configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_ha_enabled`| Enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_quarkus_db_enabled`| Enable auto configuration for database backend | `True` if `keycloak_quarkus_ha_enabled` is True, else `False` |
|`keycloak_quarkus_admin_user`| Administration console user account | `admin` |
|`keycloak_quarkus_bind_address`| Address for binding service ports | `0.0.0.0` |
|`keycloak_quarkus_host`| hostname | `localhost` |
|`keycloak_quarkus_http_port`| HTTP port | `8080` |
|`keycloak_quarkus_https_port`| TLS HTTP port | `8443` |
|`keycloak_quarkus_ajp_port`| AJP port | `8009` |
|`keycloak_quarkus_jgroups_port`| jgroups cluster tcp port | `7600` |
|`keycloak_quarkus_java_opts`| Additional JVM options | `-Xms1024m -Xmx2048m` |
|`keycloak_quarkus_service_user`| Posix account username | `keycloak` |
|`keycloak_quarkus_service_group`| Posix account group | `keycloak` |
|`keycloak_quarkus_service_pidfile`| Pid file path for service | `/run/keycloak.pid` |
|`keycloak_quarkus_jvm_package`| RHEL java package runtime | `java-11-openjdk-headless` |
|`keycloak_quarkus_frontend_url`| Service public URL | `http://localhost:8080/auth` |
|`keycloak_quarkus_http_relative_path` | Service context path | `auth` |


* Database configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_jdbc_engine` | Database engine [mariadb,postres] | `postgres` |
|`keycloak_quarkus_db_user` | User for database connection | `keycloak-user` |
|`keycloak_quarkus_db_pass` | Password for database connection | `keycloak-pass` |
|`keycloak_quarkus_jdbc_url` | JDBC URL for connecting to database | `jdbc:postgresql://localhost:5432/keycloak` |
|`keycloak_quarkus_jdbc_driver_version` | Version for JDBC driver | `9.4.1212` |


* Remote caches configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_ispn_user` | Username for connecting to infinispan | `supervisor` |
|`keycloak_quarkus_ispn_pass` | Password for connecting to infinispan | `supervisor` |
|`keycloak_quarkus_ispn_url` | URL for connecting to infinispan | `localhost` |
|`keycloak_quarkus_ispn_sasl_mechanism` | Infinispan auth mechanism | `SCRAM-SHA-512` |
|`keycloak_quarkus_ispn_use_ssl` | Whether infinispan uses TLS connection | `false` |
|`keycloak_quarkus_ispn_trust_store_path` | Path to infinispan server trust certificate | `/etc/pki/java/cacerts` |
|`keycloak_quarkus_ispn_trust_store_password` | Password for infinispan certificate keystore | `changeit` | 


* Install options

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_quarkus_offline_install` | Perform an offline install | `False`|
|`keycloak_quarkus_download_url`| Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/<version>/<archive>`| 
|`keycloak_quarkus_version`| keycloak.org package version | `17.0.1` |
|`keycloak_quarkus_dest`| Installation root path | `/opt/keycloak` |
|`keycloak_quarkus_download_url` | Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/{{ keycloak_quarkus_version }}/{{ keycloak_quarkus_archive }}` |
|`keycloak_quarkus_configure_firewalld` | Ensure firewalld is running and configure keycloak ports | `False` |


* Miscellaneous configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_metrics_enabled`| Whether to enable metrics | `False` |
|`keycloak_quarkus_archive` | keycloak install archive filename | `keycloak-{{ keycloak_quarkus_version }}.zip` |
|`keycloak_quarkus_installdir` | Installation path | `{{ keycloak_quarkus_dest }}/keycloak-{{ keycloak_quarkus_version }}` |
|`keycloak_quarkus_home` | Installation work directory | `{{ keycloak_quarkus_installdir }}` |
|`keycloak_quarkus_config_dir` | Path for configuration | `{{ keycloak_quarkus_home }}/conf` |
|`keycloak_quarkus_master_realm` | Name for rest authentication realm | `master` |
|`keycloak_auth_client` | Authentication client for configuration REST calls | `admin-cli` |
|`keycloak_force_install` | Remove pre-existing versions of service | `False` |
|`keycloak_url` | URL for configuration rest calls | `http://{{ keycloak_quarkus_host }}:{{ keycloak_http_port }}` |
|`keycloak_management_url` | URL for management console rest calls | `http://{{ keycloak_quarkus_host }}:{{ keycloak_management_http_port }}` |


Role Variables
--------------

| Variable | Description |
|:---------|:------------|
|`keycloak_quarkus_admin_pass`| Password of console admin account |


License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
