# Python template environment
This project represents a default setup for development (in development).
It features:
1. List of dependencies (`requirements.txt`)
2. Code analysis (`pylint`)
3. Tests (`pytest`)

## Quickstart
(Optional) Activate your python environment (virtualenv,...)

### Install dependencies:
```bash
pip install -r requirements.txt
```
### Code analysis
```bash
pylint utils/demo.py
```
### Running tests
```bash
# in project root
py.test
```
Alternatively, you can use VS Code for this.
First, make sure to correctly select your python interpreter.

Then, run in project root folder:
1. `Python: Configure Tests`
2. Select `pytest`
3. Select the folder `test`.

Then you should be able to execute the command `Python: Run all tests`
