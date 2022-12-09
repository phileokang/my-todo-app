FILEPATH = "todos.txt"

def get_todos(filepath=FILEPATH):
    """ Read the to-do items
    in the text file.
    """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines() #file.close() there's no need to close using with method
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list in the text file. """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


if __name__ == "__main__": #__name__ refers to arguments within the same code. __main__ refers to the NAME of the code. This is mainly for testing codes only
    print ("Hello")
    print(get_todos())

    