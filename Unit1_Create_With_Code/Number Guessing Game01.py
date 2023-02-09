import random
ynList = ["yes", "y", "no", "n"]
name = input("What is your name? ")
print("Hello " + name + " and welcome to my number guessing game!")
HighScore = 6

def getDifficulty():
    difficulty = input("")

    totalGuesses = None
    if difficulty == "1":
        totalGuesses = 10

    if difficulty == "2":
        totalGuesses = 6
    if difficulty == "3":
        totalGuesses = 4
    else:
        print("Sorry, I do not understand...")
    return totalGuesses

while True:
    NOG = 1
    number = random.randint(1, 100)
    print("I have randomly selected a number between 1->100...")
    print("What difficulty would you like to play?")
    print("Easy(1)")
    print("Medium(2)")
    print("Hard(3)")
    totalGuesses = getDifficulty()





    while NOG != totalGuesses+1:
        guess = int(input("This is guess " + str(NOG) + "/" + str(totalGuesses) + ", please enter your guess... "))
        if guess != number and NOG == totalGuesses:
            print("You ran out of guesses...")
            print("The correct number was " + str(number))
        elif guess == number and NOG == 1:
            print("WOW you guessed it first try, good job!!!")
            break
        elif guess == number:
            print("You guessed it in " + str(NOG) + " guesses!!!! ")
            break
        elif guess>number:
            print("Lower")
        elif guess<number:
            print("Higher")
        NOG = NOG+1

    if NOG < totalGuesses+1:
        if HighScore>NOG:
            HighScore = NOG
        print("HighScore (Number Of Guesses):" + str(HighScore))
    yn = input("Do you want to play again (type y/n) ")
    if yn.lower() == "n" or yn.lower() == "no":
        print("Thank you for playing, goodbye")
        quit()
    elif yn.lower() == "y" or yn.lower() == "yes":
        print("=" * 50)
        print("\n")
    else:
        while yn.lower() not in ynList:
            print("Sorry, I do not understand...")
            yn = input("Do you want to play again (type y/n) ")
        if yn.lower() == "n" or yn.lower() == "no":
            print("Thank you for playing, goodbye!")
            quit()
        elif yn.lower() == "y" or yn.lower() == "yes":
            print("=" * 50)
            print("\n")



