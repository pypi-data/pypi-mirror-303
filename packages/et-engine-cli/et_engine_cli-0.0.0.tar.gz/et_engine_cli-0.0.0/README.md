# ET Engine Command-Line Interface Tool

The official CLI for interacting with ET Engine resources

| Resource | Link |
|:----|:-----|
| Command-Line Interface (CLI) tool | https://github.com/exploretech-ai/et-engine-cli |
| ET Engine Web App | https://engine.exploretech.ai |
| Comprehensive Documentation | https://docs.exploretech.ai |
| About ExploreTech | https://exploretech.ai |


# Quick Start

First, First, make sure you have an account on the [ET Engine Web App](https://engine.exploretech.ai).

Next, ensure your Python version is >=3.11.9 and install the CLI using pip.

```bash
pip install et-engine-cli
```

Log into the ET Engine using your ET Engine credentials.

```bash
et login
```

Get help on the commands.

```bash
et -h
et tools -h
et filesystems -h
```

View the available tools.

```bash
et tools list
```

View the available filesystems.

```bash
et filesystems list
```

# Creating Tools

First, create a new folder called `my-first-tool` where you want to house the tool.

```bash
mkdir my-first-tool
cd my-first-tool
```

Initialize the folder as a new tool named `hello-tool`.
```bash
et tools init hello-tool
```

This will create a simple tool inside the current directory. Building tools is very similar to building Docker images. In fact, that's exactly what the CLI does under the hood, just in a very specific way. For this example, you can build the tool using the following command.

```bash
et tools build --name hello-tool .
```

This packages your tool into a Docker image stored on your local computer. When you're ready, you can push it to ET Engine using 

```bash
et tools push hello-tool
```

The tool can now be run like a function via the [Engine Web App](https://engine.exploretech.ai) or the [Python SDK](https://github.com/exploretech-ai/et-engine-python) with a script such as below.

```python
import et_engine as et
engine = et.Engine()

hello = engine.tools.connect("hello-tool")
hello(name="John")
hello(name="Jane")
```

# Contributing

We welcome contributions from the community. See `CONTRIBUTING.md` for more details.
