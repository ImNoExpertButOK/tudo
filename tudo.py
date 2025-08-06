import json
import argparse
import sys
from pathlib import Path

parser = argparse.ArgumentParser(
    description="Meu to-do"
)

parser.add_argument("--add",
                    "-a",
                    help="Add a new task to list.",
                    type=str,
                    nargs="*")

parser.add_argument("--list",
                    "-l",
                    help="List all tasks, including completed.",
                    type=bool,
                    nargs="?",
                    default=False)

parser.add_argument("--check",
                    "-c",
                    help="Check task as done.",
                    type=int,
                    nargs="*")

parser.add_argument("--trim",
                    "-t",
                    nargs="?",
                    help="Remove all done tasks from database.")


def update_db(tasks: dict):
    with open("tudo.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


def read_db():
    with open("tudo.json", "r", encoding="utf-8") as f:
        result = json.load(f)
        return result

def load_tasks():
    '''
    Looks in the current folder for a database. If not found,
    offer the user the option to create a new one.
    '''
    if Path("tudo.json").exists():
        return read_db()
    else:
        answer = input("No database found. Do you wish to create a new one? y/n ")
        if answer == "y":
            tasks = {}
            tasks["1"] = {"done": False, "description": "This is a sample task."}
            update_db(tasks)
            print("New database created.")
            return read_db()
        else:
            print("No action performed")
            sys.exit(1)


def get_current_task_index(tasks: dict):
    return int(max(set(tasks.keys())))


def list_tasks(tasks: dict, short: bool):
    result = ""
    if short:
        for id, content in tasks.items():
            if not content["done"]:
                result = result + f"{id}.\t[ ] {content['description']} \n"
    else:
        for id, content in tasks.items():
            if not content["done"]:
                result = result + f"{id}.\t[ ] {content['description']}\n"
            if content["done"]:
                result = result + f"{id}.\t[x] {content['description']}\n"

    return result
    
                
def add_task(tasks: dict, content: list):
    description = " ".join(content)
    index = get_current_task_index(tasks) + 1
    tasks[str(index)] = {"done": False, "description": description}
    update_db(tasks)


def mark_completed(tasks: dict, id: int):
    id = str(id)
    try:
        if not tasks[id]["done"]:
            tasks[id]["done"] = True
            print(f"{id}. [x] {tasks[id]['description']}")
        else:
            print(f"Tarefa de id {id} já foi completada")
    except KeyError:
        print(f"Tarefa de id {id} não existe.")
        

def trim(tasks: dict):
    new_task_list = {}
    new_id = 1
    for id, value in tasks.items():
        if not tasks[id]["done"]:
            new_task_list[new_id] = tasks[id]
            new_id += 1
    return new_task_list
    
    
def export_markdown(tasks):
    pass


def main():
    args = parser.parse_args()
    tasks = load_tasks()

    if len(sys.argv) <= 1:        
        print(list_tasks(tasks, short=True))
        sys.exit(1)

    if args.list is None:
        print(list_tasks(tasks, short=False))

    if args.check:
        for index in args.check:
            mark_completed(tasks, index)
        with open("tudo.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4)

    if args.add:
        add_task(tasks, args.add)

    if args.trim is None:
        update_db(trim(tasks))

    
if __name__ == "__main__":
    main()

