from task_functions import *
def main():
    FILENAME = "tasks.txt"

    while True:
        print("\n=== To-Do List Manager ===")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Mark as Completed")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            list_tasks(FILENAME)

        elif choice == '2':
            desc = input("Task description: ")
            add_task(FILENAME, desc)
            print("Task added!")

        elif choice == '3':
            task_id = int(input("Task number: "))
            complete_task(FILENAME, task_id)

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


if __name__ == '__main__':
    main()
