import functions
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

while True:
    user_input = input('Type "add", "show", "edit", "complete" or "exit": \n').strip().lower()

    if user_input.startswith("add"):
        new_todo = input("Enter a new todo: ") + "\n"
        todos = functions.get_todos()
        todos.append(new_todo)
        functions.write_todos(todos)
    elif user_input.startswith("show"):
        todos = functions.get_todos()
        for index, todo in enumerate(todos):
            print(f'{index + 1}. {todo}', end="")
    elif user_input.startswith("edit"):
        try:
            todos = functions.get_todos()
            index = int(user_input[5:])
            todos[index - 1] = input("Enter a todo: ") + "\n"
            functions.write_todos(todos)
        except ValueError:
            print("Invalid input. You must enter an integer after edit")
            continue
        except IndexError:
            print("Out of range.")
            continue
    elif user_input.startswith("complete"):
        try:
            todos = functions.get_todos()

            index = int(user_input[9:])
            popped_todo = todos.pop(index - 1)

            functions.write_todos(todos)

            print(f"Todo {popped_todo.strip("\n")} was removed from the file.")

        except IndexError:
            print("Out of range.")
            continue
    elif user_input.startswith("exit"):
        break
    else:
        print("Invalid input!!!")

print("Goodbye!")
