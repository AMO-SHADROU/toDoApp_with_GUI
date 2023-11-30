import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_to_add = st.session_state["new_todo"] + "\n"
    todos.append(todo_to_add)
    functions.write_todos(todos)


st.title("My Todo App")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new todo...", on_change=add_todo, key="new_todo")
