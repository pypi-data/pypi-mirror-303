# pyautorun

**pyauto** is a Python module that acts like a Makefile for Python projects. It allows you to define and execute a set of scripts easily using a configuration file. This tool helps in organizing and automating common project commands.

## Features
- **Configuration Management**: Store and organize scripts in a configuration file.
- **Easy Initialization**: Quickly create a default configuration file.
- **Add Scripts**: Append new commands to your configuration.
- **Search**: Find specific commands within the configuration.
- **Execute Scripts**: Run entire sections or individual commands by referencing their headers.

## Installation

To install pyautorun, use pip:

```bash
pip install pyautorun
```

## Configuration File Format

The default configuration file is `.pyscripts`, but you can specify a custom config file if needed. 

### **Rules for Configuration File**
1. **LOC Header**: The first line of the configuration file must always contain the **Line Of Configuration (LOC)** metadata, as follows:
   ```bash
   # Line Of Configuration (LOC) file = <filename> [<timestamp>]
   ```
   - This line will be automatically added during initialization `pyauto init`.

2. **Headers**: Every section must have a header. Headers should:
   - Begin with `[py.` and end with `]`.
   - Be properly closed, e.g., `[py.header]`.
   - One header can contain multiple commands.
   
3. **Commands**: Commands under each header must follow this format:
   - Each command should have a name and be assigned using `name = command`.
   - The first `=` in a line is prioritized to separate the command name from the script.

4. **Comments**: Comments can be prefixed with `#` and end with a newline.
   
5. **Ignored Lines**: Any lines that do not follow these rules will be ignored during execution.

### Example `.pyscripts` File

```ini
# Line Of Configuration (LOC) file = .pyscripts [Sun Oct 13 22:44:48 2024]

# comment
[py.header1]
cmd1_h1 = command 1 execution
cmd2_h1 = command 2 execution

[py.help]
help = python --help
python = python --help
```

### Structure
- Each header (e.g., `[py.header1]`) contains one or more command lines.
- Commands are defined using `name = command` pairs, where the name is the command name and the command is the script to execute.

## Usage

### 1. Create a Config File
To initialize a configuration file, use the `init` command:

```bash
pyauto init <file_name(optional)>
```

By default, the config file is created as `.pyscripts`, but you can provide a custom file name.

### 2. Add Commands
Add commands to a header within your config file using the `add` command:

```bash
pyauto add -h <header_name> -s '<script>' -c <configfile(optional)>
```

- `-h <header_name>`: Specify the header to add the command to.
- `-s '<script>'`: The script to be added, in the format `name = command`.
- `-c <configfile>`: Optional argument to specify the configuration file (default: `.pyscripts`).

### 3. Find Commands
Search for commands in the config file that start with a specific string:

```bash
pyauto find -l <line Startswith> -h <header> -c <configfile(optional)>
```
 - `-l <line Startswith>`: Specify the line to find.
 - `-h <header>`: Specify the header to find.
 - `-c <configfile>`: Optional argument to specify the configuration file (default: `.pyscripts`).

This will output all lines or header in the file that match the specified prefix.

### 4. Run Commands
Run all the commands in a specific header or a particular command by referencing it:

- To run all commands in a header:

```bash
pyauto run <header>
```

- To run a specific command within a header:

```bash
pyauto run <header>.<command_name>
```

## Example Workflow

1. **Initialize the config**:
   ```bash
   pyauto init .pyautorun.test
   ```

2. **Add a new command**:
   ```bash
   pyauto add -h tests -s "test = tested sucessfully" -c .pyautorun.test 
   ```

3. **Run a command from the header**:
   ```bash
   pyauto run tests -c .pyautorun.test
   ```

4. **Find commands starting with a specific line**:
   ```bash
   pyauto find -l test -h tests -c .pyautorun.test
   ```

## Contributing

If you have any suggestions or feedback, please [open an issue](https://github.com/rakeshkanna-rk/pipCreator/issues) or [create a pull request](https://github.com/rakeshkanna-rk/pipCreator/pulls).

## License

This project is licensed under the [MIT License](https://github.com/rakeshkanna-rk/pipCreator/blob/main/LICENSE).
