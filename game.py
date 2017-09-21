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

import pygame
from pygame.locals import *

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

    def display(self, window):
        """
        This method is to display the game board
        """

        wall = pygame.image.load(constants.walls).convert()
        floor = pygame.image.load(constants.floor).convert()
        stairs = pygame.image.load(constants.stairs).convert()

        for i, line in enumerate(self.STRUCTURE):
            for j, column in enumerate(line):
                #we calculate the coordinates in pixels for pygame
                coordinate_x = j * constants.size_sprite
                coordinate_y = i * constants.size_sprite
                if self.STRUCTURE[i][j] == "#":
                    window.blit(wall, (coordinate_x, coordinate_y))
                elif self.STRUCTURE[i][j] == "h":
                    window.blit(stairs, (coordinate_x, coordinate_y))
                else:
                    window.blit(floor, (coordinate_x, coordinate_y))


class Characters:
    """
    This class is use for:
    - create a character with:
        .an avatar
        .a position
    """
    def __init__(self):
        self.avatar = 'picture of character'
        #position in list STRUCTURE
        self.column = 'the letter of a line of list STRUCTURE'
        self.line = 'the line of list STRUCTURE'
        #position in pixels on the window
        self.pixels_x = 'x coordinate = self.colum * size_sprite'
        self.pixels_y = 'y coordinate = self.line * size_sprite'


class Macgyver(Characters):
    """
    This class is use for:
    - create MacGyver with:
        .an avatar
        .his start position
    - move MacGyver
    """
    def __init__(self):
        self.avatar = pygame.image.load(constants.macgyver).convert_alpha()
        self.column = 0
        self.line = 14
        self.pixels_x = self.column * constants.size_sprite
        self.pixels_y = self.line * constants.size_sprite

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


class Murdock(Characters):
    """
    This class is use for:
    - create Murdock with:
        .an avatar
        .his position
    """
    def __init__(self):
        self.avatar = pygame.image.load(constants.murdock).convert_alpha()
        self.column = 14
        self.line = 0
        self.pixels_x = self.column * constants.size_sprite
        self.pixels_y = self.line * constants.size_sprite
