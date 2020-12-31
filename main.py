'''

Created by Calvin Brauer
Attempting to make a Yahtzee game

'''

from graphics import *
from random import *

class Dice:
    '''dice class'''
    def __init__(self, num_of_sides):
        '''initializes the die with given num of sides'''
        self.numSides = num_of_sides
        self.currentValue = 1
        
    def roll(self):
        '''randomly rolls the die'''
        pass

    def getValue(self):
        '''returns the current value of the die'''
        return self.currentValue

class Scoreboard:
    '''scoreboard class'''
    pass

def main():
    '''main function to run the game'''
    # creating the graphics window
    win = GraphWin("Yahtzee", 500, 500)

    # creating 5 dice with 6 sides each
    dice = []
    for i in range(5):
        die = Dice(6)
        dice.append(die)

    # prompting user to roll
    pass

    # prompting user to choose which dice to keep
    pass

    # prompting user to roll
    pass

    # prompting user to choose which dice to keep
    pass

    # prompting user to roll
    pass

    # showing final dice and prompting user to choose score
    pass

main()
