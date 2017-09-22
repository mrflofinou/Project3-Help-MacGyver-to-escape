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
import random

import pygame
from pygame.locals import *

import constants


class Board:
    """
    This class is use for:
    - initialization of game board
    - display of game board
    """
    # Class attribute to save the structure of the labyrinth in a list
    STRUCTURE = []

    def __init__(self):
        """
        This method is to initialize the game board
        from the file "structure" wich contains the structure of the labyrinth
        """
        # Read the file "structure" and save the structure of the labyrinth
        # as a list in STRUCTURE[]
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
                # we calculate the coordinates in pixels for pygame
                coordinate_x = j * constants.size_sprite
                coordinate_y = i * constants.size_sprite
                if self.STRUCTURE[i][j] == "#":
                    window.blit(wall, (coordinate_x, coordinate_y))
                elif self.STRUCTURE[i][j] == "h" or self.STRUCTURE[i][j] == "o":
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
        # Position in list STRUCTURE
        self.column = 'the letter of a line of list STRUCTURE'
        self.line = 'the line of list STRUCTURE'
        # Position in pixels on the window
        self.pixels_x = 'x coordinate = self.colum * size_sprite'
        self.pixels_y = 'y coordinate = self.line * size_sprite'


class Macgyver(Characters):
    """
    This class is use for:
    - create MacGyver with:
        .an avatar
        .his start position
    - move MacGyver
    - catch items
    """
    def __init__(self):
        self.avatar = pygame.image.load(constants.macgyver).convert_alpha()
        self.column = 0
        self.line = 14
        self.pixels_x = self.column * constants.size_sprite
        self.pixels_y = self.line * constants.size_sprite
        self.number_items = 0

    def move(self, direction, board):
        """
        This method allow the movement of the character in the labyrinth
        """
        if direction == "up":
            if self.line > 0:
                if board.STRUCTURE[self.line - 1][self.column] != "#":
                    self.line -= 1
                    self.pixels_y =  self.line * constants.size_sprite
                    # Movement with stairs
                    if board.STRUCTURE[self.line][self.column] == "o":
                        self.column = 4 # Position of stairs in STRUCTURE
                        self.line = 3 # Position of stairs in STRUCTURE
                        self.pixels_x = self.column * constants.size_sprite
                        self.pixels_y = self.line * constants.size_sprite
        if direction == "down":
            if self.line < 14:
                if board.STRUCTURE[self.line + 1][self.column] != "#":
                    self.line += 1
                    self.pixels_y =  self.line * constants.size_sprite
                    # Movement with stairs
                    if board.STRUCTURE[self.line][self.column] == "h":
                        self.column = 14 # Position of stairs in STRUCTURE
                        self.line = 4 # Postion of stairs in STRUCTURE
                        self.pixels_x = self.column * constants.size_sprite
                        self.pixels_y = self.line * constants.size_sprite
        if direction == "left":
            if self.column > 0:
                if board.STRUCTURE[self.line][self.column - 1] != "#":
                    self.column -= 1
                    self.pixels_x =  self.column * constants.size_sprite
        if direction == "right":
            if self.column < 14:
                if board.STRUCTURE[self.line][self.column + 1] != "#":
                    self.column += 1
                    self.pixels_x =  self.column * constants.size_sprite
                    # Movement with stairs
                    if board.STRUCTURE[self.line][self.column] == "o":
                        self.column = 4 # Position of stairs in STRUCTURE
                        self.line = 3 # Position of stairs in STRUCTURE
                        self.pixels_x = self.column * constants.size_sprite
                        self.pixels_y = self.line * constants.size_sprite

    def catch(self, needle, plastic, poison):
        if needle.column == self.column and needle.line == self.line:
            self.number_items += 1
            needle.column = 0
            needle.line = 15
            needle.pixels_x = needle.column * constants.size_sprite
            needle.pixels_y = needle.line * constants.size_sprite
        if plastic.column == self.column and plastic.line == self.line:
            self.number_items += 1
            plastic.column = 0
            plastic.line = 15
            plastic.pixels_x = plastic.column * constants.size_sprite
            plastic.pixels_y = plastic.line * constants.size_sprite
        if poison.column == self.column and poison.line == self.line:
            self.number_items += 1
            poison.column = 0
            poison.line = 15
            poison.pixels_x = poison.column * constants.size_sprite
            poison.pixels_y = poison.line * constants.size_sprite


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


class Items:
    """
    This class is use for:
    - create an item with:
        .an avatar
        .a random position on the game board
    """
    def __init__(self, board):
        self.avatar = pygame.image.load(constants.item).convert_alpha()
        self.column = random.randint(0, constants.number_cases_side - 1)
        self.line = random.randint(0, constants.number_cases_side - 1)
        # We check the random position is not a wall, a stair, start position
        # or arrival position
        while board.STRUCTURE[self.line][self.column] != ".":
            self.column = random.randint(0, constants.number_cases_side - 1)
            self.line = random.randint(0, constants.number_cases_side - 1)
        self.pixels_x = self.column * constants.size_sprite
        self.pixels_y = self.line * constants.size_sprite
