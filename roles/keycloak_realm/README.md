keycloak_realm
==============

Create realms and clients in [keycloak](https://keycloak.org/) or [Red Hat Single Sing-On](https://access.redhat.com/products/red-hat-single-sign-on) services.


Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_admin_user`| Administration console user account | `admin` |

Role Variables
--------------

The following are a set of _required_ variables for the role:

| Variable | Description |
|:---------|:------------|
|`keycloak_admin_password`| Password for the administration console user account |


The following variables are _required_ only when keycloak_ha_enabled is True:

| Variable | Description | Default |
|:---------|:------------|:---------|



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
            name: keycloak_realm
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