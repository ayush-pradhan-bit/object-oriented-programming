# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 13:11:01 2021

@author: user
"""


import random


# swap function
def swap(first, second):
   n[first], n[second] = n[second], n[first]


# shuffle function
def shuffle():
    for i in range(random.randint(2, 10)):
        firstRandom = random.randint(0, 8)
        secondRandom = random.randint(0, 8)
        while firstRandom == secondRandom:  # prevents that the swap function doesnt swap
            secondRandom = random.randint(0, 8)  # a number with itself
        #swap(firstRandom, secondRandom)


# solvability detection function
def solvability():
    inversions = 0
    for i in range(9):
        for j in range (1,9):
            if n[i] != '_' and n[j] != '_' and n[i] > n[j]:
                inversions += 1
            
    if inversions % 2 != 0:
        displayPattern(n)
        print("The current number combination is not solvable. I will shuffle them again.\n")
        shuffle()
        solvability()
    else:
        print("Have fun with the game!\n")
        displayPattern(n)


# displays the lists in a 3x3 pattern
def displayPattern(list):
    listIndex = 0
    for i in range(3):
        for j in range(3):
            if (j + 1) % 3 == 0:
                print(list[listIndex], end='\n')
            else:
                print(list[listIndex], sep=' ', end=' ')
            listIndex += 1
    print('')


# setup
print("Welcome to the 8-puzzle Arrange Numbers Game!")
n = ['4', '2', '1', '3', '5', '6', '_', '8', '7']
for i in range (9):
    n.append
print (n)

corr = ('1', '2', '3', '4', '5', '6', '7', '8', '_')
print("Correct Order:")
displayPattern(corr)
shuffle()
solvability()
rounds = 1



# Game rounds
while n != list(corr):
    wronginput= True           
    while wronginput:
            try:
                choice = input('number to move:')
                position1 = n.index(choice)
                position2 = n.index('_')
                swap(position1, position2)
                displayPattern(n)
                wronginput = False
                rounds +=1
            except ValueError:
                print('enter an integer btw 1 and 8')


# Feedback
print("well done")