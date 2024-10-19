# glbuild

A tool to collect the entire history of build data and logs (at once) from GitLab projects.

## Requirements

- Python 3.10
- [Poetry](https://python-poetry.org/)

## Get started

Install dependencies

```bash
poetry install
```

Access virtual environment

```bash
poetry shell
```

Install pre-commit hook for static code analysis

```bash
pre-commit install
```

## Usage

Install the Python package using Pip

>```bash
>pip install glbuild
>```

Use in a Python script as follows:

```python
import glbuild

glb = glbuild.GitLabBuild(base_url="https://gitlab.com", token="******", projects=[1538, 5427])

glb.start(output="./data")
```

Use in a Bash command line as follows:

```bash
glbuild --base-url https://gitlab.com --token ****** --output ./data --project 1538 --project 5427
```

Contracted CLI command:

```bash
glbuild -b https://gitlab.com -t ****** -o ./data -p 1538 -p 5427
```
