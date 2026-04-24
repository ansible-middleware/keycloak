#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright (c) 2024, Contributors to the middleware_automation.keycloak collection
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import absolute_import, division, print_function
__metaclass__ = type

DOCUMENTATION = '''
---
module: keycloak_client_scope

short_description: Allows administration of Keycloak client scopes via Keycloak API

description:
    - This module allows you to add, remove or modify Keycloak client scopes via the Keycloak REST API.
      It requires access to the REST API via OpenID Connect; the user connecting and the client being
      used must have the requisite access rights. In a default Keycloak installation, admin-cli
      and an admin user would work, as would a separate client definition with the scope tailored
      to your needs and a user having the expected roles.

    - This module also supports managing protocol mappers within a client scope.

attributes:
    check_mode:
        support: full
    diff_mode:
        support: full

options:
    state:
        description:
            - State of the client scope.
            - On V(present), the client scope will be created if it does not yet exist, or updated with the parameters you provide.
            - On V(absent), the client scope will be removed if it exists.
        default: 'present'
        type: str
        choices:
            - present
            - absent

    name:
        type: str
        required: true
        description:
            - Name of the client scope.

    description:
        type: str
        default: ''
        description:
            - Description of the client scope.

    realm:
        type: str
        description:
            - The Keycloak realm under which this client scope resides.
        default: 'master'

    protocol:
        type: str
        description:
            - The protocol associated with the client scope.
        default: 'openid-connect'
        choices:
            - openid-connect
            - saml

    attributes:
        type: dict
        description:
            - A dict of key/value pairs to set as attributes for the client scope.

    protocol_mappers:
        type: list
        elements: dict
        description:
            - A list of protocol mappers to associate with the client scope.
            - Each mapper is a dict with the keys C(name), C(protocol), C(protocolMapper), and C(config).
        default: []
        suboptions:
            name:
                type: str
                required: true
                description:
                    - Name of the protocol mapper.
            protocol:
                type: str
                description:
                    - Protocol for the mapper.
                default: 'openid-connect'
            protocolMapper:
                type: str
                required: true
                description:
                    - The mapper type (e.g. V(oidc-usermodel-attribute-mapper), V(oidc-audience-mapper)).
                aliases:
                    - protocol_mapper_type
            config:
                type: dict
                required: true
                description:
                    - Configuration for the protocol mapper.

extends_documentation_fragment:
    - middleware_automation.keycloak.keycloak
    - middleware_automation.keycloak.attributes

author:
    - Paulo Menon (@paulomenon)
'''

EXAMPLES = '''
- name: Create a client scope with protocol mappers
  middleware_automation.keycloak.keycloak_client_scope:
    auth_keycloak_url: http://localhost:8080
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: TestRealm
    name: my-client-scope
    description: "A custom client scope"
    protocol: openid-connect
    protocol_mappers:
      - name: email
        protocol: openid-connect
        protocolMapper: oidc-usermodel-attribute-mapper
        config:
          user.attribute: email
          claim.name: email
          jsonType.label: String
          id.token.claim: "true"
          access.token.claim: "true"
          userinfo.token.claim: "true"
    state: present
  delegate_to: localhost

- name: Create a client scope using token authentication
  middleware_automation.keycloak.keycloak_client_scope:
    auth_keycloak_url: http://localhost:8080
    token: MY_TOKEN
    realm: TestRealm
    name: my-scope
    state: present
  delegate_to: localhost

- name: Delete a client scope
  middleware_automation.keycloak.keycloak_client_scope:
    auth_keycloak_url: http://localhost:8080
    auth_realm: master
    auth_username: admin
    auth_password: password
    realm: TestRealm
    name: my-client-scope
    state: absent
  delegate_to: localhost
'''

RETURN = '''
msg:
    description: Message as to what action was taken.
    returned: always
    type: str
    sample: "Client scope my-scope has been created"

end_state:
    description: Representation of the client scope after module execution.
    returned: on success
    type: dict
    sample: {
        "id": "uuid-here",
        "name": "my-scope",
        "protocol": "openid-connect",
        "description": "A custom scope"
    }
'''

from ansible_collections.middleware_automation.keycloak.plugins.module_utils.identity.keycloak.keycloak import KeycloakAPI, \
    keycloak_argument_spec, get_token, KeycloakError
from ansible.module_utils.basic import AnsibleModule


