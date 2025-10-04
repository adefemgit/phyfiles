


to_do_list = []


while True:
    print("\n1. Add task \n2 View task \n3 Remove task \n4 View task \n5 Exit")
    choice = int(input("enter your choice please(1-4)"))

    if choice == 1:
        task = input("enter your task: ")
        to_do_list.append(task)
        print(f"Task added: {task}")

    elif choice == 2:
        if to_do_list:
            print("\nto_do_list")
        for i, task in enumerate(to_do_list, 1):
            print(f" {i}. {to_do_list}")

        else:
            print("No tasks added")

    elif choice == 3:
        index = int(input("enter the number that needs to be removed: "))
        delete = to_do_list.pop(index - 1)
        print(f"Task removed: {delete}")

    elif choice == 4:
        print(to_do_list)

    else:
        print("Goodbye")
        exit()




