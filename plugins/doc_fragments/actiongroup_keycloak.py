# -*- coding: utf-8 -*-

# Copyright (c) 2017, Eike Frost <ei@kefro.st>
# GNU General Public License v3.0+ (see LICENSES/GPL-3.0-or-later.txt or https://www.gnu.org/licenses/gpl-3.0.txt)
# SPDX-License-Identifier: GPL-3.0-or-later

from __future__ import (absolute_import, division, print_function)
from __future__ import annotations
__metaclass__ = type


class ModuleDocFragment(object):

    DOCUMENTATION = r'''
options: {}
attributes:
  action_group:
    description: Use C(group/middleware_automation.keycloak.keycloak) in C(module_defaults) to set defaults for this module.
    support: full
    membership:
      - middleware_automation.keycloak.keycloak
'''
