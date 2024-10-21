# Dazbo Commons

## Table of Contents

- [Overview](#overview)
- [To Install and Use](#to-install-and-use)
- [Coloured Logging Module](#coloured-logging-module)
- [To Build From Package Source](#to-build-from-package-source)

## Overview

A reusable utility library.

```text
dazbo-commons/
│
├── src/
│   └── dazbo_commons/
│       ├── __init__.py
│       └── colored_logging.py
│
├── tests/
│   └── test_colored_logging.py
│
├── .env
├── .gitignore
├── LICENSE
├── pyproject.toml
├── README.md
└── requirements.txt
```

## To Install and Use

You can simply install the package from [PyPi](https://pypi.org/project/dazbo-commons/). There's no need to clone this repo.

```bash
pip install --upgrade dazbo-commons
```

Then, in your Python code, include this `import`:

```python
import dazbo_commons as dc
```

### Coloured Logging Module

This module provides a function to retrieve a logger that logs to the console, with colour.

Example:

```python
import logging
import dazbo_commons as dc

logger_name = __name__ # or just pass in a str
logger = dc.retrieve_console_logger(logger_name)
logger.setLevel(logging.INFO) # Set threshold. E.g. INFO, DEBUG, or whatever

logger.info("Some msg") # log at info level
```

### File Locations Module

This module is used to retrieve a `Locations` class, which stores directory paths 
based on the location of a specified script. 
This makes it convenient to manage and access different file and directory paths 
relative to a given script's location.

Example:

```python
import dazbo_commons as dc
APPNAME = "My_App"

locations = get_locations(APP_NAME)

with open(locations.input_file, mode="rt") as f:
    input_data = f.read().splitlines()
```

## To Build From Package Source

1. Create a Python virtual environment and activate. E.g.

```bash
python3 -m venv .dazbo-commons-env
source .dazbo-commons-env/bin/activate
```

2. Install dependent packages:

```bash
py -m pip install -r requirements.txt
```

3. Run tests. E.g.

```bash
# Set env var so that the tests know how to find dazbo-commons
export PYTHONPATH=src

py -m unittest discover -v -s tests -p '*.py'

# Or, with pytest:
py -m pip install pytest
pytest
```

4. Install packages for actually creating the build. (If nto already included in `requirements.txt`):

```bash
py -m pip install twine
py -m pip install --upgrade build
```

5. Make any required updates to the `pyproject.toml` file. E.g. the `version` attribute.

6. Build the package.

```bash
py -m build
```

This generates a `dist` folder in your project folder.

7. Upload the package to [PyPi](https://pypi.org/). 

Notes:
- You'll need to create a free account, if you haven't done so already.
- You'll need to generate an API token in _Account Settings_, for uploading to the API.
- You may want to delete any previous builds.

```bash
py -m twine upload dist/*
```

You'll be prompted for your API token. In my experience, when doing this from a terminal inside VS Code, Ctrl-V doesn't work here. So I use Paste from the menu, and this works.

And we're done!