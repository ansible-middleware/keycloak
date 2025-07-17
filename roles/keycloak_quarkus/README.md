keycloak_quarkus
================
<!--start description -->
Install [keycloak](https://keycloak.org/) >= 20.0.0 (quarkus) server configurations.
<!--end description -->

Requirements
------------

This role requires the `python3-netaddr` and `lxml` library installed on the controller node.

* to install via yum/dnf: `dnf install python3-netaddr python3-lxml`
* to install via apt: `apt install python3-netaddr python3-lxml`
* or via the collection: `pip install -r requirements.txt`


Dependencies
------------

The roles depends on:

* [middleware_automation.common](https://github.com/ansible-middleware/common)
* [ansible-posix](https://docs.ansible.com/ansible/latest/collections/ansible/posix/index.html)

To install all the dependencies via galaxy:

    ansible-galaxy collection install -r requirements.yml

Role Defaults
-------------

#### Installation options

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_version`| keycloak.org package version | `26.3.0` |
|`keycloak_quarkus_offline_install` | Perform an offline install | `False`|
|`keycloak_quarkus_dest`| Installation root path | `/opt/keycloak` |
|`keycloak_quarkus_download_url` | Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/{{ keycloak_quarkus_version }}/{{ keycloak_quarkus_archive }}` |
|`keycloak_quarkus_download_path`| Path local to controller for offline/download of install archives | `{{ lookup('env', 'PWD') }}` |


#### Service configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_bootstrap_admin_user`| Administration console user account | `admin` |
|`keycloak_quarkus_admin_user`| Deprecated, use `keycloak_quarkus_bootstrap_admin_user` instead. | |
|`keycloak_quarkus_bind_address`| Deprecated, use `keycloak_quarkus_http_host` instead |  `0.0.0.0` |
|`keycloak_quarkus_host`| Deprecated, use `keycloak_quarkus_hostname` instead. | |
|`keycloak_quarkus_port`| Deprecated, use `keycloak_quarkus_hostname` instead. | |
|`keycloak_quarkus_path`| Deprecated, use `keycloak_quarkus_hostname` instead. | |
|`keycloak_quarkus_service_user`| Posix account username | `keycloak` |
|`keycloak_quarkus_service_group`| Posix account group | `keycloak` |
|`keycloak_quarkus_service_restart_always`| systemd restart always behavior activation | `False` |
|`keycloak_quarkus_service_restart_on_failure`| systemd restart on-failure behavior activation | `False` |
|`keycloak_quarkus_service_restartsec`| systemd RestartSec | `10s` |
|`keycloak_quarkus_jvm_package`| RHEL java package runtime | `java-21-openjdk-headless` |
|`keycloak_quarkus_java_home`| JAVA_HOME of installed JRE, leave empty for using specified keycloak_quarkus_jvm_package RPM path | `None` |
|`keycloak_quarkus_java_heap_opts`| Heap memory JVM setting | `-Xms1024m -Xmx2048m` |
|`keycloak_quarkus_java_jvm_opts`| Other JVM settings | same as keycloak |
|`keycloak_quarkus_java_opts`| JVM arguments; if overridden, it takes precedence over `keycloak_quarkus_java_*` | `{{ keycloak_quarkus_java_heap_opts + ' ' + keycloak_quarkus_java_jvm_opts }}` |
|`keycloak_quarkus_additional_env_vars` | List of additional env variables of { key: str, value: str} to be put in sysconfig file, see https://www.keycloak.org/server/all-config | `[]` |
|`keycloak_quarkus_frontend_url`| Deprecated, use `keycloak_quarkus_hostname` instead. | |
|`keycloak_quarkus_admin_url`| Deprecated, use `keycloak_quarkus_hostname_admin` instead. | |
|`keycloak_quarkus_health_check_url`| Full URL (including scheme, host, path, fragment etc.) used for health check endpoint; keycloak_quarkus_hostname will NOT be prepended; helpful when health checks should happen against http port, but keycloak_quarkus_hostname uses https scheme per default | `` |
|`keycloak_quarkus_health_check_url_path`| Path to the health check endpoint; keycloak_quarkus_hostname will be prepended automatically; Note that keycloak_quarkus_health_check_url takes precedence over this property | `realms/master/.well-known/openid-configuration` |
|`keycloak_quarkus_proxy_headers`| Parse reverse proxy headers (`forwarded` or `xforwarded`) | `""` |
|`keycloak_quarkus_config_key_store_file`| Path to the configuration key store; only used if `keycloak_quarkus_keystore_password` is not empty  | `{{ keycloak.home }}/conf/conf_store.p12` if `keycloak_quarkus_keystore_password != ''`, else `''` |
|`keycloak_quarkus_config_key_store_password`| Password of the configuration keystore; if non-empty, `keycloak_quarkus_db_pass` will be saved to the keystore at `keycloak_quarkus_config_key_store_file` instead of being written to the configuration file in clear text | `""` |
|`keycloak_quarkus_configure_firewalld` | Ensure firewalld is running and configure keycloak ports | `False` |
|`keycloak_quarkus_configure_iptables` | Ensure iptables is configured for keycloak ports | `False` |


#### High-availability

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_ha_enabled`| Enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_quarkus_ha_discovery`| Discovery protocol for HA cluster members | `JDBCPING` |
|`keycloak_quarkus_db_enabled`| Enable auto configuration for database backend | `True` if `keycloak_quarkus_ha_enabled` is True, else `False` |
|`keycloak_quarkus_jgroups_ip`| Host jgroups IP.  If changing this variable you must make sure it is always set for all hosts in your cluster. | `{{ ansible_default_ipv4.address }}` |
|`keycloak_quarkus_jgroups_port`| jgroups cluster tcp port | `7800` |
|`keycloak_quarkus_systemd_wait_for_port` | Whether systemd unit should wait for keycloak port before returning | `{{ keycloak_quarkus_ha_enabled }}` |
|`keycloak_quarkus_systemd_wait_for_port_number`| Which port the systemd unit should wait for | `{{ keycloak_quarkus_https_port }}` |
|`keycloak_quarkus_systemd_wait_for_log` | Whether systemd unit should wait for service to be up in logs | `false` |
|`keycloak_quarkus_systemd_wait_for_timeout`| How long to wait for service to be alive (seconds) | `60` |
|`keycloak_quarkus_systemd_wait_for_delay`| Activation delay for service systemd unit (seconds) | `10` |
|`keycloak_quarkus_restart_strategy`| Strategy task file for restarting in HA (one of provided restart/['serial.yml','none.yml','serial_then_parallel.yml']) or path to file when providing custom strategy | `restart/serial.yml` |
|`keycloak_quarkus_restart_health_check`| Whether to wait for successful health check after restart | `true` |
|`keycloak_quarkus_restart_health_check_delay`| Seconds to let pass before starting healch checks | `10` |
|`keycloak_quarkus_restart_health_check_retries`| Number of attempts for successful health check before failing | `25` |
|`keycloak_quarkus_restart_pause`| Seconds to wait between restarts in HA strategy | `15` |


#### Hostname configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_hostname`| Address at which is the server exposed. Can be a full URL, or just a hostname. When only hostname is provided, scheme, port and context path are resolved from the request. | |
|`keycloak_quarkus_hostname_admin`| Set the base URL for accessing the administration console, including scheme, host, port and path | |
|`keycloak_quarkus_hostname_strict`| Disables dynamically resolving the hostname from request headers | `true` |
|`keycloak_quarkus_hostname_backchannel_dynamic`| Enables dynamic resolving of backchannel URLs, including hostname, scheme, port and context path. Set to true if your application accesses Keycloak via a private network. If set to true, hostname option needs to be specified as a full URL. | `false` |
|`keycloak_quarkus_hostname_strict_backchannel`| Deprecated, use (the inverted!)`keycloak_quarkus_hostname_backchannel_dynamic` instead. |  |


#### HTTP(S) configuration
| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_http_relative_path`| Set the path relative to / for serving resources. The path must start with a / | `/` |
|`keycloak_quarkus_http_host`| The http host, ie. the address used to bind the service |  `0.0.0.0` |
|`keycloak_quarkus_http_port`| HTTP listening port | `8080` |
|`keycloak_quarkus_https_port`| TLS HTTP listening port | `8443` |
|`keycloak_quarkus_http_management_port`| Port of the management interface. Relevant only when something is exposed on the management interface - see the guide for details. | `9000` |
|`keycloak_quarkus_https_key_store_file`| The file path to the key store | `{{ keycloak.home }}/conf/key_store.p12` |
|`keycloak_quarkus_https_key_store_password`| Password for the key store | `""` |
|`keycloak_quarkus_https_trust_store_enabled`| Enable configuration of the https trust store | `False` |
|`keycloak_quarkus_https_trust_store_file`| The file path to the trust store | `{{ keycloak.home }}/conf/trust_store.p12` |
|`keycloak_quarkus_https_trust_store_password`| Password for the trust store | `""` |
|`keycloak_quarkus_https_key_file_enabled`| Enable listener on HTTPS port | `False` |
|`keycloak_quarkus_key_file_copy_enabled`| Enable copy of key file to target host | `False` |
|`keycloak_quarkus_key_content`| Content of the TLS private key. Use `"{{ lookup('file', 'server.key.pem') }}"` to lookup a file. | `""` |
|`keycloak_quarkus_key_file`| The file path to a private key in PEM format | `/etc/pki/tls/private/server.key.pem` |
|`keycloak_quarkus_cert_file_copy_enabled`| Enable copy of cert file to target host | `False`|
|`keycloak_quarkus_cert_file_src`| Set the source file path | `""` |
|`keycloak_quarkus_cert_file`| The file path to a server certificate or certificate chain in PEM format | `/etc/pki/tls/certs/server.crt.pem` |
|`keycloak_quarkus_https_key_store_enabled`| Enable configuration of HTTPS via a key store | `False` |
|`keycloak_quarkus_key_store_file`| Deprecated, use `keycloak_quarkus_https_key_store_file` instead. ||
|`keycloak_quarkus_key_store_password`| Deprecated, use `keycloak_quarkus_https_key_store_password` instead.||
|`keycloak_quarkus_http_relative_path` | Set the path relative to / for serving resources. The path must start with a / | `/` |
|`keycloak_quarkus_http_management_relative_path` | Set the path relative to / for serving resources from management interface. The path must start with a /. If not given, the value is inherited from HTTP options. Relevant only when something is exposed on the management interface - see the guide for details. | `/` |
|`keycloak_quarkus_http_enabled`| Enable listener on HTTP port | `True` |


#### Database configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_db_engine` | Database engine [mariadb,postres,mssql] | `postgres` |
|`keycloak_quarkus_db_user` | User for database connection | `keycloak-user` |
|`keycloak_quarkus_db_pass` | Password for database connection | `keycloak-pass` |
|`keycloak_quarkus_db_url` | JDBC URL for connecting to database | `jdbc:postgresql://localhost:5432/keycloak` |
|`keycloak_quarkus_db_driver_version` | Version for JDBC engine driver | `9.4.1212` |


#### Cache configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_cache_remote` | Whether to connect to remote cache infinispan server | `false` |
|`keycloak_quarkus_cache_remote_username` | Username for connecting to infinispan | `supervisor` |
|`keycloak_quarkus_cache_remote_password` | Password for connecting to infinispan | `supervisor` |
|`keycloak_quarkus_cache_remote_host` | Hostname for connecting to infinispan | `localhost` |
|`keycloak_quarkus_cache_remote_port`| Port for connecting to infinispan | `11222` |
|`keycloak_quarkus_cache_remote_sasl_mechanism` | Infinispan auth mechanism | `SCRAM-SHA-512` |
|`keycloak_quarkus_cache_remote_tls_enabled` | Whether infinispan uses TLS connection | `false` |


#### Logging configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_log`| Enable one or more log handlers in a comma-separated list | `file` |
|`keycloak_quarkus_log_level`| The log level of the root category or a comma-separated list of individual categories and their levels | `info` |
|`keycloak_quarkus_log_file`| Set the log file path and filename relative to keycloak home | `data/log/keycloak.log` |
|`keycloak_quarkus_log_format`| Set a format specific to file log entries | `%d{yyyy-MM-dd HH:mm:ss,SSS} %-5p [%c] (%t) %s%e%n` |
|`keycloak_quarkus_log_target`| Set the destination of the keycloak log folder link | `/var/log/keycloak` |
|`keycloak_quarkus_log_max_file_size`| Set the maximum log file size before a log rotation happens; A size configuration option recognises string in this format (shown as a regular expression): `[0-9]+[KkMmGgTtPpEeZzYy]?`. If no suffix is given, assume bytes. | `10M` |
|`keycloak_quarkus_log_max_backup_index`| Set the maximum number of archived log files to keep | `10` |
|`keycloak_quarkus_log_file_suffix`| Set the log file handler rotation file suffix. When used, the file will be rotated based on its suffix; Note: If the suffix ends with `.zip` or `.gz`, the rotation file will also be compressed. | `.yyyy-MM-dd.zip` |


#### Miscellaneous configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_metrics_enabled`| Whether to enable metrics | `False` |
|`keycloak_quarkus_health_enabled`| If the server should expose health check endpoints on the management interface | `True` |
|`keycloak_quarkus_archive` | keycloak install archive filename | `keycloak-{{ keycloak_quarkus_version }}.zip` |
|`keycloak_quarkus_installdir` | Installation path | `{{ keycloak_quarkus_dest }}/keycloak-{{ keycloak_quarkus_version }}` |
|`keycloak_quarkus_home` | Installation work directory | `{{ keycloak_quarkus_installdir }}` |
|`keycloak_quarkus_config_dir` | Path for configuration | `{{ keycloak_quarkus_home }}/conf` |
|`keycloak_quarkus_master_realm` | Name for rest authentication realm | `master` |
|`keycloak_auth_client` | Authentication client for configuration REST calls | `admin-cli` |
|`keycloak_quarkus_force_install` | Remove pre-existing versions of service | `False` |
|`keycloak_quarkus_proxy_mode`| The proxy address forwarding mode if the server is behind a reverse proxy (deprecated) | `none` |
|`keycloak_quarkus_start_dev`| Whether to start the service in development mode (start-dev) | `False` |
|`keycloak_quarkus_transaction_xa_enabled`| Whether to use XA transactions | `True` |
|`keycloak_quarkus_spi_sticky_session_encoder_infinispan_should_attach_route`| If the route should be attached to cookies to reflect the node that owns a particular session. If false, route is not attached to cookies and we rely on the session affinity capabilities from reverse proxy | `True` |
|`keycloak_quarkus_show_deprecation_warnings`| Whether deprecation warnings should be shown | `True` |


#### Vault configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_ks_vault_enabled`| Whether to enable the vault SPI | `false` |
|`keycloak_quarkus_ks_vault_file`| The keystore path for the vault SPI | `{{ keycloak_quarkus_config_dir }}/keystore.p12` |
|`keycloak_quarkus_ks_vault_type`| Type of the keystore used for the vault SPI | `PKCS12` |


#### Configuring providers

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_providers`| List of provider definitions; see below | `[]` |

Providers support different sources:

* `url`: http download for providers not requiring authentication
* `maven`: maven download for providers hosted publicly on Apache Maven Central or private Maven repositories like Github Maven requiring authentication
* `local_path`: static providers to be uploaded

Provider definition:

```yaml
keycloak_quarkus_providers:
  - id: http-client                         # required; "{{ id }}.jar" identifies the file name on RHBK
    spi: connections                        # required if neither url, local_path nor maven are specified; required for setting properties
    default: true                           # optional, whether to set default for spi, default false
    restart: true                           # optional, whether to rebuild config and restart the service after deploying, default true
    url: https://.../.../custom_spi.jar     # optional, url for download via http
    local_path: my_theme_spi.jar            # optional, path on local controller for SPI to be uploaded
    remote: true                            # optional, whether to copy from localhost or remotely, see https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html#parameter-remote_src, default false
    maven:                                  # optional, for download using maven
      repository_url: https://maven.pkg.github.com/OWNER/REPOSITORY # optional, maven repo url
      group_id:  my.group                   # optional, maven group id
      artifact_id: artifact                 # optional, maven artifact id
      version: 24.0.5                       # optional, defaults to latest
      username:  user                       # optional, cf. https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-apache-maven-registry#authenticating-to-github-packages
      password: pat                         # optional, provide a PAT for accessing Github's Apache Maven registry
    properties:                             # optional, list of key-values
      - key: default-connection-pool-size
        value: 10
    checksum: sha256:D98291AC[...]B6DC7B97  # optional, checksum used to verify integrity:
                                            #  for `url` SPIs, use format: <algorithm>:<checksum|url>, cf. <https://docs.ansible.com/ansible/latest/collections/ansible/builtin/get_url_module.html#parameter-checksum>;
                                            #  for `local_path` SPIs, use SHA1 format <https://docs.ansible.com/ansible/latest/collections/ansible/builtin/copy_module.html#parameter-checksum>
                                            #  for `maven` SPIs, this field is ignored since maven has integrity verification methods enabled by default
```

the definition above will generate the following build command:

```
bin/kc.sh build --spi-connections-provider=http-client --spi-connections-http-client-default-connection-pool-size=10
```


#### Configuring policies

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_quarkus_policies`| List of policy definitions; see below | `[]` |

Provider definition:

```yaml
keycloak_quarkus_policies:
  - name: john-the-ripper.txt                                                                          # required, resulting file name
    url: https://github.com/danielmiessler/SecLists/raw/master/Passwords/Software/john-the-ripper.txt  # required, url for download
    type: password-blacklists                                                                          # optional, defaults to `password-blacklists`; supported values: [`password-blacklists`]
```


Role Variables
--------------

| Variable | Description | Required |
|:---------|:------------|----------|
|`keycloak_quarkus_bootstrap_admin_password`| Password of console admin account | `yes` |
|`keycloak_quarkus_admin_pass`| Deprecated, use `keycloak_quarkus_bootstrap_admin_password` instead. | |
|`keycloak_quarkus_ks_vault_pass`| The password for accessing the keystore vault SPI | `no` |
|`keycloak_quarkus_alternate_download_url`| Alternate location with optional authentication for downloading RHBK | `no` |
|`keycloak_quarkus_download_user`| Optional username for http authentication  | `no*` |
|`keycloak_quarkus_download_pass`| Optional password for http authentication | `no*` |
|`keycloak_quarkus_download_validate_certs`| Whether to validate certs for URL `keycloak_quarkus_alternate_download_url` | `no` |
|`keycloak_quarkus_jdbc_download_user`| Optional username for http authentication | `no*` |
|`keycloak_quarkus_jdbc_download_pass`| Optional password for http authentication | `no*` |
|`keycloak_quarkus_jdbc_download_validate_certs`| Whether to validate certs for URL `keycloak_quarkus_download_validate_certs` | `no` |

`*` username/password authentication credentials must be both declared or both undefined


Role custom facts
-----------------

The role uses the following [custom facts](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_vars_facts.html#adding-custom-facts) found in `/etc/ansible/facts.d/keycloak.fact` (and thus identified by the `ansible_local.keycloak.` prefix):

| Variable | Description |
|:---------|:------------|
|`general.bootstrapped` | A custom fact indicating whether this role has been used for bootstrapping keycloak on the respective host before; set to `false` (e.g., when starting off with a new, empty database) ensures that the initial admin user as defined by `keycloak_quarkus_bootstrap_admin_user[_password]` gets created |

License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
