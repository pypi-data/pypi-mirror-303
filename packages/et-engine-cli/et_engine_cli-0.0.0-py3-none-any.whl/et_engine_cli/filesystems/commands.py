import click
import os
import json
import sys

import et_engine as et
engine = et.Engine()


def check_api_key():
    """check if the api key exists"""
    if "ET_ENGINE_API_KEY" not in os.environ:
        click.echo("Error: ET_ENGINE_API_KEY environment variable is not set.", err=True)
        sys.exit(1)


@click.group()
def filesystems():
    """Filesystem operations"""
    check_api_key()


@filesystems.command()
@click.argument('name')
def create(name):
    """Create a new filesystem"""
    try:
        status = engine.filesystems.create(name)
        if status.ok:
            click.echo(f"Filesystem '{name}' created successfully.")
        else:
            click.echo("Failed to create filesystem.", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@filesystems.command()
def list():
    """List all filesystems"""
    try:
        filesystem_list = engine.filesystems.list_filesystems()
        click.echo(json.dumps(filesystem_list, indent=2))
    except PermissionError as e: #used to be AuthenticationError from et_engine.errors
        click.echo(f"Authentication Error: {str(e)}", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@filesystems.command()
@click.argument('name')
def delete(name):
    """Delete a filesystem"""
    try:
        status = engine.filesystems.delete(name)
        if status.ok:
            click.echo(f"Filesystem '{name}' deleted successfully.")
        else:
            click.echo("Failed to delete filesystem.", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@filesystems.command()
@click.argument('name')
@click.argument('local_file')
@click.argument('remote_file')
@click.option('--chunk-size', default=10*1024, help="Chunk size for multipart upload")
def upload(name, local_file, remote_file, chunk_size):
    """Upload a file to a filesystem"""
    try:
        filesystem = engine.filesystems.connect(name)
        filesystem.upload(local_file, remote_file, chunk_size=chunk_size)
        click.echo(f"File '{local_file}' uploaded to '{remote_file}' successfully.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@filesystems.command()
@click.argument('name')
@click.argument('remote_file')
@click.argument('local_file')
@click.option('--chunk-size', default=10*1024, help="Chunk size for multipart download")
def download(name, remote_file, local_file, chunk_size):
    """Download a file from a filesystem"""
    try:
        filesystem = engine.filesystems.connect(name)
        filesystem.download(remote_file, local_file, chunk_size=chunk_size)
        click.echo(f"File '{remote_file}' downloaded to '{local_file}' successfully.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@filesystems.command()
@click.argument('name')
@click.argument('path')
@click.option('--ignore-exists', is_flag=True, help="Ignore if directory already exists")
def mkdir(name, path, ignore_exists):
    """Create a directory in a filesystem"""
    try:
        filesystem = engine.filesystems.connect(name)
        filesystem.mkdir(path, ignore_exists)
        click.echo(f"Directory '{path}' created successfully.")
    except FileNotFoundError as e:
        click.echo(f"Error: {str(e)}", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@filesystems.command()
@click.argument('name')
@click.argument('path')
def rm(name, path):
    """Delete a file or directory from a filesystem"""
    try:
        filesystem = engine.filesystems.connect(name)
        filesystem.delete(path)
        click.echo(f"'{path}' deleted successfully.")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@filesystems.command()
@click.argument('name')
@click.argument('path', required=False)
def ls(name, path):
    """List files in a filesystem"""
    try:
        filesystem = engine.filesystems.connect(name)
        files = filesystem.list(path)
        click.echo(json.dumps(files, indent=2))
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)