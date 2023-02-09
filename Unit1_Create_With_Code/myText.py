with open("myTextfile.txt", "r") as file:
    print(file.read())

list = ["a", "b", "c"]

for item in list:
    with open("myTextfile.txt", "a") as file:
        file.write(item)
        file.write("\n")

with open("myTextfile2.txt", "r") as file:
    print(file.read())