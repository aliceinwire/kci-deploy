#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import logging

import click

from kcideploy.libs.common import *
from kcideploy.subcommands import (
    deploy,
)

@click.group(
    help="Stand alone tool for deploy KernelCI maestro"
)
@click.version_option("0.0.1", prog_name="kci-deploy")
@click.option(
    "--settings",
    default=".kci-deploy.toml",
    help="Local settings file to use",
    required=False,
)
@click.option("--debug", is_flag=True, help="Enable debug info")
@click.pass_context
def cli(ctx, settings, debug):
#    if debug:
        # DEBUG level is too verbose about included packages
        # us INFO instead
 #       logging.basicConfig(level=logging.INFO)

  #  subcommands = ctx.invoked_subcommand
    pass

def run():
    cli.add_command(deploy.deploy)
    cli()

if __name__ == "__main__":
    run()
