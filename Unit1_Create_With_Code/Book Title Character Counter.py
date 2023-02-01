print("Welcome to my little book title counter..." )
spaceCount = 0
bookTitles = []
bookTitle = input("What is the title of your book? (Type 'q' to quit) ")

while bookTitle.lower() != "q":
        bookTitles.append(bookTitle.title())
        for i in range (len(bookTitle)):
            bookTitleL = bookTitle[i]
            if bookTitleL == " ":
                spaceCount = spaceCount+1
        stringLength = len(bookTitle)
        stringLengthWithoutSpaces = stringLength-spaceCount
        print("Your Book Title " + "'" + bookTitle + "'" + " has " + str(stringLength) + " characters (including spaces), or " + str(stringLengthWithoutSpaces) + " characters (without spaces)... ")
        spaceCount = 0
        bookTitle = input("What is the title of your book? (Type 'q' to quit) ")

print("Thank you, goodbye! ")
print(bookTitles)
print(50 * "=")
print("The books you checked were:")
for idx, bookTitle in enumerate(bookTitles):
    print(f"{idx+1}: {bookTitle}")
print(50 * "=")
