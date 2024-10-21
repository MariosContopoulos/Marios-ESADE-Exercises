#Create empty list
todo_list=[]

def add_task(task):
    """
    This function adds a task in the todo_list

    Inputs: task
    """
    todo_list.append(task)


add_task("asdwasdfwsdfasdfasdfasdfasdfasdfasdfasdf")


def show_tasks():
    """
    This function prints all the tasks in the todo_list
    """
    if todo_list:
        print("Tasks to do:")
        for task in todo_list:
            print(f"{task}")
    else:
        print("No tasks in the list.")


show_tasks()

#OUTPUT
#Tasks to do:
#asdwasdfwsdfasdfasdfasdfasdfasdfasdfasdf