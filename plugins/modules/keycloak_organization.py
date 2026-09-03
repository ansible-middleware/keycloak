
# Copyright (c) 2025, Chris Brown
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
from __future__ import annotations
__metaclass__ = type

DOCUMENTATION = r"""
module: keycloak_organization

short_description: Allows administration of Keycloak organizations using Keycloak API

version_added: "3.1.0"

description:
  - This module allows you to add, remove or modify Keycloak organizations using the Keycloak REST API.
    It requires access to the REST API using OpenID Connect; the user connecting and the client being
    used must have the requisite access rights. In a default Keycloak installation, admin-cli and an
    admin user would work, as would a separate client definition with the scope tailored to your needs
    and a user having the expected roles.
  - The names of module options are snake_cased versions of the camelCase ones found in the Keycloak
    API and its documentation at U(https://www.keycloak.org/docs-api/latest/rest-api/index.html).
  - Attributes are multi-valued in the Keycloak API. All attributes are lists of individual values and
    are returned that way by this module. You may pass single values for attributes when calling the
    module, and this is translated into a list suitable for the API.
  - Organizations are available in Keycloak 26 and later. The realm must have organizations enabled
    (C(organizations_enabled=true) in the M(middleware_automation.keycloak.keycloak_realm) module)
    before this module can be used.
  - When updating an organization, where possible provide the organization ID to the module. This
    removes a lookup to the API to translate the name into the organization ID.
attributes:
  check_mode:
    support: full
  diff_mode:
    support: full
  action_group:
    version_added: "3.1.0"

options:
  state:
    description:
      - State of the organization.
      - On V(present), the organization is created if it does not yet exist, or updated with the
        parameters you provide.
      - On V(absent), the organization is removed if it exists.
    default: 'present'
    type: str
    choices:
      - present
      - absent

  realm:
    type: str
    description:
      - The Keycloak realm under which this organization resides.
    default: 'master'

  id:
    type: str
    description:
      - The unique identifier for this organization.
      - This parameter is not required for updating or deleting an organization but providing it
        reduces the number of API calls required.

  name:
    type: str
    description:
      - Name of the organization.
      - This parameter is required when creating a new organization.

  alias:
    type: str
    description:
      - URL-friendly alias for the organization.
      - If not provided during creation, defaults to the organization name if URL-safe.
      - The alias is immutable once set and cannot be changed on update.

  enabled:
    type: bool
    description:
      - Whether the organization is enabled.
      - Disabled organizations block member authentication.

  description:
    type: str
    description:
      - Description of the organization.

  domains:
    type: list
    elements: dict
    description:
      - List of internet domains associated with the organization.
      - A domain name can only belong to one organization within a realm.
    suboptions:
      name:
        type: str
        required: true
        description:
          - The domain name (e.g. V(example.com)).
      verified:
        type: bool
        default: false
        description:
          - Whether the domain has been verified.

  attributes:
    type: dict
    description:
      - A dict of key/value pairs to set as custom attributes for the organization.
      - Values may be single values (for example a string) or a list of strings.

extends_documentation_fragment:
  - middleware_automation.keycloak.keycloak
  - middleware_automation.keycloak.actiongroup_keycloak
  - middleware_automation.keycloak.attributes

author:
  - Chris Brown (@chribro)
"""

EXAMPLES = r"""
- name: Create a Keycloak organization
  middleware_automation.keycloak.keycloak_organization:
    name: my-org
    description: My Organization
    enabled: true
    realm: MyRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Create a Keycloak organization with domains
  middleware_automation.keycloak.keycloak_organization:
    name: acme-corp
    description: Acme Corporation
    enabled: true
    domains:
      - name: acme.com
      - name: acme.org
        verified: true
    realm: MyRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Update a Keycloak organization
  middleware_automation.keycloak.keycloak_organization:
    name: my-org
    description: Updated description
    realm: MyRealm
    state: present
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost

- name: Delete a Keycloak organization
  middleware_automation.keycloak.keycloak_organization:
    name: my-org
    state: absent
    realm: MyRealm
    auth_client_id: admin-cli
    auth_keycloak_url: https://auth.example.com
    auth_realm: master
    auth_username: USERNAME
    auth_password: PASSWORD
  delegate_to: localhost
"""

RETURN = r"""
msg:
  description: Message as to what action was taken.
  returned: always
  type: str

end_state:
  description: Representation of the organization after module execution.
  returned: on success
  type: complex
  contains:
    id:
      description: GUID that identifies the organization.
      type: str
      returned: always
      sample: 23f38145-3195-462c-97e7-97041ccea73e
    name:
      description: Name of the organization.
      type: str
      returned: always
      sample: my-org
    alias:
      description: URL-friendly alias of the organization.
      type: str
      returned: always
      sample: my-org
    enabled:
      description: Whether the organization is enabled.
      type: bool
      returned: always
      sample: true
    description:
      description: Description of the organization.
      type: str
      returned: always
      sample: My Organization
    domains:
      description: Domains associated with the organization.
      type: list
      returned: always
      sample: [{"name": "example.com", "verified": false}]
    attributes:
      description: Attributes applied to this organization.
      type: dict
      returned: always
      sample:
        attr1: ["val1", "val2"]
"""

