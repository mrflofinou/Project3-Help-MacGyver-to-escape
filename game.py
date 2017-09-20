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

    def __init__(self):
        """
        This method is to initialize the game board
        from the file "structure" wich contains the structure of the labyrinth
        """
        #Read the file "structure" and save the structure of the labyrinth
        #as a list in STRUCTURE[]
        with open("structure", "r") as labyrinth:
            for line in labyrinth:
                structure_lines = []
                for letter in line:
                    if letter != "\n":
                        structure_lines.append(letter)
                self.STRUCTURE.append(structure_lines)

    def display(self, character):
        """
        This method is to display the game board
        """
        # copy the liste STRUCTURE in new_structure without to copy
        # the references of the list STRUCTURE -> the list STRUCTURE
        # will be not modify if new_structure will be modifiy
        new_structure = [[letter for letter in line]for line in self.STRUCTURE]
        new_structure[character.line][character.column] = character.avatar
        [print("".join(line)) for line in new_structure]


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
        self.column = 0
        self.line = 14

    def move(self, direction, board):
        """
        This method allow the movement of the character in the labyrinth
        press "o" to go up
        press "l" to go down
        press "k" to go left
        press "m" to go right
        """
        if direction == "o": #up
            if self.line > 0:
                if board.STRUCTURE[self.line - 1][self.column] != "#":
                    self.line -= 1
        if direction == "l": #down
            if self.line < 14:
                if board.STRUCTURE[self.line + 1][self.column] != "#":
                    self.line += 1
        if direction == "k": #left
            if self.column > 0:
                if board.STRUCTURE[self.line][self.column - 1] != "#":
                    self.column -= 1
        if direction == "m": #right
            if self.column < 14:
                if board.STRUCTURE[self.line][self.column + 1] != "#":
                    self.column += 1
