## Developing

### Build and install locally

Clone the repository, checkout the tag you want to build, or pick the main branch for the development version; then:

    ansible-galaxy collection build .
    ansible-galaxy collection install middleware_automation-keycloak-*.tar.gz


### Development environment

Make sure your development machine has avilable:

* python 3.11+
* virtualenv
* docker (or podman)

In order to run setup the development environment and run the molecule tests locally, after cloning the repository:

```
# create new virtualenv using python 3
virtualenv $PATH_TO_DEV_VIRTUALENV
# activate the virtual env
source $PATH_TO_DEV_VIRTUALENV/bin/activate
# install ansible and tools onto the virtualenv
pip install yamllint 'molecule>=6.0' 'molecule-plugins[docker]' 'ansible-core>=2.16' ansible-lint
# install collection dependencies
ansible-galaxy collection install -r requirements.yml
# install python dependencies
pip install -r requirements.txt molecule/requirements.txt
# execute the tests (replace --all with -s subdirectory to run a single test)
molecule test --all
```

## Contributor's Guidelines

- All YAML files named with `.yml` extension
- Use spaces around jinja variables. `{{ var }}` over `{{var}}`
- Variables that are internal to the role should be lowercase and start with the role name
- Keep roles self contained - Roles should avoid including tasks from other roles when possible
- Plays should do nothing more than include a list of roles, except where `pre_tasks` and `post_tasks` are required, when possible
- Separators - Use valid names, ie. underscores (e.g. `my_role` `my_playbook`) not dashes (`my-role`)
- Paths - When defining paths, do not include trailing slashes (e.g. `my_path: /foo` not `my_path: /foo/`); when concatenating paths, follow the same convention (e.g. `{{ my_path }}/bar` not `{{ my_path }}bar`)
- Indentation - Use 2 spaces for each indent
- `vars/` vs `defaults/` - internal or interpolated variables that don't need to change or be overridden by user go in `vars/`, those that a user would likely override, go under `defaults/` directory
- All role arguments have a specification in `meta/argument_specs.yml`
- All playbooks/roles should be focused on compatibility with Ansible Automation Platform
