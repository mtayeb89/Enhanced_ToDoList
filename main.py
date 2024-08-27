import json  # For saving and loading tasks from a file

tasks = []

# Function to load tasks from a file
def loadTasks():
    try:
        with open("tasks.json", "r") as file:
            global tasks
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

# Function to save tasks to a file
def saveTasks():
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

# Function to add a task to the list with priority and due date
def addTask():
    task = input("Please enter a task: ")
    priority = input("Enter priority (High, Medium, Low): ")
    due_date = input("Enter due date (YYYY-MM-DD): ")
    tasks.append({"task": task, "priority": priority, "due_date": due_date, "completed": False})
    saveTasks()
    print(f"Task '{task}' added to the list.")

# Function to list all tasks with their details
def listTasks():
    if not tasks:
        print("There are no tasks currently.")
    else:
        print("Current Tasks:")
        for index, task in enumerate(tasks):
            status = "Completed" if task["completed"] else "Pending"
            print(f"Task #{index}. {task['task']} [Priority: {task['priority']}, Due: {task['due_date']}, Status: {status}]")

# Function to delete a task
def deleteTask():
    listTasks()
    try:
        taskToDelete = int(input("Enter the # to delete: "))
        if 0 <= taskToDelete < len(tasks):
            tasks.pop(taskToDelete)
            saveTasks()
            print(f"Task {taskToDelete} has been removed.")
        else:
            print(f"Task #{taskToDelete} was not found.")
    except:
        print("Invalid input.")

# Function to mark a task as completed
def completeTask():
    listTasks()
    try:
        taskToComplete = int(input("Enter the # to mark as completed: "))
        if 0 <= taskToComplete < len(tasks):
            tasks[taskToComplete]["completed"] = True
            saveTasks()
            print(f"Task {taskToComplete} has been marked as completed.")
        else:
            print(f"Task #{taskToComplete} was not found.")
    except:
        print("Invalid input.")

if __name__ == "__main__":
    loadTasks()
    print("Welcome to the to-do list app :)")
    while True:
        print("\n")
        print("Please select one of the following options")
        print("------------------------------------------")
        print("1. Add a new task")
        print("2. Delete a task")
        print("3. List tasks")
        print("4. Mark a task as completed")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            addTask()
        elif choice == "2":
            deleteTask()
        elif choice == "3":
            listTasks()
        elif choice == "4":
            completeTask()
        elif choice == "5":
            break
        else:
            print("Invalid input. Please try again.")

    print("Goodbye 👋👋")
