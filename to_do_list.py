import os
import json

''' Project: Create a basic to-do list where users can add, delete, and view tasks'''

# Load tasks from a file if it exists
tasks = []
if os.path.exists("tasks.txt"):
    with open("tasks.txt", "r") as file:
        tasks = json.load(file)
        print("Using your Previous Tasks")
else:
    print("No previous tasks found. Starting with an empty to-do list.")

choice = 0
while choice != 6:
    print("------------------------------------------------------------------------------------")
    if tasks:  # Check if the list is not empty
        print(f"Your current To Do List: {tasks}")
    else:
        print("Your To Do List is empty.")
    print("1. Add a Task")
    print("2. Insert a Task in between the To Do List")
    print("3. Delete a Task with its Number")
    print("4. Delete a Task with its Name") 
    print("5. Delete the whole To Do List")
    print("6. Save and Exit")
    print()
    try:
        choice = int(input("Enter your Choice: \n"))
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
        continue

    if choice == 1:
        task1 = input("Enter your Task: ")
        tasks.append(task1)
        print(f"Your inserted task is: {task1}")
        print()
    elif choice == 2:
        task2 = input("Enter your Task to be inserted: ")
        try:
            num = int(input("Enter the Task Number where to be inserted: "))
            tasks.insert(num - 1, task2)
            print(f"Your inserted task is: {task2}")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
        print()
    elif choice == 3:
        try:
            num_del = int(input("Enter the task number to be deleted: "))
            if 0 < num_del <= len(tasks):
                removed_element = tasks.pop(num_del - 1)
                print(f"The deleted task is: {removed_element}")
            else:
                print()
                print("INVALID TASK NUMBER.")
        except ValueError:
            print("Invalid input. Please enter a valid task number.")
        print()
    elif choice == 4:
        task_del = input("Enter the specific task correctly (will remove its first occurrence in the To Do List.): ")
        if task_del in tasks:
            tasks.remove(task_del)
            print(f"The deleted task is: {task_del}")
        else:
            print("Task not found in the list.")
        print()
    elif choice == 5:
        tasks.clear()
        print("All tasks have been deleted.")
    elif choice == 6:
        # Save the tasks to a file before exiting
        with open("tasks.txt", "w") as file:
            json.dump(tasks, file)
        print("Tasks saved successfully. Exiting...")
    else:
        print("Invalid choice. Please try again.")

print()
print("----------------------------------------------------------------------------------------")
print("Thank you for using our To Do List.")
print("----------------------------------------------------------------------------------------")
