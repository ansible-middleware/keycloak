#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Contributors to the middleware_automation.keycloak collection
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: keycloak_authentication_flow

short_description: Allows administration of Keycloak authentication flows via Keycloak API

description:
    - This module allows you to add, remove or modify Keycloak authentication flows via the Keycloak REST API.
      It requires access to the REST API via OpenID Connect; the user connecting and the client being
      used must have the requisite access rights. In a default Keycloak installation, admin-cli
      and an admin user would work, as would a separate client definition with the scope tailored
      to your needs and a user having the expected roles.

    - This module supports creating new top-level authentication flows, copying existing flows,
      and adding execution steps to a flow.

attributes:
    check_mode:
        support: full
    diff_mode:
        support: full

options:
    state:
        description:
            - State of the authentication flow.
            - On V(present), the flow will be created if it does not yet exist.
            - On V(absent), the flow will be removed if it exists.
        default: 'present'
        type: str
        choices:
            - present
            - absent

    alias:
        type: str
        required: true
        description:
            - Alias (name) of the authentication flow.

    description:
        type: str
        description:
            - Description of the authentication flow.
        default: ''

    realm:
        type: str
        description:
            - The Keycloak realm under which this authentication flow resides.
        default: 'master'

    provider_id:
        type: str
        description:
            - The provider ID for the flow.
        default: 'basic-flow'
        aliases:
            - providerId

    copy_from:
        type: str
        description:
            - If set, the new flow is created as a copy of the flow with this alias.
            - Cannot be used together with O(executions).
        aliases:
            - copyFrom

    executions:
        type: list
        elements: dict
        description:
            - A list of executions (authenticator steps) to add to the flow.
            - Each execution is a dict with keys C(provider_id) (or C(providerId)) and C(requirement).
            - Executions are only added when the flow is first created.
        default: []
        suboptions:
            provider_id:
                type: str
                required: true
                description:
                    - The authenticator provider ID (e.g. V(auth-cookie), V(auth-password), V(auth-otp-form)).
                aliases:
                    - providerId
            requirement:
                type: str
                required: true
                description:
                    - The requirement level for this execution.
                choices:
                    - REQUIRED
                    - ALTERNATIVE
                    - DISABLED
                    - CONDITIONAL

extends_documentation_fragment:
    - middleware_automation.keycloak.keycloak
    - middleware_automation.keycloak.attributes

author:
    - Paulo Menon (@paulomenon)
'''

EXAMPLES = '''
- name: Create an authentication flow with executions
  middleware_automation.keycloak.keycloak_authentication_flow:
    auth_keycloak_url: http://localhost:8080
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: TestRealm
    alias: my-browser-flow
    description: "Custom browser flow"
    provider_id: basic-flow
    executions:
      - provider_id: auth-cookie
        requirement: ALTERNATIVE
      - provider_id: auth-password
        requirement: REQUIRED
      - provider_id: auth-otp-form
        requirement: ALTERNATIVE
    state: present
  delegate_to: localhost

- name: Create an authentication flow by copying an existing one
  middleware_automation.keycloak.keycloak_authentication_flow:
    auth_keycloak_url: http://localhost:8080
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: TestRealm
    alias: my-copy-of-browser
    copy_from: browser
    state: present
  delegate_to: localhost

- name: Create a flow using token authentication
  middleware_automation.keycloak.keycloak_authentication_flow:
    auth_keycloak_url: http://localhost:8080
    token: MY_TOKEN
    realm: TestRealm
    alias: my-flow
    state: present
  delegate_to: localhost

- name: Delete an authentication flow
  middleware_automation.keycloak.keycloak_authentication_flow:
    auth_keycloak_url: http://localhost:8080
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: TestRealm
    alias: my-browser-flow
    state: absent
  delegate_to: localhost
'''

RETURN = '''
msg:
    description: Message as to what action was taken.
    returned: always
    type: str
    sample: "Authentication flow my-browser-flow has been created"

