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

## Usage


### Install Playbook
<!--start rhbk_playbook -->
* [`playbooks/keycloak_quarkus.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_quarkus.yml) installs keycloak >= 17 based on the defined variables (using most defaults).
* [`playbooks/keycloak.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak.yml) installs keycloak legacy based on the defined variables (using most defaults).

Both playbooks include the `keycloak` role, with different settings, as described in the following sections.

For full service configuration details, refer to the [keycloak role README](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak/README.md).
<!--end rhbk_playbook -->

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


### Example installation command

Execute the following command from the source root directory

```
ansible-playbook -i <ansible_hosts> -e @rhn-creds.yml playbooks/keycloak.yml -e keycloak_admin_password=<changeme>
```

- `keycloak_admin_password` Password for the administration console user account.
- `ansible_hosts` is the inventory, below is an example inventory for deploying to localhost

  ```
  [keycloak]
  localhost ansible_connection=local
  ```

Note: when deploying clustered configurations, all hosts belonging to the cluster must be present in `ansible_play_batch`; ie. they must be targeted by the same ansible-playbook execution.


## Configuration


### Config Playbook
<!--start rhbk_realm_playbook -->
[`playbooks/keycloak_realm.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_realm.yml) creates or updates provided realm, user federation(s), client(s), client role(s) and client user(s).
<!--end rhbk_realm_playbook -->

### Example configuration command

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

<!--start support -->
<!--end support -->


## License

Apache License v2.0 or later
<!--start license -->
See [LICENSE](LICENSE) to view the full text.
<!--end license -->
