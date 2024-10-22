 # Zinley CLI

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/downloads/)

A simple and efficient command line application written in Python.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Feature 1:** Description of feature 1.
- **Feature 2:** Description of feature 2.
- **Feature 3:** Description of feature 3.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. Navigate to the project directory:

    ```bash
    cd zinley-cli
    ```

3. Create and activate a virtual environment:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

To use the application, simply run the main script with the desired command and options.

```bash
python3 -m zinley [command] [options]
```

## Commands
### start
- Creates a new project at the specified path if it doesn't exist.
- Opens an existing project at the specified path.

```bash
zinley start <path>
```

Example
- To create a new project at `/path/to/new/project`:
```bash
zinley start /path/to/new/project
```
### Code
Initiates the coding process based on the provided input string.

```bash
zinley code <prompt>
```
Example
- To start coding with the prompt "create a function to calculate factorial":
```bash
zinley code "create a function to calculate factorial"
```

### scan
Initiates the coding process based on the provided input string.

```bash
zinley scan <options> <path>
```

Options can be
- `all`: scan all files and folder
- `image`: scan images only
- ...(other types can be added)

Example
- To scan all files and folders in /path/to/project:

```bash
zinley scan --all /path/to/project
```

### run
Executes the application at the current project path.

```bash
zinley run
```

```

## Build wheel

```bash
python3 setup.py sdist bdist_wheel
```

### Installing Zinley CLI
### Update Zinley
pip3 install --upgrade dist/zinley-0.2.5-py3-none-any.whl --break-system-packages

### Uninstall
pip3 uninstall Zinley --break-system-packages