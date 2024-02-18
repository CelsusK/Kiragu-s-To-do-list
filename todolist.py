# Define the to-do list
todo_list = []

# Function to add a task
def add_task(task):
    todo_list.append(task)
    print(f"Task added: {task}")

# Function to view all tasks
def view_tasks():
    if not todo_list:
        print("Your to-do list is empty.")
    else:
        for i, task in enumerate(todo_list, start=1):
            print(f"{i}. {task}")

# Function to delete a task
def delete_task(task_number):
    if 0 < task_number <= len(todo_list):
        removed_task = todo_list.pop(task_number - 1)
        print(f"Task removed: {removed_task}")
    else:
        print("Invalid task number. Please try again.")

# Example usage
add_task("Read a book")
add_task("Write a blog post")
add_task("Go for a run")

print("\nCurrent To-Do List:")
view_tasks()

delete_task(2)

print("\nUpdated To-Do List:")
view_tasks()