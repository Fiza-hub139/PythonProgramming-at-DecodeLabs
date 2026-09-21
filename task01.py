print("--------------Welcome to To-do List---------")
tasks = []

while True:
    print("\n--- To-Do List ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Choose an option (1-3): ")

    if choice == "1":
        # Add a new task to the list using append()
        new_task = input("Enter task (e.g., Finish Python assignment): ")
        tasks.append(new_task)
        print(f"'{new_task}' added!")

    elif choice == "2":
        # Print all tasks using a loop
        if not tasks:
            print("Your task list is empty.")
        else:
            print("\nYour Current Tasks:")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice, please select 1, 2, or 3.")

print("-------------Program End-------------------------")