end_state:
    description: Representation of the authentication flow after module execution.
    returned: on success
    type: dict
    sample: {
        "id": "uuid-here",
        "alias": "my-browser-flow",
        "providerId": "basic-flow",
        "topLevel": true,
        "builtIn": false
    }
'''

from ansible_collections.middleware_automation.keycloak.plugins.module_utils.identity.keycloak.keycloak import KeycloakAPI, \
    keycloak_argument_spec, get_token, KeycloakError
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = keycloak_argument_spec()

    execution_spec = dict(
        provider_id=dict(type='str', required=True, aliases=['providerId']),
        requirement=dict(type='str', required=True, choices=['REQUIRED', 'ALTERNATIVE', 'DISABLED', 'CONDITIONAL']),
    )

    meta_args = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        alias=dict(type='str', required=True),
        description=dict(type='str', default=''),
        realm=dict(type='str', default='master'),
        provider_id=dict(type='str', default='basic-flow', aliases=['providerId']),
        copy_from=dict(type='str', aliases=['copyFrom']),
        executions=dict(type='list', default=[], options=execution_spec, elements='dict'),
    )

    argument_spec.update(meta_args)

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True,
                           required_one_of=([['token', 'auth_realm', 'auth_username', 'auth_password']]),
                           required_together=([['auth_realm', 'auth_username', 'auth_password']]),
                           mutually_exclusive=[['copy_from', 'executions']])

    result = dict(changed=False, msg='', diff={}, end_state={})

    try:
        connection_header = get_token(module.params)
    except KeycloakError as e:
        module.fail_json(msg=str(e))

    kc = KeycloakAPI(module, connection_header)

    realm = module.params.get('realm')
    alias = module.params.get('alias')
    state = module.params.get('state')
    description = module.params.get('description')
    provider_id = module.params.get('provider_id')
    copy_from = module.params.get('copy_from')
    executions = module.params.get('executions')

    before_flow = kc.get_authentication_flow_by_alias(alias, realm=realm)
    flow_exists = bool(before_flow)

    if state == 'absent':
        if flow_exists:
            result['changed'] = True
            if module._diff:
                result['diff'] = dict(before=before_flow, after='')
            if module.check_mode:
                module.exit_json(**result)
            kc.delete_authentication_flow_by_id(before_flow['id'], realm=realm)
            result['msg'] = "Authentication flow {alias} has been deleted".format(alias=alias)
        else:
            result['msg'] = "Authentication flow {alias} does not exist, doing nothing".format(alias=alias)
        result['end_state'] = {}
        module.exit_json(**result)

    if flow_exists:
        result['changed'] = False
        result['end_state'] = before_flow
        result['msg'] = "Authentication flow {alias} already exists".format(alias=alias)
        module.exit_json(**result)

    result['changed'] = True

    flow_config = {
        'alias': alias,
        'description': description,
        'providerId': provider_id,
    }

    if module._diff:
        result['diff'] = dict(before='', after=flow_config)

    if module.check_mode:
        module.exit_json(**result)

    if copy_from:
        flow_config['copyFrom'] = copy_from
        after_flow = kc.copy_auth_flow(flow_config, realm=realm)
        result['msg'] = "Authentication flow {alias} has been created (copied from {src})".format(alias=alias, src=copy_from)
    else:
        after_flow = kc.create_empty_auth_flow(flow_config, realm=realm)

        if executions:
            for execution in executions:
                exec_rep = {
                    'providerId': execution['provider_id'],
                    'requirement': execution['requirement'],
                }
                kc.create_execution(exec_rep, alias, realm=realm)

        result['msg'] = "Authentication flow {alias} has been created".format(alias=alias)

    after_flow = kc.get_authentication_flow_by_alias(alias, realm=realm)
    result['end_state'] = after_flow
    module.exit_json(**result)


if __name__ == '__main__':
    main()
