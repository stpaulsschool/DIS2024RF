bookTitle = input("What is the title of the book? ").split()
length = len(bookTitle)
if length == 2:
    print("Studies suggest that because this book has two words in the title it is more likely to be successful.")
else:
    print("Studies suggest that this book is less likely to be successful, as your book is more likely to be successful if it has two words in the title.")

