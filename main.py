import argparse
import json
import os

TASKS_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def add_task(task):
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {task}")


def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")


def remove_task(index):
    tasks = load_tasks()
    if 1 <= index <= len(tasks):
        removed_task = tasks.pop(index - 1)
        save_tasks(tasks)
        print(f"Removed task: {removed_task}")
    else:
        print("Invalid task number.")


def main():
    parser = argparse.ArgumentParser(description="Simple To-Do List CLI Tool")
    parser.add_argument("-a", "--add", metavar="TASK", type=str, help="Add a new task")
    parser.add_argument("-l", "--list", action="store_true", help="List all tasks")
    parser.add_argument("-r", "--remove", metavar="INDEX", type=int, help="Remove a task by index")

    args = parser.parse_args()

    if args.add:
        add_task(args.add)
    elif args.list:
        list_tasks()
    elif args.remove:
        remove_task(args.remove)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
