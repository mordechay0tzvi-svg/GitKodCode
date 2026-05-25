def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            file = f.readlines()
            tasks = []
            for f in file:
                id = f.split(" ")[0]
                status = f.split(" ")[1]
                description = f.split(" ")[2]
                id = id.split(":")[1]
                status = status.split(":")[1]
                description = description.split(":")[1]
                task = {"id":id, "status":status, "description":description}
                tasks.append(task)
            return tasks
    except FileNotFoundError:
        print("File not found")
        return

def save_tasks(filename, tasks):
    try:
        with open(filename, 'w') as f:
            for t in tasks:
                task = ""
                for k, v in t.items():
                    task += f"{k}:{v} "
                f.write(task + "\n")
    except Exception as e:
        print(f"Error {e}")

def add_task(filename, description):
    try:
        tasks = load_tasks(filename)
        if not tasks:
            last_id = 0
            tasks = []
        else:
            last_id = int(tasks[-1]["id"])
        tasks.append({"id": f"{last_id + 1}", "status":"pending", "description":description})
        save_tasks(filename, tasks)
    except Exception as e:
        print(f"Error {e}")

def complete_task(filename, task_id):
    try:
        tasks = load_tasks(filename)
        for task in tasks:
            if task["id"] == str(task_id):
                task["status"] = "done"
                save_tasks(filename, tasks)
                return
        print("task not found")
        return
    except Exception as e:
        print(f"Error {e}")

def list_tasks(filename):
    try:
        tasks = load_tasks(filename)
        if not tasks:
            print("no tasks yet")
            return
        for task in tasks:
            print(task)
    except Exception as e:
        print(f"Error {e}")

