# tudo

`TuDo` is a straightforward command-line tool for managing tasks. It allows you to add, list, and mark tasks as complete, storing them in a `tudo.json` file in the same directory. The name is a play on "to-do" and "tudo", the word for "everything" in portuguese.

It was made with a few goals in mind:
1. Be the **most barebones possible**, just a place to jot down tasks and mark them as completed without switching from the terminal. You can add and list tasks, and mark them as completed. That's it.
2. Be a **single Python file,** using only the Python standard library.
3. No classes, **just functions.**
4. Operate on a **human-readable, easily editable and portable file.** Currently that's JSON, with plans to include others in the future.

## Usage

To see only your pending tasks, run the script without any arguments:

```bash
python tudo.py
```

To view all tasks, including those that have been completed, use the `--list` or `-l` flag:

```bash
python tudo.py -l
```

To add a new task, use the `--add` or `-a` flag, followed by the task description:

```bash
python tudo.py --add "This is a new task"

# You can also use it without quotes. Anything after the flag will be joined into a string.

python tudo.py -a This is a new task
```

To mark one or more tasks as complete, use the `--check` or `-c` flag, followed by the ID(s) of the task(s).

```bash
# Mark task with ID 1 as complete
python tudo.py --check 1

# Mark tasks with IDs 2 and 3 as complete
python tudo.py --check 2 3
```

## Planned features

Based on the comments in the source code, the following features and improvements are planned:

* [ ] Implement a feature to automatically create a database file if one doesn't exist.
* [ ] Implement nested tasks.
* [ ] Add support for reading from external SQLite and YAML files.
* [ ] Implement the `--trim` functionality to permanently remove completed tasks and cleanup id numbers.
* [ ] Add a feature to export tasks to a Markdown file.
