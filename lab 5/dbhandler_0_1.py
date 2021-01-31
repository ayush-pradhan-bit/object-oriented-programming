# -*- coding: utf-8 -*-
"""
sql3lite database example, https://docs.python.org/3/library/sqlite3.html
argparse tutorial https://docs.python.org/3/howto/argparse.html

Lab5- dbHandler_0_1.py
Description - ConnectionHandled uses provided sqliite database which contains tables and rounds.
              each rounds is used to toss the dices in a double-or-nothing game. It plays containing each
              choices user made (bets) and dices output when playinh a round in the game.
Author - Ayush Pradhan
"""
import os, argparse
import sqlite3
from sqlite3 import Error

class ConnectionHandler:
    '''simple and naive use of sqlite database'''
    def __init__(self, db):
       self.db = db
       self.connection = None


    def openConnection(self):
        try:        
            self.connection = sqlite3.connect(self.db)#open existing or creates a new
        except Error as error:
            print(error)
            
    def closeConnection(self):
        if self.connection:
           self.connection.close()
            
    def getData(self, query): 
        '''returns a list of tuples'''
        result = [] #fill this in and return it
        cursor = self.connection.cursor() # create cursor
        try:                        
           cursor.execute(query)
           result = cursor.fetchall()

        except Error as error:
           print(error)
        finally:
           cursor.close()
        return result
       
    def executeScript(self, scriptfile):
        with open("dicesDB.sql", 'r') as sql_file:
            sql_script = sql_file.read()
        self.openConnection()
        try:
            cursor = self.connection.cursor()
            cursor.executescript(sql_script)
            self.connection.commit() #saves the changes
            cursor.close()
        except Error as error:
            self.connection.rollback() #rolls back any changes to the database 
            print(error)
        finally:
            if self.connection:
                self.closeConnection()

def main(path):
    '''funcion to execute the progam, path db name and path to it'''
    c = ConnectionHandler('dicesDB.sqlite')
    c.executeScript('dicesDB.sql')
    c.openConnection()
    #open connection 
    if c.connection:
        print('connection is open')
        query_1 = 'SELECT * FROM rounds'
        query_2 = 'SELECT round_id, bet, result FROM plays'
        
        rounds = c.getData(query_1)
        plays = c.getData(query_2)
        
        for i in range(len(rounds)):
            print(" ")
            print(f"{i}: Initial pot: {rounds[i][1]}")
            print("bet   dice1   dice2")
            for j in range (len(plays)):
                if plays[j][0]== i:
                    digit1 = str(plays[j][2])[0]
                    digit2 = str(plays[j][2])[1]
                    print("{:<7d} {:7s} {:1s}".format(plays[j][1], digit1, digit2))
            print(f"Final pot:{rounds [i][2]}")
        c.closeConnection()
        

if __name__ == '__main__':
    path = 'dicesDB.sql' 
    #if user gives an argument 
    argparser = argparse.ArgumentParser() 
    argparser.add_argument('-i', '--initialize', default=False, required=False)
    args = argparser.parse_args()
    if bool(args.initialize):        
        scriptfile = os.getcwd()+ r'C:\Users\user\Desktop\oop\lab 5\dicesDB.sql'
        ConnectionHandler(path).executeScript(scriptfile)
        print(f'database {path} initialized')
    main(path)
