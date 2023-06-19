# Tree-styled folder structure printer 📁 → 🌳

Tiny python tool for printing any folder structure as a tree.

> **Easy way to present the project structure (for example, in README.md).**

## How to use 🛠️

- Clone with `git clone https://github.com/jiptwo553900/folder-tree-printer.git`
- Copy `tree.py` to the root of your project (or any other folder)
- Run `tree.py`

## Configuration and options ⚙️

> Config section is on the top of `tree.py`, just after imports.

|       Name and type       | Info                                                            |                 Defaults to                 |
|:-------------------------:|:----------------------------------------------------------------|:-------------------------------------------|
|    `FOLDER_ICON: str`     | icon for folders                                                |                    `📁`                     |
|     `FILE_ICON: str`      | icon for files                                                  |                    `📄`                     |
|       `INDENT: str`       | general indent (from left side)                                 |                    `│  `                    |
|    `ENTRY_INDENT: str`    | entry indent                                                    |                    `├──`                    |
| `LAST_ENTRY_INDENT: str`  | indent for the last entry in a folder                           |                    `└──`                    |
|    `SHOW_HIDDEN: bool`    | if True: show hidden folders (.git, etc)                        |                   `False`                   |
|    `PRINT_ROOT: bool`     | if True: print root directory                                   |                   `True`                    |
| `HIDDEN: tuple[str, ...]` | Prefixes of folders we want to ignore when show_hidden is False |           `(".", "__pycache__")`            |
|     `ROOT_PATH: str`      | Current directory path                                          | `os.path.dirname(os.path.realpath(__file__))` |

## Call and output examples 📝

### Default values:

```
print_tree()
```
Output:
```
├── 📁 folder-tree-printer
│   ├── 📄 .gitignore
│   ├── 📄 README.md
│   ├── 📁 sample_structure
│   │   ├── 📄 sample_file
│   │   └── 📁 sample_folder
│   │   │   ├── 📄 .hidden_file
│   │   │   └── 📁 nested_sample_folder
│   │   │   │   └── 📁 nested_folder
│   │   │   │   │   └── 📄 sample_file
│   └── 📄 tree.py
```

### Custom root path:

You can change `ROOT_PATH`:
```
# Example.
ROOT_PATH: str = ".."

# Example.
ROOT_PATH: str = os.path.dirname(os.path.realpath(__file__)) + "/sample_structure"
```
Or you can call `print_tree()` with args:  
```
# Example.
print_tree(root_path="..")

# Example.
print_tree(root_path=ROOT_PATH + "/sample_structure")
```
Output (for the `sample_structure` folder)::
```
├── 📁 sample_structure
│   ├── 📄 sample_file
│   └── 📁 sample_folder
│   │   ├── 📄 .hidden_file
│   │   └── 📁 nested_sample_folder
│   │   │   └── 📁 nested_folder
│   │   │   │   └── 📄 sample_file
```

### If you don`t want to ignore "hidden" folders:

You can change `SHOW_HIDDEN`:
```
SHOW_HIDDEN: bool = True
```
Or you can call `print_tree()` with args:  
```
print_tree(show_hidden=True)
```
Output (for the `sample_structure` folder):
```
├── 📁 sample_structure
│   ├── 📁 .hidden_folder
│   │   ├── 📁 nested_sample_folder
│   │   │   ├── 📄 .hidden_file
│   │   │   └── 📁 __pycache__sample
│   │   └── 📄 sample_file
│   ├── 📄 sample_file
│   ├── 📁 sample_folder
│   │   ├── 📄 .hidden_file
│   │   └── 📁 nested_sample_folder
│   │   │   ├── 📁 nested_folder
│   │   │   │   └── 📄 sample_file
│   │   │   └── 📁 __pycache__sample
│   └── 📁 __pycache__sample
```