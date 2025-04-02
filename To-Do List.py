tasks = []

while True:
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")
    
    print("\nOptions: [1] Add Task  [2] Remove Task  [3] Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")
    
    elif choice == "2":
        try:
            task_num = int(input("Enter task number to remove: "))
            removed = tasks.pop(task_num - 1)
            print(f"Task '{removed}' removed!")
        except (ValueError, IndexError):
            print("Invalid task number.")
    
    elif choice == "3":
        print("Goodbye!")
        break
    
    else:
        print("Invalid choice, try again.")
