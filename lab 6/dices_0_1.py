"""
lab6 - dices_0_1.py

Task:   - A dices game with 2 dices and a betting system.
        - A checklist is made to provide the desired result.
@author - Ayush Pradhan         

"""

import random 


class Dices:

    # Initializer and attributes
    def __init__(self, pot, number=2):
        self.__pot = pot
        self.__bet = 1  # default value is 1, so the while loop in main doesnt stop right away
        self.__number = number  # default value is 2, but can be changed
        self.__faces = [0] * self.__number

    # Properties 
    @property
    def pot(self):
        return self.__pot

    @pot.setter
    def pot(self, pot):
        if pot < 0:
            self.__pot = 0
        else:
            self.__pot = pot

    @property
    def bet(self):
        return self.__bet

    @bet.setter
    def bet(self, bet):
        if bet <= 0:
            self.__bet = 1
        elif bet > self.pot:
            self.__bet = self.__pot
        else:
            self.__bet = bet

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if number < 1:
            self.number = 1
        else:
            self.__number = number

    # Methods
    def roll(self):
        for i in range(self.__number):
            self.__faces[i] = random.randint(1, 6)

    def check(self):
        if self.__number != 2:
            raise ValueError("Wrong game, double-or-nothing is a two dice game")
        result = f"{self.__faces[0]} and {self.__faces[1]} - "

        # If loop to show the dices rules for the result
        # 1 - Both dices are equal and either 1 or 6 - receive bet ten fold
        if self.__faces[0] == self.__faces[1] and (self.__faces[0] == 1 or self.__faces[0] == 6):
            result += f"You won {self.__bet} x10!"
            self.__pot += self.__bet * 10
        # 2 - Both dices are equal and either 2, 3, 4 or 5 - receive double of the bet
        elif self.__faces[0] == self.__faces[1] and not (self.__faces[0] == 1 or self.__faces[0] == 6):
            result += f"You won {self.__bet} x2!"
            self.__pot += self.__bet * 2
        # 3 - The dices are not equal, but the sum of both is 6 - lose your bet
        elif self.__faces[0] != self.__faces[1] and self.__faces[0] + self.__faces[1] == 6:
            result += f"You lost {self.__bet}!"
            self.__pot -= self.__bet
        # 4 - The dices are not equal and their sum is not 6 - lose double of your bet
        elif self.__faces[0] != self.__faces[1]:
            result += f"You lost {self.__bet} x2!"
            self.__pot -= self.__bet * 2
        print(result)


def main():
    dices = Dices(100)
    print(f"The game is double-or-nothing - pot is {dices.pot}.")
    while dices.pot != 0:
        while True:
            try:
                dices.bet = int(input("Place your bet or press ENTER to exit: "))
                dices.roll()
                dices.check()
                break
            except:
                print(f"Please input a bet between 1 and {dices.pot}")
        dices.pot = dices.pot #pot updated, so pot is not negative
        print(f"Your pot is now {dices.pot}")
    print("No more bets - pot is gone")



if __name__ == '__main__':
    main()
