
"""
Lab 3 - arrangenumbers_0_3.py
Task :
-User is provided with a shuffled values in 3x3 order
-User then guesses the moves and tries to arrange the list
-Once the game ends a comment/feedback is provided.

Created on Sun Jan 17 17:04:26 2021

@author: Ayush Pradhan
"""
import random

# we define the swap function for the values entered
def swap(first, second):
   n[first], n[second] = n[second], n[first]


# we define the shuffle function
def shuffle():
    for i in range(random.randint(2, 10)):
        firstRandom = random.randint(0, 8)
        secondRandom = random.randint(0, 8)
        while firstRandom == secondRandom:  # avoid swapping of value with itself
            secondRandom = random.randint(0, 8)
        #swap(firstRandom, secondRandom)


# We define solvability function and apply the inversion within it
def solvability():
    inversions = 0
    for i in range(9):
        for j in range (1,9):
            if n[i] != '_' and n[j] != '_' and n[i] > n[j]:
                inversions += 1
            
    if inversions % 2 != 0:
        displayPattern(n)
        print("OPPs the current list seems unsolvable. I will shuffle them again.\n")
        shuffle()
        solvability()
    else:
        print("Enjoy the Game!!!\n")
        displayPattern(n)


# the list is displayed in 3x3 manner
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


# main body of the program
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



# program to run the game for user
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


# comment received to the user at the end of the game
print("well done")
   
