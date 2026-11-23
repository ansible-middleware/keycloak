# Testing

## Continuous integration

The collection is tested with a [molecule](https://github.com/ansible-community/molecule) setup covering the included roles and verifying correct installation and idempotency.
In order to run the molecule tests locally with python 3.9 available, after cloning the repository:
The test scenarios are available on the source code repository each on his own subdirectory under [molecule/](https://github.com/ansible-middleware/keycloak/molecule).


## Test playbooks

Sample playbooks are provided in the `playbooks/` directory; to run the playbooks locally (requires a rhel system with python 3.9+, ansible, and systemd) the steps are as follows:

```
# setup environment as in developing
# create inventory for localhost
cat << EOF > inventory
[keycloak]
localhost ansible_connection=local
EOF
# run the playbook
ansible-playbook -i inventory playbooks/keycloak.yml
```
