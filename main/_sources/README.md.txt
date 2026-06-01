# Ansible Collection - middleware_automation.keycloak

<!--start build_status -->
[![Build Status](https://github.com/ansible-middleware/keycloak/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/ansible-middleware/keycloak/actions/workflows/ci.yml)

> **_NOTE:_ If you are Red Hat customer, install `redhat.rhbk` (for Red Hat Build of Keycloak) or `redhat.sso` (for Red Hat Single Sign-On) from [Automation Hub](https://console.redhat.com/ansible/ansible-dashboard) as the certified version of this collection.**

<!--end build_status -->
<!--start description -->
Collection to install and configure [Keycloak](https://www.keycloak.org/) or [Red Hat Single Sign-On](https://access.redhat.com/products/red-hat-single-sign-on) / [Red Hat Build of Keycloak](https://access.redhat.com/products/red-hat-build-of-keycloak).
<!--end description -->
<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.16.0**.

Plugins and modules within a collection may be tested with only specific Ansible versions. A collection may contain metadata that identifies these versions.
<!--end requires_ansible-->


## Installation

<!--start galaxy_download -->
### Installing the Collection from Ansible Galaxy

Before using the collection, you need to install it with the Ansible Galaxy CLI:

    ansible-galaxy collection install middleware_automation.keycloak

<!--end galaxy_download -->

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: middleware_automation.keycloak
```

The keycloak collection also depends on the following python packages to be present on the controller host:

* netaddr
* lxml

A requirement file is provided to install:

    pip install -r requirements.txt

<!--start roles_paths -->
### Included roles

* `keycloak_quarkus`: role for installing keycloak (>= 19.0.0, quarkus based).
* `keycloak_realm`: role for configuring a realm, user federation(s), clients and users, in an installed service.
* `keycloak`: role for installing legacy keycloak (<= 19.0, wildfly based).

<!--end roles_paths -->

### Included modules

All Keycloak administration modules from `community.general` are provided in this collection for Keycloak 17+ (Quarkus). Use `auth_keycloak_url` without the legacy `/auth` context path (for example `http://localhost:8080`). Set `keycloak_context` to `/auth` only when automating WildFly-based Keycloak with the `keycloak` role.

* `keycloak_authentication`: manage authentication flows and executions using Keycloak Admin REST API.
* `keycloak_authentication_flow`: manage custom authentication flows and flow executions.
* `keycloak_authentication_required_actions`: manage required actions available in realm authentication.
* `keycloak_authentication_v2`: manage authentication flows with newer Keycloak API handling.
* `keycloak_authz_authorization_scope`: manage authorization scopes for a client resource server.
* `keycloak_authz_custom_policy`: manage custom authorization policies for a client resource server.
* `keycloak_authz_permission`: manage authorization permissions for a client resource server.
* `keycloak_authz_permission_info`: retrieve authorization permission information for a client resource server.
* `keycloak_client`: manage Keycloak clients (create/update/delete).
* `keycloak_client_rolemapping`: manage client role mappings for users and groups.
* `keycloak_client_rolescope`: manage client role scope mappings.
* `keycloak_client_scope`: manage client scopes and protocol mappers (replaces `community.general.keycloak_clientscope`).
* `keycloak_clientscope_type`: manage default and optional client scope assignments.
* `keycloak_clientsecret_info`: retrieve client secret information.
* `keycloak_clientsecret_regenerate`: regenerate a client secret.
* `keycloak_clienttemplate`: manage legacy client templates.
* `keycloak_component`: manage realm components.
* `keycloak_component_info`: retrieve realm component information.
* `keycloak_group`: manage realm groups and subgroups.
* `keycloak_identity_provider`: manage identity provider instances and configuration.
* `keycloak_realm`: manage realms (create/update/delete).
* `keycloak_realm_info`: retrieve realm information.
* `keycloak_realm_key`: manage realm key providers.
* `keycloak_realm_keys_metadata_info`: retrieve realm keys metadata.
* `keycloak_realm_localization`: manage realm localization texts.
* `keycloak_realm_rolemapping`: manage realm role mappings for users and groups.
* `keycloak_role`: manage realm and client roles.
* `keycloak_user`: manage users (create/update/delete).
* `keycloak_user_execute_actions_email`: trigger execute-actions emails for users.
* `keycloak_user_federation`: manage user federation providers (for example LDAP/AD).
* `keycloak_user_rolemapping`: manage user role mappings.
* `keycloak_userprofile`: manage user profile configuration.

## Usage

The collection provides roles to install Keycloak and modules to manage realms, clients, users, and related settings via the [Keycloak Admin REST API](https://www.keycloak.org/docs-api/latest/rest-api/index.html).

For Quarkus-based Keycloak (17+), set `auth_keycloak_url` to the server root URL without the legacy `/auth` path, for example `http://localhost:8080`. When using the legacy `keycloak` role with WildFly-based Keycloak, set `keycloak_context` to `/auth` in the `keycloak_realm` role.

### Install Keycloak

* [`playbooks/keycloak_quarkus.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_quarkus.yml) installs Keycloak >= 17 using the `keycloak_quarkus` role.
* [`playbooks/keycloak.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak.yml) installs legacy Keycloak (<= 19) using the `keycloak` role.

For full service configuration details, refer to the [keycloak_quarkus role README](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak_quarkus/README.md) or the [keycloak role README](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak/README.md).

#### Install from controller node (offline)

Making the keycloak zip archive available to the playbook working directory, and setting `keycloak_offline_install` to `true`, allows to skip
the download tasks. The local path for the archive does match the downloaded archive path, so that it is also used as a cache when multiple hosts are provisioned in a cluster.

```yaml
keycloak_offline_install: true
```


<!--start rhn_credentials -->
<!--end rhn_credentials -->


#### Install from alternate sources (like corporate Nexus, artifactory, proxy, etc)

It is possible to perform downloads from alternate sources, using the `keycloak_download_url` variable; make sure the final downloaded filename matches with the source filename (ie. keycloak-legacy-x.y.zip or rh-sso-x.y.z-server-dist.zip).


#### Example installation command

Execute the following command from the source root directory:

```bash
ansible-playbook -i <ansible_hosts> playbooks/keycloak_quarkus.yml -e keycloak_quarkus_bootstrap_admin_password=<changeme>
```

- `keycloak_quarkus_bootstrap_admin_password` password for the administration console user account.
- `ansible_hosts` is the inventory, below is an example inventory for deploying to localhost

  ```
  [keycloak]
  localhost ansible_connection=local
  ```

Note: when deploying clustered configurations, all hosts belonging to the cluster must be present in `ansible_play_batch`; ie. they must be targeted by the same ansible-playbook execution.

### Configure with roles

<!--start rhbk_realm_playbook -->
* [`playbooks/keycloak_realm.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_realm.yml) creates or updates provided realm, user federation(s), client(s), client role(s) and client user(s).
<!--end rhbk_realm_playbook -->
* [`playbooks/keycloak_realm_client.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_realm_client.yml) creates a realm with clients, roles and users using the `keycloak_realm` role.
* [`playbooks/keycloak_federation.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_federation.yml) configures user federation providers.

#### Example configuration command

Execute the following command from the source root directory:

```bash
ansible-playbook -i <ansible_hosts> playbooks/keycloak_realm.yml -e keycloak_admin_password=<changeme> -e keycloak_realm=test
```

- `keycloak_admin_password` password for the administration console user account.
- `keycloak_realm` name of the realm to be created/used.
- `ansible_hosts` is the inventory, below is an example inventory for deploying to localhost

  ```
  [keycloak]
  localhost ansible_connection=local
  ```
<!--start rhbk_realm_readme -->
For full configuration details, refer to the [keycloak_realm role README](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak_realm/README.md).
<!--end rhbk_realm_readme -->

### Configure with modules

Module playbooks target an already running Keycloak instance. All modules use the `middleware_automation.keycloak` collection namespace.

* [`playbooks/keycloak_client_scope.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_client_scope.yml) creates a client scope with protocol mappers using the `keycloak_client_scope` module.
* [`playbooks/keycloak_authentication_flow.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_authentication_flow.yml) creates a custom authentication flow with execution steps using the `keycloak_authentication_flow` module.

Example task using shared authentication defaults:

```yaml
- hosts: localhost
  module_defaults:
    group/middleware_automation.keycloak.keycloak:
      auth_keycloak_url: http://localhost:8080
      auth_realm: master
      auth_username: admin
      auth_password: "{{ keycloak_admin_password }}"
  tasks:
    - name: Create a user in a realm
      middleware_automation.keycloak.keycloak_user:
        realm: TestRealm
        username: testuser
        first_name: Test
        last_name: User
        email: testuser@example.com
        enabled: true
        state: present
```

When migrating from `community.general`, replace the collection prefix in playbooks (for example `community.general.keycloak_user` becomes `middleware_automation.keycloak.keycloak_user`) and use `keycloak_client_scope` instead of `keycloak_clientscope`.


## Support

<!--start support -->

For bug reports and feature requests, use [GitHub Issues](https://github.com/ansible-middleware/keycloak/issues).

<!--end support -->


## Release and Upgrade Notes

For details on changes between versions, please see the [CHANGELOG](https://github.com/ansible-middleware/keycloak/blob/main/CHANGELOG.rst) for this collection.


## License

Apache License v2.0 or later
<!--start license -->
See [LICENSE](LICENSE) to view the full text.
<!--end license -->
