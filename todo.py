import json

def load_data():
    try:
        with open('task_manager.txt','r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_data_helper(tasks):
    with open('task_manager.txt', 'w') as file:
        json.dump(tasks, file)

def list_all_tasks(tasks):
    print("\n")
    print("*" * 70)
    for index, task in enumerate(tasks, start=1):
        print(f"{index}. {task['name']} ")
    print("\n")
    print("*" * 70)

def add_task(tasks):
    name = input("Enter task name: ")
    tasks.append({'name': name})
    save_data_helper(tasks)

def update_task(tasks):
    list_all_tasks(tasks)
    index = int(input("Enter the task number"))
    if 1 <= index <= len(tasks):
        name = input("Enter the new task")
        tasks[index-1] = {'name':name}
        save_data_helper(tasks)
    else:
        print("Invalid index selected")
def remove_task(tasks):
    list_all_tasks(tasks)
    index = int(input("Enter the video number to be deleted"))
    
    if 1<= index <= len(tasks):
        del tasks[index-1]
        save_data_helper(tasks)
    else:
        print("Invalid video index selected")


def main():
    tasks = load_data()
    while True:
        print("\n ToDo | choose an option")
        print("1. List all tasks")
        print("2. Add new task")
        print("3. Update task")
        print("4. Remove task")
        print("5. Exit app")
        choice = input("Enter your choice")

        match choice:
            case '1':
                list_all_tasks(tasks)
            case '2':
                add_task(tasks)
            case '3':
                update_task(tasks)
            case '4':
                remove_task(tasks)
            case '5':
                break
            case _:
                print("Invalid Choice")

if __name__ == "__main__":
    main()