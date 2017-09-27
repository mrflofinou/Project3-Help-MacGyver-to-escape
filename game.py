"""
This file contains the classes of the programm
There are 6 classes:
    - Board
    - Position
    - Characters
        - MacGyver
        - Murdoc
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
            self.STRUCTURE = [[letter for letter in line if letter != "\n"]for line in labyrinth]

    def display(self, window, character):
        """
        This method is to display the game board
        """
        # To display the structure of labyrinth
        wall = pygame.image.load(constants.walls).convert()
        floor = pygame.image.load(constants.floor).convert()
        stairs = pygame.image.load(constants.stairs).convert()
        for i, line in enumerate(self.STRUCTURE):
            for j, column in enumerate(line):
                # we calculate the coordinates in pixels for pygame
                coordinate_x = j * constants.sprite_size
                coordinate_y = i * constants.sprite_size
                if self.STRUCTURE[i][j] == "#":
                    window.blit(wall, (coordinate_x, coordinate_y))
                elif self.STRUCTURE[i][j] == "h" or self.STRUCTURE[i][j] == "o":
                    window.blit(stairs, (coordinate_x, coordinate_y))
                else:
                    window.blit(floor, (coordinate_x, coordinate_y))
        # To display the inventory
        inventory = pygame.font.SysFont('items', 30, False, True)
        text = "Items".rjust(3)
        window.blit(inventory.render(text, True, (255, 255, 255)), (5, 610))
        items = pygame.font.SysFont('items_number', 30, False, True)
        if character.number_items > 0:
            text_items = "x" + str(character.number_items).rjust(3)
            window.blit(items.render(text_items, True, (255, 255, 255)), (120, 610))


class Position:
    """
    This class manage the position of character and items
    """
    def __init__(self, line, column):
        # Position in list STRUCTURE
        self.column = column
        self.line = line
        # Position in pixels on the window
        self.pixels_x = self.column * constants.sprite_size
        self.pixels_y = self.line * constants.sprite_size


class Characters:
    """
    This class is use for:
    - create a character with:
        .an avatar
        .a position
    """
    def __init__(self, position):
        self.avatar = 'picture of character'
        # Position in list STRUCTURE
        self.position = position


class Macgyver(Characters):
    """
    This class is use for:
    - create MacGyver with:
        .an avatar
        .his start position
        .the number of items
    - move MacGyver
    - catch if items
    """
    def __init__(self, position):
        self.avatar = pygame.image.load(constants.macgyver).convert_alpha()
        self.position = position
        self.number_items = 0

    def move(self, direction, board):
        """
        This method allow the movement of the character in the labyrinth
        """
        if direction == "up":
            if self.position.line > 0:
                if board.STRUCTURE[self.position.line - 1][self.position.column] != "#":
                    self.position.line -= 1
                    self.position.pixels_y = self.position.line * constants.sprite_size
                    # Movement with stairs
                    if board.STRUCTURE[self.position.line][self.position.column] == "o":
                        self.position = Position(3, 4)
        if direction == "down":
            if self.position.line < 14:
                if board.STRUCTURE[self.position.line + 1][self.position.column] != "#":
                    self.position.line += 1
                    self.position.pixels_y = self.position.line * constants.sprite_size
                    # Movement with stairs
                    if  board.STRUCTURE[self.position.line][self.position.column] == "h":
                        self.position = Position(4, 14)
        if direction == "left":
            if self.position.column > 0:
                if board.STRUCTURE[self.position.line][self.position.column - 1] != "#":
                    self.position.column -= 1
                    self.position.pixels_x = self.position.column * constants.sprite_size
        if direction == "right":
            if self.position.column < 14:
                if board.STRUCTURE[self.position.line][self.position.column + 1] != "#":
                    self.position.column += 1
                    self.position.pixels_x = self.position.column * constants.sprite_size
                    # Movement with stairs
                    if board.STRUCTURE[self.position.line][self.position.column] == "o":
                        self.position = Position(3, 4)

    def catch_if_item(self, needle, plastic, poison):
        if needle.column == self.position.column and needle.line == self.position.line:
            self.number_items += 1
            needle.column = 2
            needle.line = 15
            needle.pixels_x = needle.column * constants.sprite_size
            needle.pixels_y = needle.line * constants.sprite_size
        if plastic.column == self.position.column and plastic.line == self.position.line:
            self.number_items += 1
            plastic.column = 2
            plastic.line = 15
            plastic.pixels_x = plastic.column * constants.sprite_size
            plastic.pixels_y = plastic.line * constants.sprite_size
        if poison.column == self.position.column and poison.line == self.position.line:
            self.number_items += 1
            poison.column = 2
            poison.line = 15
            poison.pixels_x = poison.column * constants.sprite_size
            poison.pixels_y = poison.line * constants.sprite_size


class Murdoc(Characters):
    """
    This class is use for:
    - create Murdoc with:
        .an avatar
        .his position
    """
    def __init__(self, position):
        self.avatar = pygame.image.load(constants.murdoc).convert_alpha()
        self.position = position


class Items:
    """
    This class is use for:
    - create an item with:
        .an avatar
        .a random position on the game board
    """
    def __init__(self, board):
        self.picture = pygame.image.load(constants.item).convert_alpha()
        self.column = random.randint(0, len(board.STRUCTURE) - 1)
        self.line = random.randint(0, len(board.STRUCTURE) - 1)
        # We check the random position is not a wall, a stair, start position
        # or arrival position
        while board.STRUCTURE[self.line][self.column] != ".":
            self.column = random.randint(0, len(board.STRUCTURE) - 1)
            self.line = random.randint(0, len(board.STRUCTURE) - 1)
        self.pixels_x = self.column * constants.sprite_size
        self.pixels_y = self.line * constants.sprite_size


class Rules:
    """
    This class manage the end of the game
    """
    @classmethod
    def win(self, character, board):
        pygame.init()
        window_end = pygame.display.set_mode((550, 380))
        if character.number_items == 3:
            window_end.blit(pygame.image.load(constants.win).convert(), (0, 0))
        else:
            window_end.blit(pygame.image.load(constants.lose).convert(), (0, 0))
        pygame.display.flip()
