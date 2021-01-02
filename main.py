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
        self.diceArea = DiceArea(10, 20, 300, 60, self.win)

        # creating roll button
        rollButton = Rectangle(Point(325, 25), Point(475, 75))
        rollButton.draw(self.win)
        rollLabelPoint = rollButton.getCenter()
        rollLabel = Text(rollLabelPoint, "Roll")
        rollLabel.draw(self.win)

        # creating scoreboard
        self.scoreboard = Scoreboard(1, 99, 498, 398, self.win)

    def roll(self, dice):
        '''rolls the given dice and then updates the screen'''
        self.diceArea.roll(dice)
        self.diceArea.updateArea()

    def highlight(self, die):
        '''highlights a given die'''
        self.diceArea.highlight(die)

    def clearHighlight(self):
        '''de-highlights all dice'''
        self.diceArea.clearHighlight()

class DiceArea:
    '''area to hold the 5 dice'''
    def __init__(self, x, y, width, height, window):
        '''initializes the dice area and draws it in the given window'''
        self.win = window

        # drawing the border
        border = Rectangle(Point(x, y), Point(x + width, y + height))
        border.draw(self.win)

        # creating dice objects
        self.dice = []
        for i in range(5):
            self.dice.append(Dice(6))

        # drawing boxes to hold the dice values
        self.boxes = []
        boxSide = height - 5
        box = Rectangle(Point(x + 5, y + 5), Point(x + boxSide, y + boxSide))
        self.boxes.append(box)
        box.draw(self.win)
        tempBox = box
        for i in range(4):
            newBox = tempBox.clone()
            newBox.move(boxSide + 5, 0)
            newBox.draw(self.win)
            self.boxes.append(newBox)
            tempBox = newBox

        # creating dice labels
        self.labels = []
        center = tempBox.getCenter()
        self.labels.append(Text(center, ""))
        for i in range(4):
            center.move(0 - (boxSide + 5), 0)
            self.labels.append(Text(center, ""))
        self.labels.reverse()

    def clear(self):
        '''undraws the dice labels'''
        for i in self.labels:
            i.setText("")

    def roll(self, dice):
        '''rolls the given dice and draws the results'''
        for i in dice:
            self.dice[i].roll()

    def updateArea(self):
        '''updates (redraws) all of the dice'''
        for i in range(5):
            self.labels[i].setText(self.dice[i].getValue())
            self.labels[i].draw(self.win)

    def highlight(self, die):
        '''highlights a given die'''
        self.boxes[die].setBorder("red")

    def clearHighlight(self):
        '''de-highlights the dice'''
        for i in range(5):
            self.boxes[i].setBorder("black")

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
    win.setBackground("white")

    # creating the board on the window
    board = Board(win)   

    # running the 13 turns
    '''for i in range(13):
        turn(win, board)'''
    turn(win, board) # FIXME: testing

    # giving final score
    pass

def turn(win, board):
    '''runs one player's turn once'''
    # creating main instructions at the bottom
    instructions = Text(Point(250, 10), "")
    instructions.setSize(10)
    instructions.draw(win)
    
    # prompting user to roll
    instructions.setText("Click Roll to roll")
    
    # waiting for user click on roll button
    while True:
        q = win.checkMouse()
        if bool(q):
            if rollClicked(q):
                break
            
    # rolling all of the dice since it's the first roll
    board.roll([0, 1, 2, 3, 4])

    # prompting user to choose which dice to keep
    instructions.setText("Click which dice you want to keep then click Roll")

    # waiting for user clicks
    keepDice = [0, 1, 2, 3, 4]
    while True:
        q = win.checkMouse()
        if bool(q):
            if rollClicked(q):
                break
            dieNum = dieClicked(q)
            if bool(dieNum):
                keepDice.remove(dieNum)
                board.highlight(dieNum)
                

    # prompting user to roll
    pass

    # prompting user to choose which dice to keep
    pass

    # prompting user to roll
    pass

    # showing final dice and prompting user to choose score
    pass

    # clearing text at bottom
    pass

def rollClicked(q):
    '''checks whether the roll button has been clicked'''
    if q.getX() > 325 and q.getX() < 475:
        if q.getY() > 25 and q.getY() < 75:
            return True
    return False

def dieClicked(q):
    '''checks whether a die has been clicked and returns its number'''
    # checking whether it's within the right height
    if q.getY() < 25 or q.getY() > 85:
        return False

    # checking each individual die
    # die 0
    if q.getX() > 15 and q.getX() < 70:
        return 0

    # die 1
    pass

    # die 2
    pass

    # die 3
    pass

    # die 4
    pass

main()
