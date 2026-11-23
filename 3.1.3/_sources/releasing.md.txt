# Collection Versioning Strategy

Each supported collection maintained by Ansible follows Semantic Versioning 2.0.0 (https://semver.org/), for example:
Given a version number MAJOR.MINOR.PATCH, the following is incremented:

MAJOR version: when making incompatible API changes (see Feature Release scenarios below for examples)

MINOR version: when adding features or functionality in a backwards compatible manner, or updating testing matrix and/or metadata (deprecation)

PATCH version: when adding backwards compatible bug fixes or security fixes (strict).

Additional labels for pre-release and build metadata are available as extensions to the MAJOR.MINOR.PATCH format.

The first version of a generally available supported collection on Ansible Automation Hub shall be version 1.0.0. NOTE: By default, all newly created collections may begin with a smaller default version of 0.1.0, and therefore a version of 1.0.0 should be explicitly stated by the collection maintainer.

## New content is added to an existing collection

Assuming the current release is 1.0.0, and a new module is ready to be added to the collection, the minor version would be incremented to 1.1.0. The change in the MINOR version indicates an additive change was made while maintaining backward compatibility for existing content within the collection.


## New feature to existing plugin or role within a collection (backwards compatible)

Assuming the current release is 1.0.0, and new features for an existing module are ready for release . We would increment the MINOR version to 1.1.0. The change in the MINOR version indicates an additive change was made while maintaining backward compatibility for existing content within the collection.


## Bug fix or security fix to existing content within a collection

Assuming the current release is 1.0.0 and a bug is fixed prior to the next minor release, the PATCH version would be incremented to 1.0.1. The patch indicates only a bug was fixed within a current version. The PATCH release does not contain new content, nor was functionality removed. Bug fixes may be included in a MINOR or MAJOR feature release if the timing allows, eliminating the need for a PATCH dedicated to the fix.


## Breaking change to any content within a collection

Assuming the current release is 1.0.0, and a breaking change (API or module) is introduced for a user or developer. The MAJOR version would be incremented to 2.0.0.

Examples of breaking changes within a collection may include but are not limited to:

 - Argspec changes for a module that require either inventory structure or playbook changes.
 - A change in the shape of either the inbound or returned payload of a filter plugin.
 - Changes to a connection plugin that require additional inventory parameters or ansible.cfg entries.
 - New functionality added to a module that changes the outcome of that module as released in previous versions.
 - The removal of plugins from a collection.


## Content removed from a collection

Deleting a module or API is a breaking change. Please see the 'Breaking change' section for how to version this.


## A typographical error was fixed in the documentation for a collection

A correction to the README would be considered a bug fix and the PATCH incremented. See 'Bug fix' above.


## Documentation added/removed/modified within a collection

Only the PATCH version should be increased for a release that contains changes limited to revised documentation.


## Release automation

New releases are triggered by annotated git tags named after semantic versioning. The automation publishes the built artifacts to ansible-galaxy and github releases page.
