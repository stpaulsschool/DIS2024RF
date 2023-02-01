print("Welcome to my little book title word counter... ")

bookTitle = input("What is the title of the book? (Type 'q' to quit) ")

while bookTitle.lower() != "q":
    bookTitleS = bookTitle.split()
    length = len(bookTitleS)
    if length == 2:
        print("Studies suggest that because this book has two words in the title it is more likely to be successful.")
    elif length > 2:
        print("Studies suggest that this book is less likely to be successful, as your book is more likely to be successful if it has two words in the title, try to remove some words")
    elif length == 1:
        print("Studies suggest that this book is less likely to be successful, as your book is more likely to be successful if it has two words in the title, try to add a word")
    else:
        print("Please type a title...")
    bookTitle = input("What is the title of the book? (Type 'q' to quit) ")

