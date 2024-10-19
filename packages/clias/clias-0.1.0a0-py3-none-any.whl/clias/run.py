"""
ref: https://gist.github.com/almoore/c6fd2d041ad4f4bf2719a89c9b454f7e

A convenience module for shelling out with realtime output
includes:
- subprocess - Works with additional processes.
- shlex - Lexical analysis of shell-style syntaxes.
"""

from subprocess import PIPE, Popen


def run(command):
    process = Popen(command, stdout=PIPE, shell=True)
    while True:
        line = process.stdout.readline().rstrip()
        if not line:
            break
        yield line.decode("utf-8")


def run_command(shell, command):
    process = Popen([shell, "-c", command], stdout=PIPE, stderr=PIPE)
    stdout = None
    stderr = None
    while True:
        if (not stdout) and (not stderr) and process.poll() is not None:
            break

        stdout = process.stdout.readline().rstrip().decode("utf-8")
        if stdout:
            yield stdout

        stderr = process.stderr.readline().rstrip().decode("utf-8")
        if stderr:
            yield stderr

    rc = process.poll()
    return rc
