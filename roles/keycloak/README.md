keycloak
========

Install [keycloak](https://keycloak.org/) or [Red Hat Single Sing-On](https://access.redhat.com/products/red-hat-single-sign-on) server configurations.


Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_ha_enabled`| enable auto configuration for database backend, clustering and remote caches on infinispan | `False` |
|`keycloak_admin_user`| Administration console user account | `admin` |


Role Variables
--------------

The following are a set of required variables for the role:

| Variable | Description |
|:---------|:------------|
|`keycloak_admin_password`| Password for the administration console user account |

The following variables are required when keycloak_ha_enabled is True:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_modcluster_url` | URL for the modcluster reverse proxy | `localhost` |
|`postgres_jdbc_url` | URL for the postgres backend database | `jdbc:postgresql://localhost:5432/keycloak` |
|`postgres_db_user` | username for connecting to postgres | `keycloak-user` |
|`postgres_db_pass` | password for connecting to postgres | `keycloak-pass` |
|`infinispan_url` | URL for the infinispan remote-cache server | `localhost:11122` |
|`infinispan_user` | username for connecting to infinispan | `supervisor` |
|`infinispan_pass` | password for connecting to infinispan | `supervisor` |


Dependencies
------------

The roles depends on:

* the redhat_csp_download role of [middleware_automation.redhat_csp_download](https://github.com/ansible-middleware/redhat-csp-download) collection
* the jcliff role of [middleware_automation.jcliff](https://github.com/ansible-middleware/ansible_collections_jcliff) collection


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