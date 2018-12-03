# Write a program that is played between a human and a computer where the computer chooses a random number the human
# is supposed to guess.

import random  # import random.randint

guesses = 0  # variable guesses is given the value of zero

print("Hello, welcome to my Number Guessing Game.")  # outputs welcome and title

Guess = []  # Guess become variable for list

number = random.randint(1, 100)  # number is given value of random.randint(1, 100)

while guesses < 1:  # while guesses < 1 keep running this loop
    print("I'm thinking of a number between 1 and 100. Please guess the number:")  # outputs and asks for user guess
    guess = input()  # variable guess is user input
    guess = int(guess)  # variable guess is user input converted to integer
    Guess.append(guess)  # add user guesses to list
    if guess < number:  # if user guess less than number run loop again
        print("That's too low -- guess again:")  # outputs informs user guess was too low
    if guess > number:  # if user guess bigger than number run loop again
        print("That's too high -- guess again:")  # output informs user guess was too high
    if guess == number:  # if user guess was number then
        break  # break out of the loop
print("Good job -- The number was", guess)  # output informs user number was guess and shows number
print("Here's all the guesses you made before you answered correctly:", Guess)  # outputs list of all user's attempts
