word = input("What is your word?(type 'q' to quit) ")
while word.lower() != "q":
    list = []
    for i, v in enumerate(word):
        if v.isupper():
            list.append(i)
    print("=" * 50)
    print("The indexes that were capital letters were: " + str(list))
    word = input("What is your word?(type 'q' to quit) ")
print("Thank you, goodbye!")
