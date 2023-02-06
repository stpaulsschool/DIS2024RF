word = input("What is your word? ")
list = []
for i, v in enumerate(word):
    if v.isupper():
        list.append(i)
print(list)

