import random

name = input("What is your name? ")

print("Good Luck !!!", name)

words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

word = random.choice(words)

print("Guess the Characters : ")

Guesses = ''
turns = 12

while turns > 0:

    failed = 0

    for char in word:

        if char in Guesses:
            print(char, end= " ")

        else:
            print('_')
            failed += 1

    if failed == 0:
        print("You win!")
        print("The word is : ", word)
        print(f"You Have winned the Game in {(turns + 1) - turns} turns")
        break

    print()
    Guess = input("Guess the Characters : ")

    Guesses = Guesses + Guess

    if Guess not in word:
        turns -= 1
        print("Sorry, that's not a word")
        print("You Have", +turns, "More Guesses")

        if turns == 0:
            print("You loose")