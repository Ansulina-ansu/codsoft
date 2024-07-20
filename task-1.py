tasks=[]

def addTask():
    task = input("enter the task to be added:")
    tasks.append(task)
    print(f"Task '{task}' is added in the list")

def deleteTask():
    task = input("enter the task to be deleted:")
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' is deleted in the list")  
    else:
        print(f"Task '{task}' not found in the list ")  
def listTasks():
    print("Tasks in the list")
    for index, task in enumerate(tasks,start=1):
        print(f"{index}. {task}")

while True:
    print("\n")
    print("*To Do List")
    print("1. Add a new task")
    print("2. Delete a existing task")
    print("3. List the tasks")
    print("4. Exit")
    
    choice = input("Enter your choice:")
    if(choice=="1"):
        addTask()        
    elif(choice=="2"):
        deleteTask()
    elif(choice=="3"):
        listTasks()
    elif(choice=="4"):
        break
    else:
      print("invalid choice.  please try again")

