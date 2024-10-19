# clias

[![PyPI](https://img.shields.io/pypi/v/clias.svg)](https://pypi.org/project/clias/)
[![Changelog](https://img.shields.io/github/v/release/kj-9/clias?include_prereleases&label=changelog)](https://github.com/kj-9/clias/releases)
[![Tests](https://github.com/kj-9/clias/actions/workflows/ci.yml/badge.svg)](https://github.com/kj-9/clias/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/kj-9/clias/blob/master/LICENSE)

Turn shell script into CLIs

## Installation

Install this tool using `pip`:
```bash
pip install clias
```
## Usage

For help, run:
<!-- [[[cog
import cog
from clias import cli
from click.testing import CliRunner
runner = CliRunner()
result = runner.invoke(cli.cli, ["--help"])
help = result.output.replace("Usage: cli", "Usage: clias")
cog.out(
    f"```bash\n{help}\n```"
)
]]] -->
```bash
Usage: clias [OPTIONS] COMMAND [ARGS]...

  Turn shell script into cli command

Options:
  -d, --dryrun  dry run mode, only show the rendered command
  --version     Show the version and exit.
  --help        Show this message and exit.

Commands:
  info  Show the clias config file path to be loaded

```
<!-- [[[end]]] -->

You can also use:
```bash
python -m clias --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd clias
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
make install-e
```
To run the tests:
```bash
make test
```

To run pre-commit to lint and format:
```bash
make check
```

`make check` detects if cli help message in `README.md` is outdated and updates it.

To update cli help message `README.md`:
```bash
make readme
```

this runs [cog](https://cog.readthedocs.io/en/latest/) on README.md and updates the help message inside it.
