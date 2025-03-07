#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import click
import os

def create_directory():
    pass


@click.command(help="Deploy KernelCI")
@click.option(
    "--path",
    help="Platform filter to trigger",
)
@click.pass_context
def deploy(ctx, path):
    print("deploy to :"+ str(path))
    print('write code for deploy KernelCI')
    os.makedirs(path, exist_ok=True)
    os.chdir(path)
    os.system("git clone https://github.com/kernelci/kernelci-core") 
    os.chdir("kernelci-core")
    os.system("git fetch origin")
    os.system("git checkout origin/staging.kernelci.org")
    os.chdir("../")
    os.system("git clone https://github.com/kernelci/kernelci-api")
    os.chdir("kernelci-api")
    os.system("git fetch origin")
    os.system("git checkout origin/staging.kernelci.org")
    os.chdir("../")
    os.system("git clone https://github.com/kernelci/kernelci-pipeline")
    os.chdir("kernelci-pipeline")
    os.system("git fetch origin")
    os.system("git checkout origin/staging.kernelci.org")
    os.chdir("../")
