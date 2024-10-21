# dir-audit

|   |   |
|---|---|
|Project|[![Python Versions](https://img.shields.io/badge/Python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11%20%7C%203.12-blue?logo=python&logoColor=white)](https://www.python.org/) [![License](https://img.shields.io/github/license/deltodon/dir-audit)](LICENSE) |
|Quality| [![Issues](https://img.shields.io/github/issues/deltodon/dir-audit)](https://github.com/deltodon/dir-audit/issues) |
| Tools | [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://pre-commit.com/) [![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/) |
|Community|[![Maintenance](https://img.shields.io/badge/Maintained-yes-green)](https://github.com/deltodon/dir-audit/graphs/commit-activity) [![Stars](https://img.shields.io/github/stars/deltodon/dir-audit)](https://github.com/deltodon/dir-audit)  [![Forks](https://img.shields.io/github/forks/deltodon/dir-audit)](https://github.com/deltodon/dir-audit/network/members)  [![Contributors](https://img.shields.io/github/contributors/deltodon/dir-audit)](https://github.com/deltodon/dir-audit/graphs/contributors)  [![Commit activity](https://img.shields.io/github/commit-activity/m/deltodon/dir-audit)](https://github.com/deltodon/dir-audit/commits/main)|

Directory tree audit tool

### Setup

install with pip

```bash
pip install dir-audit
```

or with [Poetry](https://python-poetry.org/)

```bash
poetry add dir-audit
```

### Usage

get help

```bash
poetry run python dir_audit --help
usage: dir-audit [-h] [-v] {make,check} ...

Audit directory tree structure

positional arguments:
  {make,check}   Audit command
    make         Make directory tree
    check        Check directory tree

options:
  -h, --help     show this help message and exit
  -v, --version  Get dir-audit version
```

> NOTE: `make` command is still work in progress.

check for empty directories

```bash
poetry run python dir_audit check --empty /path/to/your/directory
```

check for files and directories that contain substring (i.e.: `admin`)

```bash
poetry run python dir_audit check --contains admin /path/to/your/directory
```

print full directory tree

```bash
poetry run python dir_audit check --full /path/to/your/directory
```
