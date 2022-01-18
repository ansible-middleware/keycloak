keycloak_realm
==============

Create realms and clients in [keycloak](https://keycloak.org/) or [Red Hat Single Sing-On](https://access.redhat.com/products/red-hat-single-sign-on) services.


Role Defaults
-------------

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_admin_user` | Administration console user account | `admin` |
|`keycloak_host` | hostname | `localhost` |
|`keycloak_http_port` | HTTP port | `8080` |
|`keycloak_https_port` | TLS HTTP port | `8443` |
|`keycloak_auth_realm` | Name of the main authentication realm | `master` |
|`keycloak_rhsso_enable` | Define service is an upstream(Keycloak) or RHSSO | `master` |



Role Variables
--------------

The following are a set of _required_ variables for the role:

| Variable | Description |
|:---------|:------------|
|`keycloak_admin_password`| Password for the administration console user account |
|`keycloak_realm` | Name of the realm to be created |


The following variables are available for creating clients:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_clients` | List of _client_ declarations for the realm | `[]` |
|`keycloak_client_default_roles` | List of default role name for clients | `[]` |
|`keycloak_client_users` | List of user/role mappings for a client | `[]` |

The following variable are available for creating user federation:

| Variable | Description | Default |
|:---------|:------------|:---------|
|`keycloak_user_federation` | List of _keycloak_user_federation_ for the realm | `[]` |


Variable formats
----------------

* `keycloak_user_federation`, a list of:

```yaml
    - realm:  <name of the realm in which user federation should be configured, required>
      name: <name of the user federation provider, required>
      provider_id: <Type of the user federation provider, required>
      provider_type: < Provider Type, default is set to org.keycloak.storage.UserStorageProvider>
      config: <Dictionary of supported configuration values, required>
      mappers: <List of supported configuration values, required>
```

Refer to [docs](https://docs.ansible.com/ansible/latest/collections/community/general/keycloak_user_federation_module.html) for information on supported variables.

* `keycloak_clients`, a list of:

```yaml
    - name: <name of the client>
      roles: <keycloak_client_default_roles>
      realm: <name of the realm that contains the client>
      public_client: <true for public, false for confidential>
      web_origins: <list of allowed we origins for the client>
      users: <keycloak_client_users>
```

* `keycloak_client_users`, a list of:

```yaml
    - username: <username, required>
      password: <password, required>
      firstName: <firstName, optional>
      lastName: <lastName, optional>
      email: <email, optional>
      client_roles: <list of client user/role mappings>
```

* Client user/role mappings, a list of:

```yaml
    - client: <name of the client>
      role: <name of the role>
      realm: <name of the realm>
```

For a comprehensive example, refer to the [playbook](playbooks/keycloak.yml).

Example Playbook
----------------

The following is an example playbook that makes use of the role to create a realm in keycloak.

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
            keycloak_realm: TestRealm
            keycloak_clients: [...]
```


License
-------

Apache License 2.0


Author Information
------------------

* [Guido Grazioli](https://github.com/guidograzioli)
* [Romain Pelisse](https://github.com/rpelisse)