

FILEPATH = "venv/todos.txt"

def get_todos(filepath=FILEPATH):
    """Read a text file an return the list of to-do item."""
    with open(filepath,'r') as file:
        to_dos = file.readlines()
    return to_dos

def write_todos(todos_arg, filepath=FILEPATH):
    """write the to-do items lis in the text file"""
    with open(filepath,'w') as file:
        file.writelines(todos_arg)
        print ("escribiendo en los ficheros")
        print (todos_arg)
    return

if __name__ == "__main__":
    print("Hello from ...")
    print(get_todos())
