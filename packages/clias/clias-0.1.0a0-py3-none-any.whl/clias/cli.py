from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

import click
import yaml  # type: ignore
from jinja2 import Template

from clias.run import run_command


@dataclass
class OptionSpec:
    name: list[str]
    help: str | None = None
    # TODO: implement the rest of the options
    type: str | tuple[str] | None = None
    default: str | int | tuple[str] | None = None
    show_default: bool | None = None
    nargs: int | None = None
    multiple: bool | None = None
    is_flag: bool | None = None
    flag_value: str | None = None
    prompt: bool | None = None
    hide_input: bool | None = None


@dataclass
class ArgumentSpec:
    name: str
    nargs: int | None = None


@dataclass
class CommandSpec:
    name: str
    help: str
    arguments: list[ArgumentSpec]
    options: list[OptionSpec]
    command: str
    shell: str | None = None


def name_and_else(dc):
    kwargs = dc.__dict__
    name = kwargs.pop("name")

    return name, kwargs


def get_config_file_path() -> Path | None:
    # from env var
    env_path = os.getenv("clias_CONFIG", None)

    if env_path:
        file_path = Path(env_path)

        if file_path.exists():
            return file_path

    # current dir
    file_path = Path(".clias.yml")
    if file_path.exists():
        return file_path

    # home dir
    file_path = Path("~/.clias.yml").expanduser()
    if file_path.exists():
        return file_path

    return None


def load_command_specs_from_yaml(file_path: Path) -> list[CommandSpec]:
    with open(file_path) as file:
        config = yaml.safe_load(file)

    if not config:
        raise ValueError("Invalid config file")

    default_shell = config.get("default", {}).get("shell", "/bin/bash")

    command_specs = []
    for command in config.get("commands") or []:
        arguments = [ArgumentSpec(**arg) for arg in command.get("arguments", [])]
        options = [OptionSpec(**opt) for opt in command.get("options", [])]
        command_spec = CommandSpec(
            name=command["name"],
            help=command["help"],
            command=command["command"],
            shell=command.get("shell", default_shell),
            arguments=arguments,
            options=options,
        )
        command_specs.append(command_spec)

    return command_specs


@click.group()
@click.option(
    "-d",
    "--dryrun",
    default=False,
    is_flag=True,
    help="dry run mode, only show the rendered command",
)
@click.version_option()
@click.pass_context
def cli(ctx, dryrun):
    "Turn shell script into cli command"

    # ensure that ctx.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    ctx.ensure_object(dict)

    ctx.obj["DRYRUN"] = dryrun


@cli.command()
def info():
    """Show the clias config file path to be loaded"""
    file_path = get_config_file_path()
    if not file_path:
        click.echo("No config file found")
        return

    click.echo(file_path.absolute())


def add_command(cli, spec: CommandSpec):
    @cli.command(name=spec.name, help=spec.help)
    @click.pass_context
    def command_func(ctx, **kwargs):
        is_dryrun = ctx.obj["DRYRUN"]

        if is_dryrun:
            click.echo(":dry run mode:")

        template = Template(spec.command)
        rendered = template.render(kwargs)

        if is_dryrun:
            click.echo(rendered)
            return

        # run the shell script
        for line in run_command(spec.shell, rendered):
            click.echo(line)

    for argument in spec.arguments:
        name, kwargs = name_and_else(argument)

        # click errors out if nargs is None
        if kwargs.get("nargs") is None:
            kwargs.pop("nargs")

        command_func = click.argument(name, **kwargs)(command_func)

    for option in spec.options:
        name, kwargs = name_and_else(option)

        command_func = click.option(*name, **kwargs)(command_func)

    return command_func


# dynamically create commands
config_file_path = get_config_file_path()
if config_file_path:
    specs = load_command_specs_from_yaml(config_file_path)

    if specs:
        for spec in specs:
            add_command(cli, spec)
