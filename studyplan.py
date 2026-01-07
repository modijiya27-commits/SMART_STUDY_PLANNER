tasks = []

def add_task():
    subject = input("Enter subject/task name: ")
    days_left = int(input("Days left for deadline: "))
    difficulty = input("Difficulty (Easy / Medium / Hard): ").lower()

    if difficulty == "easy":
        diff_score = 11
    elif difficulty == "medium":
        diff_score = 2
    elif difficulty == "hard":
        diff_score = 3
    else:
        print("Invalid difficulty! Default set to Medium.")
        diff_score = 2

    priority = (diff_score * 2) + (10 - days_left)

    task = {
        "subject": subject,
        "days_left": days_left,
        "difficulty": difficulty,
        "priority": priority
    }

    tasks.append(task)
    print("Task added successfully!\n")

def show_plan():
    if not tasks:
        print("No tasks available.")
        return

    sorted_tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)

    print("\nToday's Study Plan (High → Low Priority)")
    for i, task in enumerate(sorted_tasks, start=1):
        print(f"{i}. {task['subject']} | Days Left: {task['days_left']} | Difficulty: {task['difficulty']}")

while True:
    print("\n--- SMART STUDY PLANNER ---")
    print("1. Add Task")
    print("2. View Study Plan")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_plan()
    elif choice == "3":
        print("Exiting Planner. Stay consistent!")
        break
    else:
        print("Invalid choice. Try again.")
