# al78 tools

## Tools for Python setup file
Simple tools to complete setup.py file


## Installation
```bash
pip3 install al78tools
```

## Usage

### Handle App first run

There is no way to run some post install bash code after pip package installation. But you can use this simple
tool to run some bash code after first run of your app.

#### Example
`main.py` file
```python
import os
from al78tools.pysetup.first_run import first_run_decorator
from al78tools.pysetup.tools import get_file_content


APP = "my-app-name"
VERSION = get_file_content(os.path.join(os.path.dirname(__file__), "VERSION"))


@first_run_decorator(APP, VERSION)
def _handle_first_run():
    import subprocess
    result = subprocess.run([os.path.join(os.path.dirname(__file__), "postinstall.sh")])
    if result.returncode != 0:
        print("Postinstall script failed.")


def main():    
    _handle_first_run()
    # rest of your code

if __name__ == '__main__':
    main()
```
!!! Warning !!! Do not forget to add `postinstall.sh` file to your `MANIFEST.in` file.
After this, you can use `postinstall.sh` file to run some bash code after first run of your app.
There is a version string compare mechanism. If version differs from previous version, the `postinstall.sh` will be run.
If you want to run `postinstall.sh` only once during all package updates, do not fill version paremeter in `first_run_decorator` function
and it will run only for the first time of package installation.


### File content reading
`setup.py` file
```python
import os
from al78tools.pysetup.tools import get_file_content, get_file_content_as_list


pwd = os.path.dirname(__file__)

VERSION = get_file_content(os.path.join(pwd, "VERSION"))
README_MD = get_file_content(os.path.join(pwd, "README.md"))
requirements = get_file_content_as_list(os.path.join(pwd, "requirements.txt"))
```
