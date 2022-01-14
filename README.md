# Ansible Collection - keycloak

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

### Install Playbook

`playbooks/keycloak.yml` installs the upstream(Keycloak) based on the defined variables.
`playbooks/rhsso.yml` installs Red Hat Single Sign-On(RHSSO) based on defined variables.

### Choosing between upstream(Keycloak) project and Red Hat Single Sign-On(RHSSO)

The roles supports installing upstream(Keycloak) or Red Hat Single Sign-On in the following ways

#### Install upstream(Keycloak) from remote source

This is default approach, there is one required variable

```
keycloak_admin_password: "<changeme>"
```

#### Install upstream(Keycloak) from local source when the following variable is defined

```
keycloak_admin_password: "<changeme>"
zip_file_local_path: <keycloak zip file on Ansible control node local path>
```

#### Install RHSSO from the Red Hat Customer Support Portal, when the following variables are defined

```
keycloak_admin_password: "<changeme>"
rhn_username: '<customer_portal_username>'
rhn_password: '<customer_portal_password>'
rhsso_rhn_id: '<sso_product_id>'
```

where `sso_product_id` is the ID for the specific Red Hat Single Sign-On version, ie. _101971_ will install version _7.5_)

#### Install RHSSO from remote sources like Nexus etc, when the following variables are defined

```
keycloak_admin_password: "<changeme>"
keycloak_rhsso_enable: True
rhsso_source_download_url: '<url to download RHSSO zip file>'
```

#### Install RHSSO from local source when the following variable is defined

```
keycloak_admin_password: "<changeme>"
keycloak_rhsso_enable: True
zip_file_local_path: <rhsso zip file on Ansible control node local path>
```

### Install role

* [`keycloak`](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak/README.md): role for installing the service. _Requires: python3-netaddr_

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

`playbooks/keycloak-realm.yml` creates provided realm, client(s), client role(s) and client user(s) if they don't exist.

### Config role

* [`keycloak_realm`](https://github.com/ansible-middleware/keycloak/blob/main/roles/keycloak_realm/README.md): role for configuring a realm, with clients and users, in an installed service.

### Example configuration command

Execute the following command from the source root directory

```
ansible-playbook -i <ansible_hosts> -e @rhn-creds.yml playbooks/keycloak.yml -e keycloak_admin_password=<changeme> -e keycloak_realm=test
```

- `keycloak_admin_password` password for the administration console user account.
- `keycloak_realm` name of the realm to be created/used.
- `ansible_hosts` is the inventory, below is an example inventory for deploying to localhost

  ```
  [keycloak]
  localhost ansible_connection=local
  ```

## License

Apache License v2.0 or later

See [LICENCE](LICENSE) to view the full text.

