# Command Line System Function Runner

This package provides a command-line interface for running system commands with parsed options and arguments. It dynamically generates a function interface for any system command, allowing for easy execution and option handling.

## Features

- Dynamic parsing of command options from `--help` output
- Support for short and long option formats
- Piping input from standard input or command line argument
- Ability to list available options for a command

## Installation

To install the package, clone the repository and install the dependencies:

```
git clone <repository-url>
cd <repository-directory>
pip install -r requirements.txt
```

## Usage

Run the script with the following syntax:

```
python script_name.py <command> [ARGS]... [OPTIONS]
```

### Arguments

- `command`: The system command to run
- `ARGS`: Additional arguments for the command (optional)

### Options

- `-o, --option TEXT`: Specify command options (can be used multiple times)
- `-p, --pipe TEXT`: Provide input to pipe to the command
- `-P, --print-args`: Print available options for the command
- `--help`: Show help message and exit

## Examples

1. List available options for a command:
   ```
   python script_name.py ls --print-args
   ```

2. Run a command with options:
   ```
   python script_name.py ls -o l -o a /home
   ```

3. Pipe input to a command:
   ```
   python script_name.py grep -o i -p "search text" search_pattern
   ```

4. Use standard input:
   ```
   echo "Hello, World!" | python script_name.py grep World
   ```

## Note

This tool is designed for educational and development purposes. Use caution when running system commands, especially with elevated privileges.
