# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:43:12 2021

@author: user
"""


import random

def isReady(numbers, check):
    return numbers == list(check)


def move(numbers):
    wronginput= True           
    while wronginput:
            try:
                numberInput = input('number to move:')
                inputIndex = numbers.index(numberInput)
                emptyIndex = numbers.index('_')
                printBoard(numbers)
                wronginput = False
                numbers[inputIndex],numbers[emptyIndex]=numbers[emptyIndex],numbers[inputIndex]
                break
            except ValueError:
                print('enter an integer btw 1 and 8')


def isSolvable(numbers):
     inversions = 0
     for i in range(9):
        for j in range (1,9):
            if numbers[i] != '_' and numbers[j] != '_' and numbers[i] > numbers[j]:
                inversions += 1
            
     if inversions % 2 != 0:
         shuffle(numbers)

def shuffle(numbers):
    for i in range(random.randint(2, 10)):
        firstRandom = random.randint(0, 8)
        secondRandom = random.randint(0, 8)
        while firstRandom == secondRandom:  # avoid swapping of value with itself
            secondRandom = random.randint(0, 8)
        #swap(firstRandom, secondRandom)


def printBoard(numbers):
    listIndex = 0
    for i in range(3):
        for j in range(3):
            if (j + 1) % 3 == 0:
                print(numbers[listIndex], end='\n')
            else:
                print(numbers[listIndex], sep=' ', end=' ')
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
    numbers = create()
    check = tuple(numbers)
    # preparation loop
    while True:
        shuffle(numbers)
        if isSolvable(numbers):
            break
    print('8 puzzle - arrange the numbers by swapping them with the empty place')
    # the main loop
    while True:
        printBoard(numbers)
        if isReady(numbers, check):
            print('Good work!')
            break
        else:
            move(numbers)


if __name__ == '__main__':
    main()
