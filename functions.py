FILEPATH = "toDos.txt"


def get_todos():
    with open(file=FILEPATH, mode='r') as file:
        todos_local = file.readlines()
        return todos_local


def write_todos(todos_local):
    with open(file=FILEPATH, mode='w') as file:
        file.writelines(todos_local)
