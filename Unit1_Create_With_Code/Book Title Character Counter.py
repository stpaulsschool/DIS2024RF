print("Welcome to my little book title counter..." )
yn = input("Would you like me to count the length of the book's title? ")
spaceCount = 0

while yn.lower() != "no":
    if yn.lower() == "yes":
        bookTitle = input("What is the title of your book? ")
        for i in range (len(bookTitle)):
            bookTitleL = bookTitle[i]
            if bookTitleL == " ":
                spaceCount = spaceCount+1


        stringLength = len(bookTitle)
        stringLengthWithoutSpaces = stringLength-spaceCount
        print("Your Book Title " + "'" + bookTitle + "'" + " has " + str(stringLength) + " characters (including spaces), or " + str(stringLengthWithoutSpaces) + " characters (without spaces)... ")
        spaceCount = 0
        yn = input("Would you like to try again? ")

    else:
        print("Sorry I do not understand ")

print("Thank you, goodbye! ")