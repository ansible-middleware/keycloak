# Testing

## Continuous integration

The collection is tested with a [molecule](https://github.com/ansible-community/molecule) setup covering the included roles and verifying correct installation and idempotency.
In order to run the molecule tests locally with python 3.9 available, after cloning the repository:

```
pip install yamllint 'molecule[docker]~=3.5.2' ansible-core flake8 ansible-lint voluptuous
molecule test --all
```


## Integration testing

Demo repositories which depend on the collection, and aggregate functionality with other middleware_automation collections, are automatically rebuilt
at every collection release to ensure non-breaking changes and consistent behaviour.

The repository are:

 - [Flange demo](https://github.com/ansible-middleware/flange-demo)
   A deployment of Wildfly cluster integrated with keycloak and infinispan.
 - [CrossDC keycloak demo](https://github.com/ansible-middleware/cross-dc-rhsso-demo)
   A clustered multi-regional installation of keycloak with infinispan remote caches.


## Test playbooks

Sample playbooks are provided in the `playbooks/` directory; to run the playbooks locally (requires a rhel system with python 3.9+, ansible, and systemd) the steps are as follows:

```
# setup environment
pip install ansible-core
# clone the repository
git clone https://github.com/ansible-middleware/keycloak
cd keycloak
# install collection dependencies
ansible-galaxy collection install -r requirements.yml
# install collection python deps
pip install -r requirements.txt
# create inventory for localhost
cat << EOF > inventory
[keycloak]
localhost ansible_connection=local
EOF
# run the playbook
ansible-playbook -i inventory playbooks/keycloak.yml
```

