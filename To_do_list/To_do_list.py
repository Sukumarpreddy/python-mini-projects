todo_list = []

def show_tasks():
    if not todo_list:
        print("No tasks yet.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task}")

def add_task(task):
    todo_list.append(task)
    print("Task added.")

def delete_task(task):
    if 0< index <= len(todo_list):
        removed = todo_list.pop(index)
        print(f"Deleted: {removed}")
    else:
        print("Invalid task number")

while True :
    print("\n=== to- do List ===")
    print("1. veiw tasks")
    print("2. Add Task")
    print("3. deleted Task ")
    print("4. Exit")

    choice = input("choose an option (1-4) ")
    if choice == "1":
        show_tasks()
    elif choice  ==  "2":
        task = input("Enter task :")
        add_task(task)
    elif choice == "3":
        show_tasks()
        try:
            idx = int(input('Enter task  numbe to delete: '))
            delete_task(idx)
        except ValueError:
            print('please enter a valid number ')
    elif choice == "4":
        print('goodbye!')
        break 
    else :
        print("Invalid option.")