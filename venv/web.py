'''
This is the first web aplication in python
run  streamlit run web.py
'''
from streamlit import session_state

from functions import get_todos, write_todos
import streamlit as st

todos = get_todos()

#session_state es como un dictionary, con parese clave valor


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    write_todos(todos)
    return



st.title("My web todo App")
st.subheader("This is my todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="",placeholder="Add new to_do",
              on_change=add_todo,key='new_todo')
print ("Hello")
print (session_state)
st.session_state

'''
'''