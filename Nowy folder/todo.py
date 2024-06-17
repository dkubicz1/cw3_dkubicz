tasks = []


def add_task(task):
    tasks.append(task)
    return task


def get_tasks():
    return tasks


if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python todo.py <command> [task]")
        sys.exit(1)

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) != 3:
            print("Usage: python todo.py add <task>")
            sys.exit(1)
        task = sys.argv[2]
        add_task(task)
        print(f"Added task: {task}")
    elif command == "list":
        for task in get_tasks():
            print(task)
    else:
        print("Unknown command. Use 'add' to add a task or 'list' to list all tasks.")
