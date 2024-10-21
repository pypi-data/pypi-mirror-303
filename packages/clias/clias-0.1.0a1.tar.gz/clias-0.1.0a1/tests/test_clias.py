from tempfile import NamedTemporaryFile

from click.testing import CliRunner

from clias.cli import (
    ArgumentSpec,
    CommandSpec,
    OptionSpec,
    cli,
    load_command_specs_from_yaml,
)


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("cli, version ")


def test_info():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["info"])
        assert result.exit_code == 0


def test_load_empty_yaml():
    sample_yaml = """
    commands:
    """

    with NamedTemporaryFile(delete=False, mode="w") as temp_file:
        temp_file.write(sample_yaml)
        temp_file_path = temp_file.name

    loaded_specs = load_command_specs_from_yaml(temp_file_path)
    assert loaded_specs == []


def test_load_command_specs_from_yaml():
    sample_yaml = """
    commands:
      - name: my-echo
        help: echo command
        arguments:
          - name: message
        options:
          - name: ["-c", "--capitalize"]
            help: capitalize the message
        command: "echo {{ capitalize }} {{ message }}"

      - name: my-add
        help: add command
        arguments:
          - name: a
          - name: b
        command: echo $(({{a}} + {{b}}))
    """

    with NamedTemporaryFile(delete=False, mode="w") as temp_file:
        temp_file.write(sample_yaml)
        temp_file_path = temp_file.name

    loaded_specs = load_command_specs_from_yaml(temp_file_path)

    expected_specs = [
        CommandSpec(
            name="my-echo",
            help="echo command",
            command="echo {{ capitalize }} {{ message }}",
            arguments=[ArgumentSpec(name="message")],
            shell="/bin/bash",
            options=[
                OptionSpec(
                    name=["-c", "--capitalize"],
                    help="capitalize the message",
                )
            ],
        ),
        CommandSpec(
            name="my-add",
            help="add command",
            command="echo $(({{a}} + {{b}}))",
            shell="/bin/bash",
            arguments=[
                ArgumentSpec(name="a"),
                ArgumentSpec(name="b"),
            ],
            options=[],
        ),
    ]

    assert loaded_specs == expected_specs
