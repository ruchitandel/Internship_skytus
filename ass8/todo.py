tasks = []

while True:
    print("\n--- TODO LIST MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter your choice: ")

    # ---- Add Task ----
    if choice == "1":
        task = input("Enter task to add: ")
        tasks.append(task)
        print("Task added")

    # ---- View Tasks ----
    elif choice == "2":
        if len(tasks) == 0:
            print("No task available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    # ---- Delete Task ----
    elif choice == "3":
        if len(tasks) == 0:
            print("No task available")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
                
            delete_index = int(input("Enter task number to delete: "))
            if 1 <= delete_index <= len(tasks):
                removed_task = tasks.pop(delete_index - 1)
                print(f"'{removed_task}' deleted")
            else:
                print("Invalid task number")

    # ---- Exit ----
    elif choice == "4":
        print("Exiting!")
        break

    else:
        print("Invalid choice!")
