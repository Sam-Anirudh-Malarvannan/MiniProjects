import random

print("******** Hi! WELCOMEE TO THE NUMBER GUESSING GAME ********")
print("********* You Have 7 chances to guess the number **********")

low = int(input("Enter the LowerBound : "))
high = int(input("Enter the UpperBound : "))

print(f"\nYou have 7 chances to guess the number between {low} and {high}.")

number = random.randint(low,high)
chances = 7
guessCount = 0

while guessCount < chances:
    guessCount += 1
    guess = int(input("Enter Your Guess : "))

    if guess == number:
        print(f"Correct! The Number Guessed is {number}. You Guessed it in {guessCount} chances.")
        break

    elif guessCount >= chances and guess != number:
        print(f'Sorry! The Number was {number}. Better Luck Next Time')

    elif guess < number:
        print("Too low! Try Again with a Higher Number")

    elif guess > number:
        print("Too high! Try Again with a Lower Number")


