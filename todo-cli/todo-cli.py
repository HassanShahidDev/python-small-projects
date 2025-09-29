# todo-cli.py
tasks=[]
def show(): 
    if tasks: 
        print("\nTo-Do List:"); 
        [print(f"{i+1}. {t}") for i,t in enumerate(tasks)]
    else: print("To-Do List is empty!")

while True:
    print("\nOptions: add, remove, show, q")
    cmd=input("Enter command: ").lower()
    if cmd=='q': break
    elif cmd=='add': tasks.append(input("Enter task: "))
    elif cmd=='remove':
        show()
        try: tasks.pop(int(input("Enter number to remove: "))-1)
        except: print("Invalid input!")
    elif cmd=='show': show()
    else: print("Unknown command!")
