keycloak_quarkus
================

Install [keycloak](https://keycloak.org/) >= 20.0.0 (quarkus) server configurations.


Role Defaults
-------------

* Installation options

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_version`| keycloak.org package version | `23.0.1` |


* Service configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_ha_enabled`| Enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_quarkus_db_enabled`| Enable auto configuration for database backend | `True` if `keycloak_quarkus_ha_enabled` is True, else `False` |
|`keycloak_quarkus_admin_user`| Administration console user account | `admin` |
|`keycloak_quarkus_bind_address`| Address for binding service ports | `0.0.0.0` |
|`keycloak_quarkus_host`| Hostname for the Keycloak server | `localhost` |
|`keycloak_quarkus_port`| The port used by the proxy when exposing the hostname | `-1` |
|`keycloak_quarkus_path`| This should be set if proxy uses a different context-path for Keycloak | |
|`keycloak_quarkus_http_port`| HTTP listening port | `8080` |
|`keycloak_quarkus_https_port`| TLS HTTP listening port | `8443` |
|`keycloak_quarkus_ajp_port`| AJP port | `8009` |
|`keycloak_quarkus_jgroups_port`| jgroups cluster tcp port | `7600` |
|`keycloak_quarkus_service_user`| Posix account username | `keycloak` |
|`keycloak_quarkus_service_group`| Posix account group | `keycloak` |
|`keycloak_quarkus_service_restart_always`| systemd restart always behavior activation | `False` |
|`keycloak_quarkus_service_restart_on_failure`| systemd restart on-failure behavior activation | `False` |
|`keycloak_quarkus_service_restartsec`| systemd RestartSec | `10s` |
|`keycloak_quarkus_service_pidfile`| Pid file path for service | `/run/keycloak.pid` |
|`keycloak_quarkus_jvm_package`| RHEL java package runtime | `java-17-openjdk-headless` |
|`keycloak_quarkus_java_home`| JAVA_HOME of installed JRE, leave empty for using specified keycloak_quarkus_jvm_package RPM path | `None` |
|`keycloak_quarkus_java_opts`| Additional JVM options | `-Xms1024m -Xmx2048m` |
|`keycloak_quarkus_frontend_url`| Set the base URL for frontend URLs, including scheme, host, port and path | |
|`keycloak_quarkus_admin_url`| Set the base URL for accessing the administration console, including scheme, host, port and path | |
|`keycloak_quarkus_http_relative_path` | Set the path relative to / for serving resources. The path must start with a / | `/` |
|`keycloak_quarkus_http_enabled`| Enable listener on HTTP port | `True` |
|`keycloak_quarkus_https_key_file_enabled`| Enable listener on HTTPS port | `False` |
|`keycloak_quarkus_key_file`| The file path to a private key in PEM format | `{{ keycloak.home }}/conf/server.key.pem` |
|`keycloak_quarkus_cert_file`| The file path to a server certificate or certificate chain in PEM format | `{{ keycloak.home }}/conf/server.crt.pem` |
|`keycloak_quarkus_https_key_store_enabled`| Enable configuration of HTTPS via a key store | `False` |
|`keycloak_quarkus_key_store_file`| The file pat to the key store | `{{ keycloak.home }}/conf/key_store.p12` |
|`keycloak_quarkus_key_store_password`| Password for the key store | `""` |
|`keycloak_quarkus_https_trust_store_enabled`| Enalbe confiugration of a trust store | `False` |
|`keycloak_quarkus_trust_store_file`| The file pat to the trust store | `{{ keycloak.home }}/conf/trust_store.p12` |
|`keycloak_quarkus_trust_store_password`| Password for the trust store | `""` |


* Hostname configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_http_relative_path`| Set the path relative to / for serving resources. The path must start with a / | `/` |
|`keycloak_quarkus_hostname_strict`| Disables dynamically resolving the hostname from request headers | `true` |
|`keycloak_quarkus_hostname_strict_backchannel`| By default backchannel URLs are dynamically resolved from request headers to allow internal and external applications. If all applications use the public URL this option should be enabled. | `false` |


* Database configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_jdbc_engine` | Database engine [mariadb,postres,mssql] | `postgres` |
|`keycloak_quarkus_db_user` | User for database connection | `keycloak-user` |
|`keycloak_quarkus_db_pass` | Password for database connection | `keycloak-pass` |
|`keycloak_quarkus_jdbc_url` | JDBC URL for connecting to database | `jdbc:postgresql://localhost:5432/keycloak` |
|`keycloak_quarkus_jdbc_driver_version` | Version for JDBC driver | `9.4.1212` |


* Remote caches configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_ispn_user` | Username for connecting to infinispan | `supervisor` |
|`keycloak_quarkus_ispn_pass` | Password for connecting to infinispan | `supervisor` |
|`keycloak_quarkus_ispn_hosts` | host name/port for connecting to infinispan, eg. host1:11222;host2:11222 | `localhost:11222` |
|`keycloak_quarkus_ispn_sasl_mechanism` | Infinispan auth mechanism | `SCRAM-SHA-512` |
|`keycloak_quarkus_ispn_use_ssl` | Whether infinispan uses TLS connection | `false` |
|`keycloak_quarkus_ispn_trust_store_path` | Path to infinispan server trust certificate | `/etc/pki/java/cacerts` |
|`keycloak_quarkus_ispn_trust_store_password` | Password for infinispan certificate keystore | `changeit` |


* Install options

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_quarkus_offline_install` | Perform an offline install | `False`|
|`keycloak_quarkus_version`| keycloak.org package version | `23.0.1` |
|`keycloak_quarkus_dest`| Installation root path | `/opt/keycloak` |
|`keycloak_quarkus_download_url` | Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/{{ keycloak_quarkus_version }}/{{ keycloak_quarkus_archive }}` |
|`keycloak_quarkus_configure_firewalld` | Ensure firewalld is running and configure keycloak ports | `False` |


* Miscellaneous configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_metrics_enabled`| Whether to enable metrics | `False` |
|`keycloak_quarkus_health_enabled`| If the server should expose health check endpoints | `True` |
|`keycloak_quarkus_archive` | keycloak install archive filename | `keycloak-{{ keycloak_quarkus_version }}.zip` |
|`keycloak_quarkus_installdir` | Installation path | `{{ keycloak_quarkus_dest }}/keycloak-{{ keycloak_quarkus_version }}` |
|`keycloak_quarkus_home` | Installation work directory | `{{ keycloak_quarkus_installdir }}` |
|`keycloak_quarkus_config_dir` | Path for configuration | `{{ keycloak_quarkus_home }}/conf` |
|`keycloak_quarkus_master_realm` | Name for rest authentication realm | `master` |
|`keycloak_auth_client` | Authentication client for configuration REST calls | `admin-cli` |
|`keycloak_force_install` | Remove pre-existing versions of service | `False` |
|`keycloak_url` | URL for configuration rest calls | `http://{{ keycloak_quarkus_host }}:{{ keycloak_http_port }}` |
|`keycloak_quarkus_log`| Enable one or more log handlers in a comma-separated list | `file` |
|`keycloak_quarkus_log_level`| The log level of the root category or a comma-separated list of individual categories and their levels | `info` |
|`keycloak_quarkus_log_file`| Set the log file path and filename relative to keycloak home | `data/log/keycloak.log` |
|`keycloak_quarkus_log_format`| Set a format specific to file log entries | `%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%c] (%t) %s%e%n` |
|`keycloak_quarkus_log_target`| Set the destination of the keycloak log folder link | `/var/log/keycloak` |
|`keycloak_quarkus_proxy_mode`| The proxy address forwarding mode if the server is behind a reverse proxy | `edge` |
|`keycloak_quarkus_start_dev`| Whether to start the service in development mode (start-dev) | `False` |
|`keycloak_quarkus_transaction_xa_enabled`| Whether to use XA transactions | `True` |


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|----------|
|`keycloak_quarkus_admin_pass`| Password of console admin account | `yes` |
|`keycloak_quarkus_frontend_url`| Base URL for frontend URLs, including scheme, host, port and path | `no` |
|`keycloak_quarkus_admin_url`| Base URL for accessing the administration console, including scheme, host, port and path | `no` |


License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
