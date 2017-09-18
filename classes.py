"""
This file contains the classes of the programm
There are 6 classes:
     - Characters
        - MacGyver
        - Murdock
    - Board
    - Items
    - Rules
"""

import constants

class Board:
    """
    This class is use for:
    - initialization of game board
    - display of game board
    """

    #Class attribute to save the structure of the labyrinth in a list
    STRUCTURE = []

    def initialization(self):
        """
        This method is to initialize the game board
        from the file "structure" wich contains the structure of the labyrinth
        """
        #Read the file "structure" and save the structure of the labyrinth
        #as a list in STRUCTURE[]
        with open("structure", "r") as labyrinth:
            for line in labyrinth:
                self.STRUCTURE += line.split()

    def display(self, character):
        """
        This method is to display the game board
        """
        #for each line of list STRUCTURE we print the line
        for i, line in enumerate(self.STRUCTURE):
            #We create a temporary list to save the letters of a line
            #that will allow to print line by line and not letter by letter
            temp = []
            for j, letter in enumerate(line):
                if character.line == i and character.column == j:
                    temp += character.avatar
                else:
                    temp += letter
            print("".join(temp))

class Characters:
    """
    This class is use for:
    - create a character with:
        .an avatar
        .a position
    - move the character
    """
    def __init__(self):
        self.avatar = 'X'
        self.line = 14
        self.column = 0

    def move(self, direction, board):
        """
        This method allow the movement of the character in the labyrinth
        """
        if direction == "o":
            if self.line > 0:
                if board.STRUCTURE[self.line - 1][self.column] != "#":
                    self.line -= 1
        if direction == "l":
            if self.line < 14:
                if board.STRUCTURE[self.line + 1][self.column] != "#":
                    self.line += 1
        if direction == "k":
            if self.column > 0:
                if board.STRUCTURE[self.line][self.column - 1] != "#":
                    self.column -= 1
        if direction == "m":
            if self.column < 14:
                if board.STRUCTURE[self.line][self.column + 1] != "#":
                    self.column += 1
