import json
import argparse
import sys
from pathlib import Path

# TODO:
# - Criar o repo para esse projeto.
# - Pensar na arquitetura OOP.
# - Caso não exista uma database, oferecer de criar uma.
# - Ler SQLite externo.
# - Ler YAML externo



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
                    help="Remove all done tasks from database.")



def load_tasks():
        
    if Path("tudo.db").exists():
        print("Database existe em sqlite")

    elif Path("tudo.md").exists():
        print("Database existe em markdown")
        
    elif Path("tudo.json").exists():
        with open("tudo.json", "r", encoding="utf-8") as f:
            result = json.load(f)
        return result

    else:
        confirmation = input("Nenhuma database foi encontrada. Criar uma nova? y/n ")


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

def get_current_task_index(tasks: dict):
    return int(max(set(tasks.keys())))
                
def add_task(tasks: dict, content: list):
    description = " ".join(content)
    index = get_current_task_index(tasks) + 1

    tasks[str(index)] = {"done": False, "description": description}

    with open("tudo.json", "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)


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
    count = 1

    
    
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

    
if __name__ == "__main__":
    main()

