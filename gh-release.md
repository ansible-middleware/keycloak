 v3.1.0
 ======
 
 Minor Changes
 -------------
 
 - 369 add integration tests for keycloak_authentication_v2 #374
 - AMW-578 Replace deprecated community.general.yaml callback with result #413
 - AMW-615 Inconsistent support of authentication via client credentials #400
 - AMW-622 keycloak collection spelling and grammar checking for PRs #406
 - AMW-626 keycloak_user_rolemapping raises 403 error code while listing assignable Roles if invoker lacks view-realm Role #411
 - Add use_netrc option to prevent .netrc overriding bearer token #408
 - Address issue #370, add keycloak_realm: max_secondary_auth_failures parameter #404
 - Fix #396 keycloak_user_federation.py mapper sorting now happens after unspecified mappers are merged in #414
 - Fix issue #397 #398 crash on first role assignment #405
 - In a flow definition, handle non-existing keys correctly #402
 - Normalize hostname that includes http_relative_path suffix #392
 - Replace deprecated top-level fact variables with ansible_fact #412
 - authentication_v2: Fix validation for FormActions #384
 - keycloak_group: fix subgroup lookup on Keycloak older than 25 #407
 - keycloak_user: fix attributes always reporting changed=True #399
 
