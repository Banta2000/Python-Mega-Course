import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    


st.title('My Todo App')
st.subheader('Here are the things I need to do:')
# st.write("Written by Manuel Altermatt")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label = "Add new todo", placeholder="Add new todo", on_change=add_todo, key="new_todo")

