keycloak
========

Install [keycloak](https://keycloak.org/) or [Red Hat Single Sing-On](https://access.redhat.com/products/red-hat-single-sign-on) server configurations.


Requirements
------------

This role requires the `python3-netaddr` library installed on the controller node.

* to install via yum/dnf: `dnf install python3-netaddr`
* or via pip: `pip install netaddr==0.8.0`


Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_ha_enabled`| Enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_db_enabled`| Enable auto configuration for database backend | `True` if `keycloak_ha_enabled` is True, else `False` |
|`keycloak_admin_user`| Administration console user account | `admin` |
|`keycloak_bind_address`| Address for binding service ports | `0.0.0.0` |
|`keycloak_host`| hostname | `localhost` |
|`keycloak_http_port`| HTTP port | `8080` |
|`keycloak_https_port`| TLS HTTP port | `8443` |
|`keycloak_management_http_port`| Management port | `9990` |
|`keycloak_management_https_port`| TLS management port | `9993` |
|`keycloak_java_opts`| Additional JVM options | `-Xms1024m -Xmx2048m` |
|`keycloak_prefer_ipv4`| Prefer IPv4 stack and addresses for port binding | `True` |
|`jvm_package`| RHEL java package runtime | `java-1.8.0-openjdk-devel` |


Role Variables
--------------

The following are a set of _required_ variables for the role:

| Variable | Description |
|:---------|:------------|
|`keycloak_admin_password`| Password for the administration console user account |


The following variables are _required_ only when `keycloak_ha_enabled` is True:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_modcluster_url` | URL for the modcluster reverse proxy | `localhost` |
|`keycloak_jdbc_engine` | backend database flavour when db is enabled: [ postgres, mariadb ] | `postgres` |
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

The following variables can be used to install Keycloak or Red Hat Single Sign-On from local path:
| Variable | Description | Default |
|:---------|:------------|:---------|
|`rhsso_zip_file_local_path` | Full local path of Red Hat Single Sign-On zip file  | `tmp/rhsso/rh-sso-7.5-server-dist.zip` |
|`keycloak_zip_file_local_path` | Full local path of Keycloak zip file  | `/tmp/keycloak/keycloak-16.1.0.zip` |

The following variable can be used to install Red Hat Single Sign-On from source via url, auth support is not added right now.
| Variable | Description | Default |
|:---------|:------------|:---------|
|`rhsso_source_download_url` | URL to download Red Hat Single Sign-On zip file from | `http://localhost:8081/nexus/rhsso/rh-sso-7.5-server-dist.zip` |

Dependencies
------------

The roles depends on:

* the redhat_csp_download role from [middleware_automation.redhat_csp_download](https://github.com/ansible-middleware/redhat-csp-download) collection if Red Hat Single Sign-on zip have to be downloaded from RHN.
* the wildfly_driver role from [middleware_automation.wildfly](https://github.com/ansible-middleware/wildfly) collection


Example Playbook
----------------

The following is an example playbook that makes use of the role to install keycloak from remote

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
            keycloak_admin_password: "changeme"
```

The following is an example playbook that makes use of the role to install keycloak from local path

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
            keycloak_admin_password: "changeme"
            keycloak_zip_file_local_path: "/tmp/keycloak/keycloak-16.1.0.zip" # This should be local path of keycloak zip file
```

The following is an example playbook that makes use of the role to install Red Hat Single Sign-On from RHN

```yaml
---
- name: Playbook for Keycloak Hosts
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
        keycloak_admin_password: "changeme"
```

The following is an example playbook that makes use of the role to install Red Hat Single Sign-On from source url

```yaml
---
- hosts: keycloak
  tasks:
    - name: Keycloak Role
      include_role:
        name: keycloak
      vars:
        keycloak_admin_password: "changeme"
        rhsso_source_download_url: "<REPLACE with - Source download url>" # This should be the full of remote source rhsso zip file
```

The following is an example playbook that makes use of the role to install Red Hat Single Sign-On from local path

```yaml
---
- hosts: keycloak
  tasks:
    - name: Keycloak Role
      include_role:
        name: keycloak
      vars:
        keycloak_admin_password: "changeme"
        rhsso_zip_file_local_path: "/tmp/rhsso/rh-sso-7.5-server-dist.zip" # This should be local path of rhsso zip file
```

License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
* [Romain Pelisse](https://github.com/rpelisse)
