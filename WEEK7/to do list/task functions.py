def load_tasks(filename):
    try:
        with open(filename, 'r') as f:
            return f.readlines()
    except FileNotFoundError:
        print("File not found")
        return None

def save_tasks(filename, tasks):
    with open(filename, 'w') as f:
        f.write(tasks)
