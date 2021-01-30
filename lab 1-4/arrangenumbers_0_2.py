# -*- coding: utf-8 -*-
"""
Lab 2 - arrangenumbers_0_2.py
Task:
-Enter a List of Numbers
- create a tuple containing values
-rearrange the values in correct ascending order
-Print the result

Created on Sun Jan 17 08:10:31 2021

@author: Ayush
"""
print ('8 puzzle - arrange the numbers by swapping them with the empty place')
n =['4', '7', '2', '6', '8', '3', '5', '_', '1']
print("The number to be arranged", n) #these are the values entered
corr = ['1', '2', '3', '4', '5', '6', '7', '8', '_']
print ("The Correct Order is", corr) #entered value should be equal to the correct vales
# here we use the swap function for 8 different times
for i in range (8):
    user_inp = input (f'{i+1}. position to swap :') # the formatting function helps to swap position 8 times
    position1 = n.index(user_inp)
    position2 = n.index('_')
    n[position1], n[position2] = n[position2], n[position1]
    print (n)
# we check the output    
result = True
for i in range (len(n)):
    if n[i] != corr[i]:
        output = False
# the result of the output is given         
if result:
    match = True
else:
    match = False
print ("The numbers are in correct order is", match)

    



