keycloak
========

Install [keycloak](https://keycloak.org/) or [Red Hat Single Sing-On](https://access.redhat.com/products/red-hat-single-sign-on) server configurations.


Requirements
------------

This role requires the `python3-netaddr` library installed on the controller node.


Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_ha_enabled`| enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_db_enabled`| enable auto configuration for database backend | `True` if keycloak_ha_enabled is True, else `False` |
|`keycloak_admin_user`| Administration console user account | `admin` |
|`keycloak_bind_address`| address for binding service ports | `0.0.0.0`
|`keycloak_host`| hostname | `localhost`
|`keycloak_http_port`| HTTP port | `8080`
|`keycloak_https_port`| TLS HTTP port | `8443`
|`keycloak_management_http_port`| management port | `9990`
|`keycloak_management_https_port`| TLS management port | `9993`
|`keycloak_java_opts`| | `-Xms1024m -Xmx20480m -XX:MaxPermSize=768m`


Role Variables
--------------

The following are a set of _required_ variables for the role:

| Variable | Description |
|:---------|:------------|
|`keycloak_admin_password`| Password for the administration console user account |


The following variables are _required_ only when keycloak_ha_enabled is True:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_modcluster_url` | URL for the modcluster reverse proxy | `localhost` |
|`keycloak_jdbc_engine` | backend database flavour when db is enabled: [ postgres, mariadb ] | `postgres` |
|`infinispan_url` | URL for the infinispan remote-cache server | `localhost:11122` |
|`infinispan_user` | username for connecting to infinispan | `supervisor` |
|`infinispan_pass` | password for connecting to infinispan | `supervisor` |


The following variables are _required_ only when keycloak_db_enabled is True and keycloak_jdbc_engine is postgres:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`postgres_jdbc_url` | URL for the postgres backend database | `jdbc:postgresql://localhost:5432/keycloak` |
|`postgres_db_user` | username for connecting to postgres | `keycloak-user` |
|`postgres_db_pass` | password for connecting to postgres | `keycloak-pass` |


The following variables are _required_ only when keycloak_db_enabled is True and keycloak_jdbc_engine is mariadb:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`mariadb_jdbc_url` | URL for the mariadb backend database | `jdbc:mariadb://localhost:3306/keycloak` |
|`mariadb_db_user` | username for connecting to mariadb | `keycloak-user` |
|`mariadb_db_pass` | password for connecting to mariadb | `keycloak-pass` |


Dependencies
------------

The roles depends on:

* the redhat_csp_download role from [middleware_automation.redhat_csp_download](https://github.com/ansible-middleware/redhat-csp-download) collection
* the wildfly_driver role from [middleware_automation.wildfly](https://github.com/ansible-middleware/wildfly) collection


Example Playbook
----------------

The following is an example playbook that makes use of the role to install keycloak

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

License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
* [Romain Pelisse](https://github.com/rpelisse)