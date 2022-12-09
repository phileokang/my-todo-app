#Run in terminal: pip freeze > requirements.txt

import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n" #reference key is 'new_todo'
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("Coolio!")
st.write("Checking write function")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index) #to remove in text file
        functions.write_todos(todos)
        del st.session_state[todo] #to remove on session
        st.experimental_rerun()

st.text_input(label="Input", placeholder="Enter a todo...", on_change=add_todo, key="new_todo")

st.session_state