# uvxt - uv tools collection

A collection of tools that, in conjunction with the capabilities of the uv, will increase your productivity

[![PyPI](https://img.shields.io/pypi/v/uvxt)](https://pypi.org/project/uvxt/)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/uvxt)](https://pypi.org/project/uvxt/)

[![Downloads](https://static.pepy.tech/badge/uvxt)](https://pepy.tech/project/uvxt)
[![GitLab stars](https://img.shields.io/gitlab/stars/rocshers/python/uvxt)](https://gitlab.com/rocshers/python/uvxt)
[![GitLab last commit](https://img.shields.io/gitlab/last-commit/rocshers/python/uvxt)](https://gitlab.com/rocshers/python/uvxt)

## Quick start

```bash
uv tool install uvxt
uvxt up --latest
```

or

```bash
uvx uvxt up --latest
```

## Commands

- `uvx uvxt version` - Launch the [uv-version](https://pypi.org/project/uv-version/)
- `uvx uvxt up` - Launch the [uv-version](https://pypi.org/project/uv-up/)

## Contribute

Issue Tracker: <https://gitlab.com/rocshers/python/uvxt/-/issues>  
Source Code: <https://gitlab.com/rocshers/python/uvxt>

### How to add a new tool?

1) Create your CLI application.
   - We strongly recommend using `typer` for easy integration into uvxt.
   - Make sure that your package dependencies do not conflict with those already described in uvxt.
2) Upload your module to PyPI.
3) Add this package as a dependency to uvxt via `uv add`.
4) Import your CLI application in [uvxt/cli.py](./uvxt/cli.py)
5) Check that everything works fine.
6) Make a PR.

### Development Commands

Before adding changes:

```bash
make install
```

After changes:

```bash
make format test
```
