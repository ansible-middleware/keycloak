
# Copyright (c) Ansible project
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import annotations

DOCUMENTATION = r"""
module: keycloak_client_scope_type

short_description: Set the type of a client scope in a realm or client using the Keycloak API

# Originally added in community.general 6.6.0
version_added: "3.0.0"

description:
  - This module allows you to set the type (optional, default) of client scopes using the Keycloak REST API. It requires access
    to the REST API using OpenID Connect; the user connecting and the client being used must have the requisite access rights.
    In a default Keycloak installation, admin-cli and an admin user would work, as would a separate client definition with
    the scope tailored to your needs and a user having the expected roles.
attributes:
  check_mode:
    support: full
  diff_mode:
    support: full
  action_group:
    # Originally added in community.general 10.2.0
    version_added: "3.0.0"

options:
  realm:
    type: str
    description:
      - The Keycloak realm.
    default: 'master'

  client_id:
    description:
      - The O(client_id) of the client. If not set the client scope types are set as a default for the realm.
    aliases:
      - clientId
    type: str

  default_client_scopes:
    description:
      - Client scopes that should be of type default.
    type: list
    elements: str

  optional_client_scopes:
    description:
      - Client scopes that should be of type optional.
    type: list
    elements: str

extends_documentation_fragment:
  - middleware_automation.keycloak.keycloak
  - middleware_automation.keycloak.actiongroup_keycloak
  - middleware_automation.keycloak.attributes

author:
  - Simon Pahl (@simonpahl)
"""

EXAMPLES = r"""
- name: Set default client scopes on realm level
  middleware_automation.keycloak.keycloak_client_scope_type:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
    realm: "MyCustomRealm"
    default_client_scopes: ['profile', 'roles']
  delegate_to: localhost


- name: Set default and optional client scopes on client level with token auth
  middleware_automation.keycloak.keycloak_client_scope_type:
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com
    token: TOKEN
    realm: "MyCustomRealm"
    client_id: "MyCustomClient"
    default_client_scopes: ['profile', 'roles']
    optional_client_scopes: ['phone']
  delegate_to: localhost
"""

