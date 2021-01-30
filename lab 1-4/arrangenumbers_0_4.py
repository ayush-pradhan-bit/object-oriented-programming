# -*- coding: utf-8 -*-
"""
lab2 -  arrangenumbers_0_4.py
Task:
-A random list of 3x3 is provided
-user provides a value to swap
-once the random list is equal to check list user have to input value
-prints "Good work" once match is found
Created on Sat Jan 23 23:15:55 2021

@author: Ayush Pradhan
import random- Generating Random Numbers in a 3x3 list
"""
import random

# checks if the list matches the tuple
def isReady(n, check):
    return n == list(check)

# user inputs the value and swap is done
def move(n):
    wronginput= True           
    while wronginput:
            try:
                numberInput = input('number to move:')
                inputIndex = n.index(numberInput)
                emptyIndex = n.index('_')
                wronginput = False
                n[inputIndex],n[emptyIndex]=n[emptyIndex],n[inputIndex]
                break
            except ValueError:
                print('enter an integer btw 1 and 8')
# checks if order is solvable and returns a result

def isSolvable(n):
     inversions = 0
     for i in range(9):
        for j in range (1,9):
            if n[i] != '_' and n[j] != '_' and n[i] > n[j]:
                inversions += 1
            
     return inversions % 2 == 0
         
# we define the shuffle function
def shuffle(n):
    for i in range(random.randint(2, 10)):
        firstRandom = random.randint(0, 8)
        secondRandom = random.randint(0, 8)
        n[firstRandom], n[secondRandom] = n[secondRandom], n[firstRandom]

#program to give the list in 3x3 order
def printBoard(n):
    listIndex = 0
    for i in range(3):
        for j in range(3):
            if (j + 1) % 3 == 0:
                print(n[listIndex], end='\n')
            else:
                print(n[listIndex], sep=' ', end=' ')
            listIndex += 1
    print('')


def create():
    createdList = []
    for i in range(1, 9):
        createdList.append(str(i))
    createdList.append('_')
    return createdList


def main():
    # create a list of numbers, shuffle the order and add an empty string to the end
    n = create()
    check = tuple(n)
    # preparation loop
    while True:
        shuffle(n)
        if isSolvable(n):
            break
    print('8 puzzle - arrange the numbers by swapping them with the empty place')
    # the main loop
    while True:
        printBoard(n)
        if isReady(n, check):
            print('Good work!')
            break
        else:
            move(n)


if __name__ == '__main__':
    main()