def main():
    argument_spec = keycloak_argument_spec()

    mapper_spec = dict(
        name=dict(type='str', required=True),
        protocol=dict(type='str', default='openid-connect'),
        protocolMapper=dict(type='str', required=True, aliases=['protocol_mapper_type']),
        config=dict(type='dict', required=True),
    )

    meta_args = dict(
        state=dict(type='str', default='present', choices=['present', 'absent']),
        name=dict(type='str', required=True),
        description=dict(type='str', default=''),
        realm=dict(type='str', default='master'),
        protocol=dict(type='str', default='openid-connect', choices=['openid-connect', 'saml']),
        attributes=dict(type='dict'),
        protocol_mappers=dict(type='list', default=[], options=mapper_spec, elements='dict'),
    )

    argument_spec.update(meta_args)

    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True,
                           required_one_of=([['token', 'auth_realm', 'auth_username', 'auth_password']]),
                           required_together=([['auth_realm', 'auth_username', 'auth_password']]))

    result = dict(changed=False, msg='', diff={}, end_state={})

    try:
        connection_header = get_token(module.params)
    except KeycloakError as e:
        module.fail_json(msg=str(e))

    kc = KeycloakAPI(module, connection_header)

    realm = module.params.get('realm')
    name = module.params.get('name')
    state = module.params.get('state')
    protocol = module.params.get('protocol')
    description = module.params.get('description')
    attributes = module.params.get('attributes')
    protocol_mappers = module.params.get('protocol_mappers')

    before_scope = kc.get_clientscope_by_name(name, realm=realm)

    if state == 'absent':
        if before_scope:
            result['changed'] = True
            if module._diff:
                result['diff'] = dict(before=before_scope, after='')
            if module.check_mode:
                module.exit_json(**result)
            kc.delete_clientscope(cid=before_scope['id'], realm=realm)
            result['msg'] = "Client scope {name} has been deleted".format(name=name)
        else:
            result['msg'] = "Client scope {name} does not exist, doing nothing".format(name=name)
        result['end_state'] = {}
        module.exit_json(**result)

    scope_rep = {
        'name': name,
        'protocol': protocol,
        'description': description,
    }
    if attributes:
        scope_rep['attributes'] = attributes

    if not before_scope:
        result['changed'] = True
        if module._diff:
            result['diff'] = dict(before='', after=scope_rep)
        if module.check_mode:
            module.exit_json(**result)

        kc.create_clientscope(scope_rep, realm=realm)
        after_scope = kc.get_clientscope_by_name(name, realm=realm)

        if protocol_mappers:
            for mapper in protocol_mappers:
                mapper_rep = {
                    'name': mapper['name'],
                    'protocol': mapper.get('protocol', protocol),
                    'protocolMapper': mapper['protocolMapper'],
                    'config': mapper['config'],
                }
                kc.create_clientscope_protocolmapper(after_scope['id'], mapper_rep, realm=realm)
            after_scope = kc.get_clientscope_by_name(name, realm=realm)

        result['end_state'] = after_scope
        result['msg'] = "Client scope {name} has been created".format(name=name)
        module.exit_json(**result)

    else:
        changed = False
        for key in ('protocol', 'description'):
            if scope_rep.get(key) and scope_rep[key] != before_scope.get(key):
                changed = True
                break

        if attributes and attributes != before_scope.get('attributes', {}):
            changed = True

        if changed:
            result['changed'] = True
            scope_rep['id'] = before_scope['id']
            if module._diff:
                result['diff'] = dict(before=before_scope, after=scope_rep)
            if module.check_mode:
                module.exit_json(**result)
            kc.update_clientscope(scope_rep, realm=realm)

        if protocol_mappers:
            existing_mappers = kc.get_clientscope_protocolmappers(before_scope['id'], realm=realm)
            existing_mapper_names = {m['name'] for m in existing_mappers}

            for mapper in protocol_mappers:
                if mapper['name'] not in existing_mapper_names:
                    result['changed'] = True
                    if not module.check_mode:
                        mapper_rep = {
                            'name': mapper['name'],
                            'protocol': mapper.get('protocol', protocol),
                            'protocolMapper': mapper['protocolMapper'],
                            'config': mapper['config'],
                        }
                        kc.create_clientscope_protocolmapper(before_scope['id'], mapper_rep, realm=realm)

        after_scope = kc.get_clientscope_by_name(name, realm=realm)
        result['end_state'] = after_scope

        if result['changed']:
            result['msg'] = "Client scope {name} has been updated".format(name=name)
        else:
            result['msg'] = "No changes required to client scope {name}".format(name=name)
        module.exit_json(**result)


if __name__ == '__main__':
    main()