RETURN = r"""
msg:
  description: Message as to what action was taken.
  returned: always
  type: str
  sample: ""
proposed:
  description: Representation of proposed client-scope types mapping.
  returned: always
  type: dict
  sample:
    {
      "default_client_scopes": [
        "profile",
        "role"
      ],
      "optional_client_scopes": []
    }
existing:
  description:
    - Representation of client scopes before module execution.
  returned: always
  type: dict
  sample:
    {
      "default_client_scopes": [
        "profile",
        "role"
      ],
      "optional_client_scopes": [
        "phone"
      ]
    }
end_state:
  description:
    - Representation of client scopes after module execution.
    - The sample is truncated.
  returned: on success
  type: dict
  sample:
    {
      "default_client_scopes": [
        "profile",
        "role"
      ],
      "optional_client_scopes": []
    }
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.middleware_automation.keycloak.plugins.module_utils.identity.keycloak.keycloak import (
    KeycloakAPI,
    KeycloakError,
    get_token,
    keycloak_argument_spec,
)


def keycloak_client_scope_type_module():
    """
    Returns an AnsibleModule definition.

    :return: argument_spec dict
    """
    argument_spec = keycloak_argument_spec()

    meta_args = dict(
        realm=dict(default="master"),
        client_id=dict(type="str", aliases=["clientId"]),
        default_client_scopes=dict(type="list", elements="str"),
        optional_client_scopes=dict(type="list", elements="str"),
    )

    argument_spec.update(meta_args)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=(
            [
                ["token", "auth_realm", "auth_username", "auth_password", "auth_client_id", "auth_client_secret"],
                ["default_client_scopes", "optional_client_scopes"],
            ]
        ),
        required_together=([["auth_username", "auth_password"]]),
        required_by={"refresh_token": "auth_realm"},
        mutually_exclusive=[["token", "auth_realm"], ["token", "auth_username"], ["token", "auth_password"]],
    )

    return module


def client_scopes_to_add(existing, proposed):
    to_add = []
    existing_client_scope_ids = extract_field(existing, "id")
    for client_scope in proposed:
        if client_scope["id"] not in existing_client_scope_ids:
            to_add.append(client_scope)
    return to_add


def client_scopes_to_delete(existing, proposed):
    to_delete = []
    proposed_client_scope_ids = extract_field(proposed, "id")
    for client_scope in existing:
        if client_scope["id"] not in proposed_client_scope_ids:
            to_delete.append(client_scope)
    return to_delete


def extract_field(dictionary, field="name"):
    return [cs[field] for cs in dictionary]


def normalize_scopes(scopes):
    scopes_copy = scopes.copy()
    if isinstance(scopes_copy.get("default_client_scopes"), list):
        scopes_copy["default_client_scopes"] = sorted(scopes_copy["default_client_scopes"])
    if isinstance(scopes_copy.get("optional_client_scopes"), list):
        scopes_copy["optional_client_scopes"] = sorted(scopes_copy["optional_client_scopes"])
    return scopes_copy


def main():
    """
    Module keycloak_client_scope_type

    :return:
    """

    module = keycloak_client_scope_type_module()

    # Obtain access token, initialize API
    try:
        connection_header = get_token(module.params)
    except KeycloakError as e:
        module.fail_json(msg=str(e))

    kc = KeycloakAPI(module, connection_header)

    realm = module.params.get("realm")
    client_id = module.params.get("client_id")
    default_client_scopes = module.params.get("default_client_scopes")
    optional_client_scopes = module.params.get("optional_client_scopes")

    result = dict(changed=False, msg="", proposed={}, existing={}, end_state={})

    all_client_scopes = kc.get_client_scopes(realm)
    default_client_scopes_real = []
    optional_client_scopes_real = []

    for client_scope in all_client_scopes:
        if default_client_scopes is not None and client_scope["name"] in default_client_scopes:
            default_client_scopes_real.append(client_scope)
        if optional_client_scopes is not None and client_scope["name"] in optional_client_scopes:
            optional_client_scopes_real.append(client_scope)

    if default_client_scopes is not None and len(default_client_scopes_real) != len(default_client_scopes):
        module.fail_json(msg="At least one of the default_client_scopes does not exist!")

    if optional_client_scopes is not None and len(optional_client_scopes_real) != len(optional_client_scopes):
        module.fail_json(msg="At least one of the optional_client_scopes does not exist!")

    result["proposed"].update(
        {
            "default_client_scopes": "no-change" if default_client_scopes is None else default_client_scopes,
            "optional_client_scopes": "no-change" if optional_client_scopes is None else optional_client_scopes,
        }
    )

    default_client_scopes_existing = kc.get_default_client_scopes(realm, client_id)
    optional_client_scopes_existing = kc.get_optional_client_scopes(realm, client_id)

    result["existing"].update(
        {
            "default_client_scopes": extract_field(default_client_scopes_existing),
            "optional_client_scopes": extract_field(optional_client_scopes_existing),
        }
    )

    if module._diff:
        result["diff"] = dict(before=normalize_scopes(result["existing"]), after=normalize_scopes(result["proposed"]))

    default_client_scopes_add = client_scopes_to_add(default_client_scopees_existing, defaultclient_scopees_real)
    optional_client_scopes_add = client_scopes_to_add(optional_client_scopes_existing, optional_client_scopes_real)

    default_client_scopes_delete = client_scopes_to_delete(default_client_scopes_existing, default_client_scopes_real)
    optional_client_scopes_delete = client_scopes_to_delete(optional_client_scopes_existing, optional_client_scopes_real)

    result["changed"] = any(
        len(x) > 0
        for x in [
            default_client_scopes_add,
            optional_client_scopes_add,
            default_client_scopes_delete,
            optional_client_scopes_delete,
        ]
    )

    if module.check_mode:
        module.exit_json(**result)

    # first delete so client_scopes can change type
    for client_scope in default_client_scopes_delete:
        kc.delete_default_client_scope(client_scope["id"], realm, client_id)
    for client_scope in optional_client_scopes_delete:
        kc.delete_optional_client_scope(client_scope["id"], realm, client_id)

    for client_scope in default_client_scopes_add:
        kc.add_default_client_scope(client_scope["id"], realm, client_id)
    for client_scope in optional_client_scopes_add:
        kc.add_optional_client_scope(client_scope["id"], realm, client_id)

    result["end_state"].update(
        {
            "default_client_scopes": extract_field(kc.get_default_client_scopes(realm, client_id)),
            "optional_client_scopes": extract_field(kc.get_optional_client_scopes(realm, client_id)),
        }
    )

    module.exit_json(**result)


if __name__ == "__main__":
    main()
