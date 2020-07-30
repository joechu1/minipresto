#!usr/bin/env/python3
# -*- coding: utf-8 -*-

# Docker labels
RESOURCE_LABEL = "com.starburst.tests=minipresto"
MODULE_LABEL_KEY_ROOT = "com.starburst.tests.module"

# Generic Constants
CONTAINER = "container"
IMAGE = "image"
VOLUME = "volume"
LIB = "lib"
MODULE_ROOT = "modules"
MODULE_CATALOG = "catalog"
MODULE_SECURITY = "security"

# Snapshots
SNAPSHOT_ROOT_FILES = ["docker-compose.yml", ".env", "Dockerfile"]

# Terminal
DEFAULT_INDENT = " " * 5

# Scrub Keys
SCRUB_KEYS = [
    "accesskey",
    "apikey",
    "secretkey",
    "-key",
    "_key",
    "password",
]

# Templates
CONFIG_TEMPLATE = """
[CLI]
LIB_PATH=

[DOCKER]
STARBURST_LIC_PATH=

S3_ENDPOINT=s3.region.amazonaws.com
S3_ACCESS_KEY=
S3_SECRET_KEY=
AWS_REGION=

LDAP_ORGANISATION=
LDAP_DOMAIN=
LDAP_ADMIN_PASSWORD=

SNOWFLAKE_DIST_CONNECT_URL=
SNOWFLAKE_DIST_CONNECT_USER=
SNOWFLAKE_DIST_CONNECT_PASSWORD=
SNOWFLAKE_DIST_WAREHOUSE=
SNOWFLAKE_DIST_DB=
SNOWFLAKE_DIST_STAGE_SCHEMA=

SNOWFLAKE_JDBC_CONNECT_URL=
SNOWFLAKE_JDBC_CONNECT_USER=
SNOWFLAKE_JDBC_CONNECT_PASSWORD=
SNOWFLAKE_JDBC_WAREHOUSE=
SNOWFLAKE_JDBC_DB=
SNOWFLAKE_JDBC_STAGE_SCHEMA=
"""

PROVISION_SNAPSHOT_TEMPLATE = """
#!/usr/bin/env bash

# ------------------------------------------------------------------------------
# Below is the exact command used to provision the snapshotted environment. Run
# this command in your terminal to reproduce the exact state of the environment.
# ------------------------------------------------------------------------------


"""