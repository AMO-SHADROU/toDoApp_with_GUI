import PySimpleGUI as sG
import functions

# Add button
label = sG.Text("Type in a to-do: ")
input_box = sG.InputText(key="todo")
add_button = sG.Button("Add")

# Show todos
list_box = sG.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10))

edit_button = sG.Button("Edit")
complete_button = sG.Button("Complete")
exit_button = sG.Button("Exit")

window = sG.Window("To-Do App", layout=[[label],
                                        [input_box, add_button],
                                        [list_box, edit_button, complete_button],
                                        [exit_button]],
                   font=("Helvetica", 18))

while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            todo_to_edit = values["todos"][0]
            new_todo = values["todo"] + "\n"
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window["todos"].update(values=todos)
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sG.WIN_CLOSED:
            break

window.close()
