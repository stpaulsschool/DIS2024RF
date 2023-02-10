import random
ynList = ["yes", "y", "no", "n"]
name = input("What is your name? ")
print("Hello " + name + " and welcome to my number guessing game!")
HighScore = 6

while True:
    NOG = 1
    number = random.randint(1, 100)
    print("I have randomly selected a number between 1->100...")
    print("What difficulty would you like to play?")
    print("Easy(1)")
    print("Medium(2)")
    print("Hard(3)")
    difficulty = input()
    if difficulty == "1:
        totalGuesses =




    while NOG != 7:
        guess = int(input("This is guess " + str(NOG) + "/6, please enter your guess... "))
        if guess != number and NOG == 6:
            print("You ran out of guesses...")
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

    if NOG <7:
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



