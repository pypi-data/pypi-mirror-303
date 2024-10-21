# CGI Multiprocess

## Description

Multiprocessing with Process Pools implemented using Processes and Shared Memory objects.

- Built in progress bar.
- Graceful shutdown by default (CTRL+C 2x, will kill immediately).
- Automatically calls join
- Allows re-use of pool after join, cutting down on process spawning time.

## Example

`pants run :example`

## Development setup

1. Open repository in vscode using the following:
`code .`

This ensures environment variable proliferation into the vscode shell

2.When prompted by vscode (lower right) to Open in Container, say Yes

3.VSCode will restart and reopen in the Container (This may take a minute if the container has not yet been built)

4.Open a new ZSH terminal in VSCode (this will initialize pants)

## Run Tests

`pants test ::`

## Rebuild lock files

To rebuild lock files (after package updates or installation)
`pants generate-lockfiles`

## Build distribution

`pants package :dist`

## Export Virtualenv

Use pants to export virtualenvs:
`pants export --resolve=python-default --resolve=pytest`

Source the virtualenv for use with poetry:
`source dist/export/python/virtualenvs/python-default/$CODE_PYTHON_VERSION.*/bin/activate`

Install local directory:
`pip install .`

## Update dependencies

1. Follow "Update Virtualenv"
2. From the poetry shell type:
`poetry update`
3. Follow instructions from "Rebuild lock files"
4. Commit the lock files

## Run precommit manually

`pre-commit run --all-files --hook-stage commit`
`pre-commit run --all-files --hook-stage push`
