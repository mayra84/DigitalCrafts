tasks = []


def add_task(title, priority):
    task = {
        'title': title,
        'priority': priority}
    tasks.append(task)
    print(tasks)
    menu()
    # Without menu(), the tasks are not stored. Why?
# How to i enable several inputs

    
def delete_task(wishful_deletion):
    del wishful_deletion

def view_tasks():
    pass

def quit(): 
    pass

def menu():
    print('Press 1 to add task: ')
    print('Press 2 to delete task: ')
    print('Press 3 to view all tasks: ')
    print('Press q to quit: ')
    choice = input()


    if choice == '1':
        title = input('Enter the name of the task: ')
        priority = input('Enter the priority of the task\n(choose one of the following: high, medium, low): ')
        priority_choices = ['high', 'medium', 'low']
        if priority not in priority_choices:
            print('That is not a priority choice. Try again!')
            
        # How do I loop back to choices?
        add_task(title, priority)
        menu()

    elif choice == '2':
        wishful_deletion = input('Enter the name of the task you wish to delete: ')
        # DON'T NEED A FOR LOOP AFTER ALL LOL 
        for i in range(len(tasks)):
            if wishful_deletion not in tasks[i]['title']:
                print('That task does not exist! Try again.')
            delete_task(wishful_deletion)
            menu()


    elif choice == '3':
        view_tasks()

    elif choice == 'q':
        quit()

    else:
        print('That is not an option. Try again!')
        # How to loop back to menu?


menu()
