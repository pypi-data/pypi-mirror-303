import click
import os
import json
import sys
import docker

import et_engine as et
engine = et.Engine()


TOOL_FILE_LIST = [
    "Dockerfile",
    "README.md",
    "test.sh",
    "tool_name.py",
    "tool.py",
    "tool.json"
]


def check_api_key():
    if "ET_ENGINE_API_KEY" not in os.environ:
        click.echo("Error: ET_ENGINE_API_KEY environment variable is not set.", err=True)
        sys.exit(1)


@click.group()
def tools():
    """Tool operations"""
    check_api_key()


@tools.command()
@click.argument('name')
@click.argument('description')
def create(name, description):
    """Create a new tool"""
    try:
        status = engine.tools.create(name, description)
        if status.ok:
            click.echo(f"Tool '{name}' created successfully.")
        else:
            click.echo("Failed to create tool.", err=True)
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@tools.command()
@click.argument('name')
def status(name):
    """Get status of a tool"""
    try:
        tool = engine.tools.connect(name)
        status = tool.status()
        click.echo(json.dumps(status, indent=2))
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@tools.command()
@click.argument("path", type=click.Path(exists=True))
@click.option("-f", "--file", type=click.Path(exists=True))
@click.option("--platform", type=str)
@click.option("--name", type=str)
def build(path, file, platform, name):
    """Builds the tool as a docker image"""
    
    # Read the JSON to get the tool name
    if name is None:
        with open("tool.json", "r") as f:
            tool_json = json.load(f)
            name = tool_json["tool_name"]

    # Get the tool ID from ET Engine API
    tool = engine.tools.connect(name)

    # Parse tool.py to get a list of function args (these will get pushed to the ET Engine Platform during push)
    # TODO

    # Build the image
    kwargs = {
        "path": path,
        "tag": tool.id,
        "dockerfile": file,
        "quiet": False
    }
    if platform is not None:
        kwargs["platform"] = platform

    click.echo("Starting build...")
    client = docker.from_env()
    image, generator = client.images.build(**kwargs)

    # Dump logs
    for chunk in generator:
        if "stream" in chunk:
            click.echo(chunk["stream"], nl=False)

    # Final message
    success = image.tag(f"tools.exploretech.ai/{tool.id}")
    if success:
        click.echo(f"Push using 'et tools push {name}'")
    else:
        click.echo("Error tagging tool")


@tools.command()
@click.argument("name")
def push(name):
    """Pushes the tool to ExploreTech's Tool Registry"""

    client = docker.from_env()
    tool = engine.tools.connect(name)
    generator = client.images.push(f"tools.exploretech.ai/{tool.id}", stream=True, decode=True)

    for chunk in generator:
        click.echo(chunk)


@tools.command()
@click.argument('name')
@click.argument('args', nargs=-1)
def run(name, args):
    """Run a tool with given arguments"""
    try:
        tool = engine.tools.connect(name)
        kwargs = dict(arg.split('=') for arg in args)
        batch = tool(**kwargs)
        click.echo(f"Tool '{name}' started with batch ID: {batch.id}")
    except Exception as e:
        click.echo(f"Error: {str(e)}", err=True)


@tools.command()
@click.argument("tool_name")
def init(tool_name):
    """Initialize a tool in the current directory"""

    message = f'Initializing tool {tool_name}...'
    click.echo(message)

    current_directory = os.path.abspath(os.path.dirname(__file__))
    template_directory = os.path.join(current_directory, "templates", "python_tool")
    command_source_directory = os.getcwd()

    for file in TOOL_FILE_LIST:

        init_file = os.path.join(template_directory, file)
        if file == "tool_name.py":
            dest_file = os.path.join(command_source_directory, f"{tool_name}.py")
        else:
            dest_file = os.path.join(command_source_directory, file)

        if os.path.exists(dest_file):
            click.echo(f"Error: File '{dest_file}' already exists.", err=True)
            sys.exit(1)

        with open(init_file, "r") as f:
            file_contents = f.read()
        file_contents = file_contents.replace("<<{{TOOL_NAME}}>>", tool_name)

        with open(dest_file, "w") as f:
            f.write(file_contents)

    click.echo(f"Tool '{tool_name}' initialized successfully.")


tools.TOOL_FILE_LIST = TOOL_FILE_LIST