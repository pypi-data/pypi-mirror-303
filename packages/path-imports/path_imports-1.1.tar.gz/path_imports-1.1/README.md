## Introduction

Import modules from anywhere on the file system.

## Usage

```python
import path_imports


# Import a certain file
foo_module = path_imports.import_from_path('somewhere/on your/file system/foo.py')

# Import a module from a certain directory
submodule = path_imports.import_from_directory('some/directory', 'root_module.submodule')

# Find the file path of a module
path = path_imports.find_module_location('my_module', directory='my project folder')
print(path)  # Output: "my project folder/my_module.py"
```

## Installation

```
pip install path-imports
```

## Documentation

There is no online documentation; however, the module has docstrings and type annotations. Your IDE
should display all the relevant information to you.
