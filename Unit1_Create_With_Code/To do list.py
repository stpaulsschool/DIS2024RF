tasks = []
answer = ("")
while answer != "4":
    answer = input("Type 1 for adding to list / Type 2 for displaying list / Type 3 to remove from list / Type 4 for ending script ")
    if answer == "1":
        listItem = input("What do you want to add to the list? ")
        tasks.append(listItem)
    elif answer == "2":
        print(tasks)
    elif answer == "3":
        remove1 = int(input("What number is the item you want to remove?"))
        del tasks[remove1-1]
    elif answer == "4":
        print("Thank you, goodbye")
    else:
        print("Invalid answer")