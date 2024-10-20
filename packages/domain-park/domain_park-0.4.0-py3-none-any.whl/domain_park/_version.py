"""Version information for this package."""

### IMPORTS
### ============================================================================
## Standard Library
import datetime  # pylint: disable=unused-import

## Installed

## Application

### CONSTANTS
### ============================================================================
## Version Information - DO NOT EDIT
## -----------------------------------------------------------------------------
# These variables will be set during the build process. Do not attempt to edit.
PACKAGE_VERSION = "0.4.0"
BUILD_VERSION = "0.4.0"
BUILD_GIT_HASH = "f7ecfcd940a7633b70194f5652afbc6a9ce2e042"
BUILD_GIT_HASH_SHORT = "f7ecfcd"
BUILD_GIT_BRANCH = "master"
BUILD_TIMESTAMP = 1729412972
BUILD_DATETIME = datetime.datetime.utcfromtimestamp(1729412972)

VERSION_VARS = vars()  # Don't have f-strings until py36

## Version Information Templates
## -----------------------------------------------------------------------------
# You can customise the templates used for version information here.
VERSION_INFO_TEMPLATE_SHORT = "{BUILD_VERSION}"
VERSION_INFO_TEMPLATE = "{PACKAGE_VERSION} ({BUILD_VERSION})"
VERSION_INFO_TEMPLATE_LONG = (
    "{PACKAGE_VERSION} ({BUILD_VERSION}) ({BUILD_GIT_BRANCH}@{BUILD_GIT_HASH_SHORT})"
)
VERSION_INFO_TEMPLATE_FULL = (
    "{PACKAGE_VERSION} ({BUILD_VERSION})\n"
    "{BUILD_GIT_BRANCH}@{BUILD_GIT_HASH}\n"
    "Built: {BUILD_DATETIME}"
)


### FUNCTIONS
### ============================================================================
def get_version_info_short() -> str:  # pylint: disable=missing-function-docstring
    return VERSION_INFO_TEMPLATE_SHORT.format(**VERSION_VARS)


def get_version_info() -> str:  # pylint: disable=missing-function-docstring
    return VERSION_INFO_TEMPLATE.format(**VERSION_VARS)


def get_version_info_long() -> str:  # pylint: disable=missing-function-docstring
    return VERSION_INFO_TEMPLATE_LONG.format(**VERSION_VARS)


def get_version_info_full() -> str:  # pylint: disable=missing-function-docstring
    return VERSION_INFO_TEMPLATE_FULL.format(**VERSION_VARS)
