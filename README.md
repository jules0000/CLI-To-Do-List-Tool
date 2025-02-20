# CLI To-Do List Tool

A simple command-line tool for managing a to-do list using Python.

## Features
- Add tasks to the to-do list
- List all tasks
- Remove tasks by index
- Stores tasks in a JSON file

## Requirements
- Python 3.x

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/jules0000/cli-todo-tool.git
   cd cli-todo-tool
   ```
2. (Optional) Create a virtual environment:
   ```sh
   python -m venv .venv
   source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
   ```
3. Install dependencies (if any):
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the script with the following commands:

### Add a task
```sh
python main.py --add "Buy cat food"
```
Or use the shorthand:
```sh
python main.py -a "Buy cat food"
```

### List all tasks
```sh
python main.py --list
```
Or use the shorthand:
```sh
python main.py -l
```

### Remove a task by index
```sh
python main.py --remove 1
```
Or use the shorthand:
```sh
python main.py -r 1
```

## Notes
- Tasks are stored in `tasks.json`.