from ansible.module_utils.basic import AnsibleModule

from ansible_collections.middleware_automation.keycloak.plugins.module_utils.identity.keycloak.keycloak import (
    KeycloakAPI,
    KeycloakError,
    camel,
    get_token,
    keycloak_argument_spec,
)


def normalise_org(org):
    """Normalise an organization representation for comparison.
    Sorts domains by name to ensure order-independent comparison.
    """
    if org and "domains" in org and org["domains"]:
        org["domains"] = sorted(org["domains"], key=lambda d: d.get("name", ""))
    return org


def main():
    argument_spec = keycloak_argument_spec()

    meta_args = dict(
        state=dict(default="present", choices=["present", "absent"]),
        realm=dict(default="master"),
        id=dict(type="str"),
        name=dict(type="str"),
        alias=dict(type="str"),
        enabled=dict(type="bool"),
        description=dict(type="str"),
        domains=dict(
            type="list",
            elements="dict",
            options=dict(
                name=dict(type="str", required=True),
                verified=dict(type="bool", default=False),
            ),
        ),
        attributes=dict(type="dict"),
    )

    argument_spec.update(meta_args)

    module = AnsibleModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        required_one_of=(
            [
                ["id", "name"],
                ["token", "auth_realm", "auth_username", "auth_password", "auth_client_id", "auth_client_secret"],
            ]
        ),
        required_together=([["auth_username", "auth_password"]]),
        required_by={"refresh_token": "auth_realm"},
    )

    result = dict(changed=False, msg="", diff={}, end_state={})

    try:
        connection_header = get_token(module.params)
    except KeycloakError as e:
        module.fail_json(msg=str(e))

    kc = KeycloakAPI(module, connection_header)

    realm = module.params.get("realm")
    state = module.params.get("state")
    oid = module.params.get("id")
    name = module.params.get("name")
    attributes = module.params.get("attributes")

    if attributes is not None:
        for key, val in module.params["attributes"].items():
            module.params["attributes"][key] = [val] if not isinstance(val, list) else val

    # Parameters that map to the organization representation (excluding module-level params)
    org_params = [
        x
        for x in module.params
        if x not in list(keycloak_argument_spec().keys()) + ["state", "realm"]
        and module.params.get(x) is not None
    ]

    if oid is None:
        before_org = kc.get_organization_by_name(name, realm=realm)
    else:
        before_org = kc.get_organization_by_id(oid, realm=realm)

    if before_org is None:
        before_org = {}

    normalise_org(before_org)

    changeset = {}
    for param in org_params:
        new_param_value = module.params.get(param)
        if param == "alias" and before_org:
            if new_param_value != before_org.get("alias"):
                module.warn(
                    f"Organization alias is immutable and cannot be changed from '{before_org.get('alias')}' "
                    f"to '{new_param_value}'. The alias parameter will be ignored for this update."
                )
            continue
        old_value = before_org.get(camel(param))
        if new_param_value != old_value:
            changeset[camel(param)] = new_param_value

    desired_org = before_org.copy()
    desired_org.update(changeset)

    normalise_org(desired_org)

    if not before_org:
        if state == "absent":
            if module._diff:
                result["diff"] = dict(before="", after="")
            result["changed"] = False
            result["end_state"] = {}
            result["msg"] = "Organization does not exist; doing nothing."
            module.exit_json(**result)

        result["changed"] = True

        if name is None:
            module.fail_json(msg="name must be specified when creating a new organization")

        if module._diff:
            result["diff"] = dict(before="", after=desired_org)

        if module.check_mode:
            module.exit_json(**result)

        kc.create_organization(desired_org, realm=realm)

        after_org = kc.get_organization_by_name(name, realm=realm)

        result["end_state"] = normalise_org(after_org) if after_org else {}
        result["msg"] = f"Organization {name} has been created with ID {after_org['id']}"
        module.exit_json(**result)

    else:
        if state == "present":
            if desired_org == before_org:
                result["changed"] = False
                result["end_state"] = desired_org
                result["msg"] = f"No changes required to organization {before_org['name']}."
                module.exit_json(**result)

            result["changed"] = True

            if module._diff:
                result["diff"] = dict(before=before_org, after=desired_org)

            if module.check_mode:
                module.exit_json(**result)

            kc.update_organization(desired_org, realm=realm)

            after_org = kc.get_organization_by_id(desired_org["id"], realm=realm)

            result["end_state"] = normalise_org(after_org) if after_org else {}
            result["msg"] = f"Organization {desired_org['id']} has been updated"
            module.exit_json(**result)

        else:
            result["changed"] = True

            if module._diff:
                result["diff"] = dict(before=before_org, after="")

            if module.check_mode:
                module.exit_json(**result)

            oid = before_org["id"]
            kc.delete_organization(org_id=oid, realm=realm)

            result["end_state"] = {}
            result["msg"] = f"Organization {before_org['name']} has been deleted"

    module.exit_json(**result)


if __name__ == "__main__":
    main()
