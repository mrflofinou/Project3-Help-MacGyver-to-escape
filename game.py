"""
This file contains the classes of the programm
There are 10 classes:
    - Board
    - Position
    - Character
        - MacGyver
        - Murdoc
    - Item
        - Needle
        - Tube
        - Poison
    - Rule
"""
import random

import pygame
from pygame.locals import *

import constants


class Position:
    """
    This class manages the position of character and items
    """
    def __init__(self, line, column):
        # Position in list STRUCTURE
        self.column = column
        self.line = line
        # Position in pixels on the window
        self.pixels_x = self.column * constants.sprite_size
        self.pixels_y = self.line * constants.sprite_size


class Board:
    """
    This class is used for:
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
            self.STRUCTURE = [[letter for letter in line if letter != "\n"] for line in labyrinth]


    def display(self, window):
        """
        This method is to display the game board
        """
        # To display the structure of labyrinth
        wall_picture = pygame.image.load(constants.walls).convert()
        floor_picture = pygame.image.load(constants.floor).convert()
        stairs_picture = pygame.image.load(constants.stairs).convert()
        for i, line in enumerate(self.STRUCTURE):
            for j, column in enumerate(line):
                position = Position(i, j)
                if self.STRUCTURE[i][j] == constants.wall_symbol:
                    window.blit(wall_picture, (position.pixels_x, position.pixels_y))
                elif self.STRUCTURE[i][j] == constants.stairs_symbol:
                    window.blit(stairs_picture, (position.pixels_x, position.pixels_y))
                else:
                    window.blit(floor_picture, (position.pixels_x, position.pixels_y))
        # To display the inventory
        inventory = pygame.font.SysFont('items', 30, False, True)
        text = "Items:".rjust(3)
        window.blit(inventory.render(text, True, (255, 255, 255)), (5, 610))


class Character:
    """
    This class is used for:
    - create a character with:
        .an avatar
        .a position
    """
    def __init__(self, position):
        self.picture = 'picture of character'
        self.position = position


class Macgyver(Character):
    """
    This class is used for:
    - create MacGyver with:
        .an avatar
        .his start position
        .the number of items
    - move with stairs
    - move MacGyver
    - catch if items
    """
    def __init__(self, position):
        """
        This method creates MacGyver with his avatar and start position
        """
        self.picture = pygame.image.load(constants.macgyver).convert_alpha()
        self.position = position
        self.number_items = 0

    def _take_stairs(self):
        """
        This private method manages the movement with stairs
        """
        if (self.position.line, self.position.column) == (3, 4): # Position of stairs one
            self.position = Position(4, 14) # Postion of stairs 2
        elif (self.position.line, self.position.column) == (4, 14): # Postion of stairs 2
            self.position = Position(3, 4) # Position of stairs one

    def move(self, direction, board):
        """
        This method allows the movement of the character in the labyrinth
        """
        if direction == "up":
            if self.position.line > 0:
                if board.STRUCTURE[self.position.line - 1][self.position.column] != constants.wall_symbol:
                    self.position.line -= 1
                    self.position = Position(self.position.line, self.position.column)
                    # Movement with stairs
                    self._take_stairs()
        if direction == "down":
            if self.position.line < len(board.STRUCTURE) - 1:
                if board.STRUCTURE[self.position.line + 1][self.position.column] != constants.wall_symbol:
                    self.position.line += 1
                    self.position = Position(self.position.line, self.position.column)
                    # Movement with stairs
                    self._take_stairs()
        if direction == "left":
            if self.position.column > 0:
                if board.STRUCTURE[self.position.line][self.position.column - 1] != constants.wall_symbol:
                    self.position.column -= 1
                    self.position = Position(self.position.line, self.position.column)
                    # Movement with stairs
                    self._take_stairs()
        if direction == "right":
            if self.position.column < len(board.STRUCTURE) - 1:
                if board.STRUCTURE[self.position.line][self.position.column + 1] != constants.wall_symbol:
                    self.position.column += 1
                    self.position = Position(self.position.line, self.position.column)
                    # Movement with stairs
                    self._take_stairs()

    def catch_if_item(self, *items):
        """
        This method allows to MacGyver to catch an item if there is one on his position
        The item is move in the counter
        """
        for item in items:
            if (item.position.line, item.position.column) == (self.position.line, self.position.column):
                self.number_items += 1
                if self.number_items == 1:
                    item.position = Position(15, 2)
                elif self.number_items == 2:
                    item.position = Position(15, 3)
                else:
                    item.position = Position(15, 4)


class Murdoc(Character):
    """
    This class is used for:
    - create Murdoc with:
        .an avatar
        .his position
    """
    def __init__(self, position):
        """
        This method creates Murdoc with his avatar and his position
        """
        self.picture = pygame.image.load(constants.murdoc).convert_alpha()
        self.position = position


class Item:
    """
    This class is used for:
    - create an item with:
        .a picture
        .a random position on the game board
    """
    def __init__(self, board):
        """
        This method creates an item with a picture and a random position
        """
        self.picture = pygame.image.load(constants.item).convert_alpha()
        self.position = self._random_position(board)

    def _random_position(self, board):
        """
        This method calculates a random position for an item
        """
        random_line = random.randint(0, len(board.STRUCTURE) - 1)
        random_column = random.randint(0, len(board.STRUCTURE) - 1)
        # We check the random position is not a wall, a stair, start position
        # or arrival position
        while board.STRUCTURE[random_line][random_column] != constants.floor_symbol:
            random_line = random.randint(0, len(board.STRUCTURE) - 1)
            random_column = random.randint(0, len(board.STRUCTURE) - 1)
        board.STRUCTURE[random_line][random_column] = constants.item_symbol
        return Position(random_line, random_column)


class Needle(Item):
    """
    Create a needle
    """
    def __init__(self, board):
        self.picture = pygame.image.load(constants.needle).convert_alpha()
        self.position = self._random_position(board)


class Tube(Item):
    """
    Create a tube
    """
    def __init__(self, board):
        self.picture = pygame.image.load(constants.tube).convert_alpha()
        self.position = self._random_position(board)


class Poison(Item):
    """
    create a poison
    """
    def __init__(self, board):
        self.picture = pygame.image.load(constants.poison).convert_alpha()
        self.position = self._random_position(board)


class Rule:
    """
    This class manage the end of the game
    """
    @classmethod
    def win(self, character, board):
        """
        This method manage the end of the game
        """
        pygame.init()
        window_end = pygame.display.set_mode((550, 380))
        if character.number_items == 3:
            window_end.blit(pygame.image.load(constants.win).convert(), (0, 0))
        else:
            window_end.blit(pygame.image.load(constants.lose).convert(), (0, 0))
        pygame.display.flip()
