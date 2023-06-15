import os

# Default config values
FOLDER_ICON = "📁"  # folder icon
FILE_ICON = "📄"  # file icon
INDENT = "│  "  # general indent (from left side)
ENTRY_INDENT = "├──"  # entry indent
LAST_ENTRY_INDENT = "└──"  # the last entry indent
SHOW_HIDDEN: bool = False  # show hidden folders (.git, .idea, etc)

# Current directory path
ROOT_PATH: str = os.path.dirname(os.path.realpath(__file__))


def print_tree(root_path: str = ROOT_PATH,
               folder: str = FOLDER_ICON,
               file: str = FILE_ICON,
               ind: str = INDENT,
               entry_ind: str = ENTRY_INDENT,
               last_ind: str = LAST_ENTRY_INDENT,
               show_hidden: bool = SHOW_HIDDEN) -> None:
    """
    Prints a tree. Recursive.

    :param root_path:   root path, defaults to current dir path
    :param folder:      folder icon
    :param file:        file icon
    :param ind:         general indent (from left side)
    :param entry_ind:   entry indent
    :param last_ind:    the last entry indent
    :param show_hidden: show hidden folders (.git, .idea, etc)
    """
    entries: list[os.DirEntry] = list(os.scandir(root_path))

    for i, entry in enumerate(entries):

        # If the entry is last in folder: replace indent type.
        if i == len(entries) - 1:
            entry_ind = last_ind

        if entry.is_file():
            # If the entry is a file: print it and go on.
            print(f"{ind} {entry_ind} {file} {entry.name}")

        elif not entry.name.startswith(".") or show_hidden:
            # If the entry is a folder: print it ...
            print(f"{ind} {entry_ind} {folder} {entry.name}")
            # ... and call of print_tree() for this folder.
            print_tree(
                root_path=f"{root_path}/{entry.name}",
                ind=(ind + " " + INDENT)
            )


if __name__ == "__main__":
    # First string (print root directory)
    print(f"{ENTRY_INDENT} {FOLDER_ICON} {os.path.basename(ROOT_PATH)}")

    print_tree()
