#!/usr/bin/env python

import click
import docker
from et_engine_cli.tools.commands import tools
from et_engine_cli.filesystems.commands import filesystems

@click.group()
def cli():
    pass


@cli.command()
def login():
    """Log in to your ET Engine account"""
    username = click.prompt('Email', type=str)
    password = click.prompt('Password', type=str, hide_input=True)
    client = docker.from_env()
    response = client.login(username, password=password, registry="https://tools.exploretech.ai/v2/")
    click.echo(response["Status"])


cli.add_command(tools)
cli.add_command(filesystems)


if __name__ == '__main__':
    cli()
