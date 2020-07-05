#!/usr/bin/env python3

# Desc: Guess the number game
# Lang: python3
# Author: naildownx
# 07/05/20

import random
import os

tryAgain = 'y'

while tryAgain == 'y':

    os.system('cls' if os.name == 'nt' else 'clear')

    actualNumber = random.randint(1, 100)

    print('Welcome to my number guessing game!|')
    print('------------------------------------')

    print('Instructions:\nYou will guess a number from between 1-100 and will be given\nclues to go higher or lower.\n\n')

    count = 1

    while True:
        while True:
            userGuess = input('Try guessing the number: ')

            try:
                valueTest = int(userGuess)
                break
            except ValueError:
                try:
                    valueTest = float(userGuess)
                    print('')
                except ValueError:
                    print('')

        userGuess = int(userGuess)
        if userGuess < actualNumber:
            print('The number is greater than ' + str(userGuess) + '!\n')
        elif userGuess > actualNumber:
            print('The number is less than ' + str(userGuess) + '!\n')
        else:
            print('\n\n.-~*´¨¯¨`*·~-.,-( S U C C E S S )-,.-~*´¨¯¨`*·~-.¸··.')
            print('\n\tYoU GuEsSeD ThE SeCrEt NuMbEr!\n\tThe secret number was ' + str(actualNumber) + '.')
            print('\tNumber of guesses: {}\n'.format(count))
            tryAgain = input('Would you like to play again? <y/N> ')
            break
        count += 1

print('\n\nThanks For Playing My Number Guessing Game! Play again soon!!!!\n\n')
