import sys
import typer
import subprocess
import re
from typing import List, Optional

app = typer.Typer()


class SystemFunction:
    def __init__(self, command):
        self.command = command
        self.options = self._parse_help()

    def _parse_help(self):
        try:
            help_output = subprocess.check_output([self.command, '--help'], stderr=subprocess.STDOUT, text=True)
        except subprocess.CalledProcessError as e:
            help_output = e.output

        options = {}
        for line in help_output.split('\n'):
            match = re.match(r'\s*(-\w)?,?\s*(--[\w-]+)?\s*(.+)', line)
            if match:
                short_opt, long_opt, description = match.groups()
                if short_opt:
                    options[short_opt[1:]] = description.strip()
                if long_opt:
                    options[long_opt[2:]] = description.strip()
        return options

    def __call__(self, *args, pipe=None, **kwargs):
        cmd = [self.command]

        for k, v in kwargs.items():
            if k in self.options:
                if len(k) == 1:
                    cmd.append(f'-{k}')
                else:
                    cmd.append(f'--{k}')
                if v is not True and v is not False:
                    cmd.append(str(v))
            else:
                raise ValueError(f"Unknown option: {k}")

        cmd.extend(args)

        if pipe:
            process = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
            stdout, _ = process.communicate(input=pipe)
        else:
            process = subprocess.run(cmd, capture_output=True, text=True)
            stdout = process.stdout

        return stdout.strip()


def create_system_function(command):
    return SystemFunction(command)


@app.command()
def run_command(
    command: str,
    args: Optional[List[str]] = typer.Argument(None),
    options: Optional[List[str]] = typer.Option(None, "--option", "-o"),
    pipe: Optional[str] = typer.Option(None, "--pipe", "-p"),
    print_args: bool = typer.Option(False, "--print-args", "-P", help="Print available options for the command")
):
    """Run a system command with parsed options."""
    func = create_system_function(command)

    # Handle default for args
    if args is None:
        args = []

    # Print options if flag is set and exit
    if print_args:
        typer.echo(f"Available options for {command}:")
        for opt, desc in func.options.items():
            typer.echo(f"  {opt}: {desc}")
        return

    # Prepare kwargs
    kwargs = {}
    if options:
        for option in options:
            key, _, value = option.partition('=')
            kwargs[key] = value if value else True

    # Handle piping from standard input
    if pipe is None and not sys.stdin.isatty():
        pipe = typer.get_text_stream("stdin").read().strip() or None

    # Run command
    result = func(*args, pipe=pipe, **kwargs)
    typer.echo(f"\nCommand output:\n{result}")


if __name__ == "__main__":
    app()
