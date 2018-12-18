# Write a program that is played between a human and a computer where the computer chooses a random number the human
# is supposed to guess.
# Version 2 update, with a better understanding of the language and how functions work I put everything in a function
import random


def guessGame(): # function created
    print("Hello, welcome to my Number Guessing Game.")
    guesses = 0  # variable guesses is given the value of zero
    Guess = []  # Guess become variable for list
    number = random.randint(1, 100)  # number is given value of random.randint with a range of random number from 1-100
    while guesses < 1:  # while guesses < 1 keep running this loop
        guess = input("I'm thinking of a number between 1 and 100. Please guess the number:")  # variable guess is user guess
        guess = int(guess)  # variable guess is user input converted to integer
        Guess.append(guess)  # add user guesses to list
        if guess < number:  # if user guess less than number run loop again
            print("That's too low -- guess again:")  # outputs informs user guess was too low
        elif guess > number:  # if user guess bigger than number run loop again
            print("That's too high -- guess again:")  # output informs user guess was too high
        elif guess == number:  # if user guess was number then
            print("Good job -- The number was", guess)  # output informs user number was guess and shows number
            print("Here's all the guesses you made before you answered correctly:", Guess) # outputs list of all user's attempts in a list
            break


guessGame()

