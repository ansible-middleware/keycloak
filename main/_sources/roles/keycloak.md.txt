keycloak
========

Install [keycloak](https://keycloak.org/) or [Red Hat Single Sign-On](https://access.redhat.com/products/red-hat-single-sign-on) server configurations.


Requirements
------------

This role requires the `python3-netaddr` library installed on the controller node.

* to install via yum/dnf: `dnf install python3-netaddr`
* or via pip: `pip install netaddr==0.8.0`
* or via the collection: `pip install -r requirements.txt`


Dependencies
------------

The roles depends on:

* the `redhat_csp_download` role from [middleware_automation.redhat_csp_download](https://github.com/ansible-middleware/redhat-csp-download) collection if Red Hat Single Sign-on zip have to be downloaded from RHN.
* the `wildfly_driver` role from [middleware_automation.wildfly](https://github.com/ansible-middleware/wildfly) collection


Versions
--------

| RH-SSO VERSION | Release Date      | Keycloak Version | EAP Version | Notes           |
|:---------------|:------------------|:-----------------|:------------|:----------------|
|`7.5.0 GA`      |September 20, 2021 |`15.0.2`          | `7.4.0`     |[Release Notes](https://access.redhat.com/documentation/en-us/red_hat_single_sign-on/7.5/html/release_notes/index)|


Patching
--------

When variable `keycloak_rhsso_apply_patches` is `True` (default: `False`), the role will automatically apply the latest cumulative patch for the selected base version.

| RH-SSO VERSION | Release Date      | RH-SSO LATEST CP | Notes           |
|:---------------|:------------------|:-----------------|:----------------|
|`7.5.0 GA`      |January 20, 2022   |`7.5.1 GA`        |[Release Notes](https://access.redhat.com/articles/6646321)|



Role Defaults
-------------

* Service configuration

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_ha_enabled`| Enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_db_enabled`| Enable auto configuration for database backend | `True` if `keycloak_ha_enabled` is True, else `False` |
|`keycloak_admin_user`| Administration console user account | `admin` |
|`keycloak_bind_address`| Address for binding service ports | `0.0.0.0` |
|`keycloak_host`| hostname | `localhost` |
|`keycloak_http_port`| HTTP port | `8080` |
|`keycloak_https_port`| TLS HTTP port | `8443` |
|`keycloak_ajp_port`| AJP port | `8009` |
|`keycloak_jgroups_port`| jgroups cluster tcp port | `7600` |
|`keycloak_management_http_port`| Management port | `9990` |
|`keycloak_management_https_port`| TLS management port | `9993` |
|`keycloak_java_opts`| Additional JVM options | `-Xms1024m -Xmx2048m` |
|`keycloak_prefer_ipv4`| Prefer IPv4 stack and addresses for port binding | `True` |
|`keycloak_config_standalone_xml`| filename for configuration | `keycloak.xml` |
|`keycloak_service_user`| posix account username | `keycloak` |
|`keycloak_service_group`| posix account group | `keycloak` |
|`keycloak_service_pidfile`| pid file path for service | `/run/keycloak.pid` |
|`keycloak_jvm_package`| RHEL java package runtime | `java-1.8.0-openjdk-devel` |


* Install options

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_rhsso_enable`| Enable Red Hat Single Sign-on installation | `False` |
|`keycloak_offline_install` | perform an offline install | `False`|
|`keycloak_download_url`| Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/<version>/<archive>`| 
|`keycloak_rhsso_download_url`| Download URL for RHSSO | `https://access.redhat.com/jbossnetwork/restricted/softwareDownload.html?softwareId=<productID>`|
|`keycloak_version`| keycloak.org package version | `15.0.2` |
|`keycloak_rhsso_version`| RHSSO version | `7.5.0` |
|`keycloak_rhsso_apply_patches`| Install RHSSO more recent cumulative patch | `False` |
|`keycloak_dest`| Installation root path | `/opt/keycloak` |
|`keycloak_download_url` | Download URL for keycloak | `https://github.com/keycloak/keycloak/releases/download/{{ keycloak_version }}/{{ keycloak_archive }}` |
|`keycloak_rhn_url` | Base download URI for customer portal | `https://access.redhat.com/jbossnetwork/restricted/softwareDownload.html?softwareId=` |
|`keycloak_configure_firewalld` | Ensure firewalld is running and configure keycloak ports | `False` |


* Miscellaneous configuration

| Variable | Description | Default |
|:---------|:------------|:--------|
|`keycloak_archive` | keycloak install archive filename | `keycloak-{{ keycloak_version }}.zip` |
|`keycloak_download_url_9x` | Download URL for keycloak (deprecated) | `https://downloads.jboss.org/keycloak/{{ keycloak_version }}/{{ keycloak_archive }}` |
|`keycloak_installdir` | Installation path | `{{ keycloak_dest }}/keycloak-{{ keycloak_version }}` |
|`keycloak_rhsso_archive` | Red Hat SSO install archive filename | `rh-sso-{{ keycloak_rhsso_version }}-server-dist.zip` |
|`keycloak_rhsso_installdir`| Installation path for Red Hat SSO | `{{ keycloak_dest }}/rh-sso-{{ keycloak_rhsso_version | regex_replace('^([0-9])\.([0-9]*).*', '\1.\2') }}` |
|`keycloak_rhsso_download_url`| Full download URI for Red Hat SSO | `{{ keycloak_rhn_url }}{{ rhsso_rhn_id }}` |
|`keycloak_jboss_home` | Installation work directory | `{{ keycloak_rhsso_installdir if keycloak_rhsso_enable else keycloak_installdir }}` |
|`keycloak_config_dir` | Path for configuration | `{{ keycloak_jboss_home }}/standalone/configuration` |
|`keycloak_config_path_to_standalone_xml` | Custom path for configuration | `{{ keycloak_jboss_home }}/standalone/configuration/{{ keycloak_config_standalone_xml }}` |
|`keycloak_auth_realm` | Name for rest authentication realm | `master` |
|`keycloak_auth_client` | Authentication client for configuration REST calls | `admin-cli` |
|`keycloak_force_install` | Remove pre-existing versions of service | `False` |
|`keycloak_url` | URL for configuration rest calls | `http://{{ keycloak_host }}:{{ keycloak_http_port }}` |
|`keycloak_management_url` | URL for management console rest calls | `http://{{ keycloak_host }}:{{ keycloak_management_http_port }}` |
|`rhsso_rhn_id` | Customer Portal product ID for Red Hat SSO | `{{ rhsso_rhn_ids[keycloak_rhsso_version].id }}` |


Role Variables
--------------

The following are a set of _required_ variables for the role:

| Variable | Description |
|:---------|:------------|
|`keycloak_admin_password`| Password for the administration console user account (minimum 12 characters) |
|`keycloak_frontend_url` | frontend URL for keycloak endpoint | `http://localhost:8080/auth` |


The following variables are _required_ only when `keycloak_ha_enabled` is True:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_modcluster_url` | URL for the modcluster reverse proxy | `localhost` |
|`keycloak_jdbc_engine` | backend database engine when db is enabled: [ postgres, mariadb ] | `postgres` |
|`infinispan_url` | URL for the infinispan remote-cache server | `localhost:11122` |
|`infinispan_user` | username for connecting to infinispan | `supervisor` |
|`infinispan_pass` | password for connecting to infinispan | `supervisor` |
|`infinispan_sasl_mechanism`| Authentication type | `SCRAM-SHA-512` |
|`infinispan_use_ssl`| Enable hotrod TLS communication | `False` |
|`infinispan_trust_store_path`| Path to truststore with infinispan server certificate | `/etc/pki/java/cacerts` |
|`infinispan_trust_store_password`| Password for opening truststore | `changeit` |


The following variables are _required_ only when `keycloak_db_enabled` is True:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_jdbc_url` | URL for the postgres backend database | `jdbc:postgresql://localhost:5432/keycloak` |
|`keycloak_jdbc_driver_version`| Version for the JDBC driver to download | `9.4.1212` |
|`keycloak_db_user` | username for connecting to postgres | `keycloak-user` |
|`keycloak_db_pass` | password for connecting to postgres | `keycloak-pass` |


Example Playbooks
-----------------

_NOTE_: use ansible vaults or other security systems for storing credentials.


* The following is an example playbook that makes use of the role to install keycloak from remote:

```yaml
---
- hosts: ...
      vars:
        keycloak_admin_password: "remembertochangeme"
      collections:
        - middleware_automation.keycloak
      roles:
        - middleware_automation.keycloak.keycloak
```

* The following is an example playbook that makes use of the role to install Red Hat Single Sign-On from RHN:

```yaml
---
- name: Playbook for RHSSO
  hosts: keycloak
  collections:
    - middleware_automation.redhat_csp_download
  roles:
    - redhat_csp_download
  tasks:
    - name: Keycloak Role
      include_role:
        name: keycloak
      vars:
        keycloak_admin_password: "remembertochangeme"
        keycloak_rhsso_enable: True
        rhn_username: '<customer portal username>'
        rhn_password: '<customer portal password>'
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
            keycloak_offline_install: True
            # This should be the filename of keycloak archive on Ansible node: keycloak-16.1.0.zip
```


* This playbook installs Red Hat Single Sign-On from an alternate url:

```yaml
---
- hosts: keycloak
  collections:
    - middleware_automation.keycloak
  tasks:
    - name: Keycloak Role
      include_role:
        name: keycloak
      vars:
        keycloak_admin_password: "remembertochangeme"
        keycloak_rhsso_enable: True
        keycloak_rhsso_download_url: "<REPLACE with download url>"
        # This should be the full of remote source rhsso zip file and can contain basic authentication credentials
```


* The following is an example playbook that makes use of the role to install Red Hat Single Sign-On offline from the controller node, and apply latest cumulative patch:

```yaml
---
- hosts: keycloak
  collections:
    - middleware_automation.keycloak
  tasks:
    - name: Keycloak Role
      include_role:
        name: keycloak
      vars:
        keycloak_admin_password: "remembertochangeme"
        keycloak_rhsso_enable: True
        keycloak_offline_install: True
        keycloak_rhsso_apply_patches: True
        # This should be the filename of rhsso zip file on Ansible node: rh-sso-7.5-server-dist.zip
```

License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
* [Romain Pelisse](https://github.com/rpelisse)
* [Pavan Kumar Motaparthi](https://github.com/motaparthipavankumar)
