# Ansible Collection - middleware_automation.keycloak

[![Build Status](https://github.com/ansible-middleware/keycloak/workflows/CI/badge.svg?branch=main)](https://github.com/ansible-middleware/keycloak/actions/workflows/ci.yml)


Collection to install and configure [Keycloak](https://www.keycloak.org/) or [Red Hat Single Sign-On](https://access.redhat.com/products/red-hat-single-sign-on). 

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.9.10**.

Plugins and modules within a collection may be tested with only specific Ansible versions. A collection may contain metadata that identifies these versions.
<!--end requires_ansible-->


## Installation

### Installing the Collection from Ansible Galaxy

Before using the collection, you need to install it with the Ansible Galaxy CLI:

    ansible-galaxy collection install middleware_automation.keycloak

You can also include it in a `requirements.yml` file and install it via `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: middleware_automation.keycloak
```

The keycloak collection also depends on the following python packages to be present on the controller host:

* netaddr

A requirement file is provided to install:

    pip install -r requirements.txt


### Included roles

* [`keycloak`](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak/README.md): role for installing the service.
* [`keycloak_realm`](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak_realm/README.md): role for configuring a realm, user federation(s), clients and users, in an installed service.


## Usage


### Install Playbook

* [`playbooks/keycloak.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak.yml) installs the upstream(Keycloak) based on the defined variables.
* [`playbooks/rhsso.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/rhsso.yml) installs Red Hat Single Sign-On(RHSSO) based on defined variables.

Both playbooks include the `keycloak` role, with different settings, as described in the following sections.

For full service configuration details, refer to the [keycloak role README](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak/README.md).


### Choosing between upstream project (Keycloak) and Red Hat Single Sign-On (RHSSO)

The general flag `keycloak_rhsso_enable` controls what to install between upstream (Keycloak, when `False`) or Red Hat Single Sign-On (when `True`).
The default value for the flag if `True` when Red Hat Network credentials are defined, `False` otherwise.


#### Install upstream (Keycloak) from keycloak releases

This is the default approach when RHN credentials are not defined. Keycloak is downloaded from keycloak builds (hosted on github.com) locally, and distributed to target nodes.


#### Install RHSSO from the Red Hat Customer Support Portal

Define the credentials as follows, and the default behaviour is to download a fresh archive of RHSSO on the controller node, then distribute to target nodes.

```yaml
rhn_username: '<customer_portal_username>'
rhn_password: '<customer_portal_password>'
# (keycloak_rhsso_enable defaults to True)
```


#### Install from controller node (local source)

Making the keycloak zip archive (or the RHSSO zip archive), available to the playbook repository root directory, and setting `keycloak_offline_install` to `True`, allows to skip
the download tasks. The local path for the archive matches the downloaded archive path, so it is also used as a cache when multiple hosts are provisioned in a cluster.

```yaml
keycloak_offline_install: True
```

And depending on `keycloak_rhsso_enable`:

* `True`: install RHSSO using file rh-sso-x.y.z-server-dist.zip
* `False`: install keycloak using file keycloak-x.y.zip


#### Install from alternate sources (like corporate Nexus, artifactory, proxy, etc)

For RHSSO:

```yaml
keycloak_rhsso_enable: True
keycloak_rhsso_download_url: "https://<internal-nexus.private.net>/<path>/<to>/rh-sso-x.y.z-server-dist.zip"
```

For keycloak:

```yaml
keycloak_rhsso_enable: False
keycloak_download_url: "https://<internal-nexus.private.net>/<path>/<to>/keycloak-x.y.zip"
```


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


## Configuration


### Config Playbook

[`playbooks/keycloak_realm.yml`](https://github.com/ansible-middleware/keycloak/blob/main/playbooks/keycloak_realm.yml) creates or updates provided realm, user federation(s), client(s), client role(s) and client user(s).


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

For full configuration details, refer to the [keycloak_realm role README](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak_realm/README.md).

## Support

Keycloak collection v1.0.0 is a Beta release and for [Technical Preview](https://access.redhat.com/support/offerings/techpreview). If you have any issues or questions related to collection, please don't hesitate to contact us on Ansible-middleware-core@redhat.com or open an issue on https://github.com/ansible-middleware/keycloak/issues

## License

Apache License v2.0 or later

See [LICENSE](LICENSE) to view the full text.

