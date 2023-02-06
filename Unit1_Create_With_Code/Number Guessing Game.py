import random
NOG = 1

print("Hello and welcome to my number guessing game!")
number = random.randint(1, 100)
print("I have randomly selected a number between 1->100")
print(number)

while NOG != 7:
    guess = int(input("guess " + str(NOG) + "/6, please enter your guess... "))
    if guess == number:
        print("You guessed it in " + str(NOG) + " guess/es!!!! ")
        quit()
    elif guess>number:
        print("Lower")
    elif guess<number:
        print("Higher")
    NOG = NOG+1

