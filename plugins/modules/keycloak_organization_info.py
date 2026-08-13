
# Copyright (c) 2025, Chris Brown
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
from __future__ import annotations
__metaclass__ = type

DOCUMENTATION = r"""
module: keycloak_organization_info

short_description: Retrieve organization info in Keycloak

version_added: "3.1.0"

description:
  - This module retrieves information on organizations from Keycloak.
  - Organizations are available in Keycloak 26 and later. The realm must have organizations enabled
    before this module can be used.
attributes:
  action_group:
    version_added: "3.1.0"

options:
  realm:
    description:
      - The name of the realm.
    required: true
    type: str
  name:
    description:
      - Name of the organization to search for.
      - If not provided, all organizations in the realm are returned.
    type: str
  exact:
    description:
      - Whether the search should be an exact match.
      - Only relevant when O(name) is provided.
    type: bool
    default: true

extends_documentation_fragment:
  - middleware_automation.keycloak.keycloak
  - middleware_automation.keycloak.actiongroup_keycloak
  - middleware_automation.keycloak.attributes
  - middleware_automation.keycloak.attributes.info_module

author:
  - Chris Brown (@chribro)
"""

EXAMPLES = r"""
- name: Retrieve a specific organization by name
  middleware_automation.keycloak.keycloak_organization_info:
    auth_keycloak_url: https://auth.example.com
    auth_username: admin
    auth_password: password
    auth_realm: master
    realm: MyRealm
    name: my-org

- name: List all organizations in a realm
  middleware_automation.keycloak.keycloak_organization_info:
    auth_keycloak_url: https://auth.example.com
    auth_username: admin
    auth_password: password
    auth_realm: master
    realm: MyRealm

- name: Search organizations by partial name
  middleware_automation.keycloak.keycloak_organization_info:
    auth_keycloak_url: https://auth.example.com
    auth_username: admin
    auth_password: password
    auth_realm: master
    realm: MyRealm
    name: acme
    exact: false
"""

RETURN = r"""
organizations:
  description: JSON representation of organizations.
  returned: always
  type: list
  elements: dict
"""

from urllib.parse import quote

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.middleware_automation.keycloak.plugins.module_utils.identity.keycloak.keycloak import (
    KeycloakAPI,
    KeycloakError,
    get_token,
    keycloak_argument_spec,
)


def main():
    argument_spec = keycloak_argument_spec()

    meta_args = dict(
        name=dict(type="str"),
        realm=dict(type="str", required=True),
        exact=dict(type="bool", default=True),
    )

    argument_spec.update(meta_args)

    module = AnsibleModule(argument_spec=argument_spec, supports_check_mode=True)

    result = dict(changed=False, organizations=[])

    try:
        connection_header = get_token(module.params)
    except KeycloakError as e:
        module.fail_json(msg=str(e))

    kc = KeycloakAPI(module, connection_header)

    realm = module.params.get("realm")
    name = module.params.get("name")
    exact = module.params.get("exact")

    filters = []
    if name:
        filters.append(f"search={quote(name, safe='')}")
        if exact:
            filters.append("exact=true")

    filter_str = "&".join(filters) if filters else None

    result["organizations"] = kc.get_organizations(search_filter=filter_str, realm=realm)

    module.exit_json(**result)


if __name__ == "__main__":
    main()
