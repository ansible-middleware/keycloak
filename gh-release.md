 v3.1.2
 ======
 
 Major Changes
 -------------
 
 - Port integration tests from community.general #409
 
 Minor Changes
 -------------
 
 - AMW-642 keycloak_identity_provider: add support for Do not store users from transient-users feature #430
 - AMW-644 keycloak_user_federation module always reports task as changed in check mode #433
 
 Bugfixes
 --------
 
 - Fix health check URL to use localhost with protocol and port #429
 - Issue#421 Remove default setting of JAVA_OPTS and restrict to JAVA_OPTS_KC_HEAP and JAVA_OPTS_APPEND #425
 
