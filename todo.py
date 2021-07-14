tasks = []


print("Welcome to Zac's TO-D0 app!")
print("Please pick from the folowing items.")

def list_tasks():
    for item in tasks:
        dict_name = item["Task name"]
        pri_name = item["Task Priority"]
        print(f"You need to {dict_name}!! It's priority is {pri_name}!")

while True:
    menue_item = input("Press 1 to add a task... \nPress 2 to delete a task... \nPress 3 to view all tasks... \nPress q to quit...  >  ")
    
    

    if menue_item == "1":
        name = input("Enter the name of your task.  >  ")
        priority = input("Enter the priority of your task (High, Medium, Low). >  ")

        task = {"Task name": name, "Task Priority": priority}
        tasks.append(task)
        list_tasks()


    elif menue_item == "q":
        break
    
    elif menue_item == "3":
        list_tasks() 

    elif menue_item == "2":
        del_task = int(input("What is the number of the task you would like to delete? (1, 2, 3, 4)... > ")) - 1
        del tasks[del_task]

    elif menue_item != "q" and menue_item != "1" and menue_item != "2" and menue_item != "3":
        print("YOU MUST HAVE TASKS!!!!")


print(tasks)
