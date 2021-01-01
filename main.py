'''

Created by Calvin Brauer, 2021
Attempting to make a Yahtzee game

'''

from graphics import *
from random import *

class Board:
    '''main class that holds the entire board'''
    def __init__(self, window):
        '''initializes the board and draws the objects'''
        self.win = window
        
        # creating dice area
        self.diceArea = DiceArea(0, 20, 300, 150, self.win)

        # creating roll button
        pass

        # creating scoreboard
        self.scoreboard = Scoreboard(1, 99, 498, 398, self.win)

class DiceArea:
    '''area to hold the 5 dice'''
    def __init__(self, x, y, width, height, window):
        '''initializes the dice area and draws it in the given window'''
        self.win = window

        # drawing the border
        pass

        # creating dice
        pass

    def clear(self):
        '''undraws the dice'''
        pass

    def delete(self):
        '''deletes the dice'''
        pass

    def roll(self, dice):
        '''rolls the given dice and draws the results'''
        pass

class Dice:
    '''dice class'''
    def __init__(self, num_of_sides):
        '''initializes the die with given num of sides'''
        self.numSides = num_of_sides
        self.currentValue = 1
        
    def roll(self):
        '''randomly rolls the die'''
        self.currentValue = randrange(1, 7)

    def getValue(self):
        '''returns the current value of the die'''
        return self.currentValue

    def draw(self, x, y, width, height, window):
        '''draws the die at the given spot'''
        pass

class Scoreboard:
    '''scoreboard class'''
    def __init__(self, x, y, width, height, window):
        '''initializes the scoreboard and draws it in the given window'''
        self.win = window
        
        # drawing the border
        border = Rectangle(Point(x, y), Point(x + width, y + height))
        border.draw(self.win)

        # drawing score labels
        pass

        # drawing score boxes
        pass

    def updateScore(self, spot, score):
        '''updates a given space with a given score'''
        pass

class Score:
    '''score class that holds an individual score in a box'''
    def __init__(self, x, y, height, window, score):
        '''initializes the score and draws it in the given window with the given score'''
        pass

def main():
    '''main function to run the game'''
    # creating the graphics window
    win = GraphWin("Yahtzee", 500, 500)
    win.setCoords(0, 0, 500, 500)

    # creating the board on the window
    board = Board(win)   

    # running the 13 turns
    for i in range(13):
        turn()

    # giving final score
    pass

def turn():
    '''runs one player's turn once'''
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
