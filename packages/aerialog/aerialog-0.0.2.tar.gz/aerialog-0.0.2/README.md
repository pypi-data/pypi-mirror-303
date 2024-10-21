# Aerialog

A simple, yet effective logger built in Python.

## Features

- [x] Easily log to terminal or file
- [x] Coloured coded (only within terminal)
- [x] Log to file later on, and remove it
- [x] Lightweight, only needing one extra dependency
- [x] Load Log Level through .env or set it through the class

## Using Aerialog

1.  Run `python3 -m venv env` and then activate the environment through `source env/bin/activate` (may differ on Windows)
2.  Install the dependency using your preferred method `pip install aerialog`
3.  Import the dependency into your code `import aerialog.logger import Logger`
4.  Initalise the class and freely use it `log = Logger()`

You may also use `.env` files and directly set the log_level through that too

```env

#FATAL, ERROR, WARN, INFO, DEBUG, SILLY
# If not any of those above, it will default to DEBUG
# If it's not called LOG_LEVEL it will also default to DEBUG
LOG_LEVEL=DEBUG
```


## Example

```python

from aerialog import Logger

log = Logger()

def main():
    log.info("This is a really interesting info message!", "Main")
    log.error("Oh no! an error happened here", "Error")


def file_setup():
    log.set_file("awesome-project.log")
    log.info("This now gets logged to the file!", "File")
    log.remove_file() # It will now log back to the terminal
```

## Licence
This project uses the following license: [PYTHON PACKAGING AUTHORITY](https://github.com/devtomos/aerialog/blob/main/LICENSE.md).