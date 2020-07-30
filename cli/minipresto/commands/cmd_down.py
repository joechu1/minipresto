#!usr/bin/env/python3
# -*- coding: utf-8 -*-

import sys
import click

from minipresto.commands.core import check_daemon
from minipresto.cli import pass_environment

from minipresto.settings import RESOURCE_LABEL


@click.command("down", help="""
Brings down all running minipresto containers. This command follows the
behavior of `docker-compose down`, where containers are both stopped and
removed.
""")


@pass_environment
def cli(ctx):
    """
    Down command for minipresto. Exits with a 0 status code if there are no
    running minipresto containers.
    """

    docker_client = check_daemon()

    containers = docker_client.containers.list(
        filters={"label": RESOURCE_LABEL}, all=True
    )

    if len(containers) == 0:
        ctx.log(f"No containers to bring down")
        sys.exit(0)

    for container in containers:
        container.stop()
        container.remove()  # Default behavior of Compose is to remove containers
        ctx.vlog(f"Stopped/removed container: {container.short_id} | {container.name}")

    ctx.log(f"Brought down all running minipresto containers")