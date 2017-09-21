#! /usr/bin/env python3
# coding: utf-8

"""
Project 3 of Python web developer course of OpenClassrooms
This is a game where we have to help MacGyver to escape
Mac Gyver must find 3 items to fight the guardian of the labyrinth
"""

import pygame
from pygame.locals import *

import game
import constants

def main():
    """
    Main function of the programm
    """
    #initialization of pygame module
    pygame.init()
    #creation of window for display
    size_side = constants.number_cases_side*constants.size_case
    window = pygame.display.set_mode((size_side, size_side))
    #Title of window
    pygame.display.set_caption(constants.title)
    board = game.Board()
    mac = game.Characters()
    #Display the labyrinth in the window
    board.display(window)
    play = 1
    while play:
        # direction = input("choose the direction: ")
        # mac.move(direction, board)
        # board.display(mac)
        # if board.STRUCTURE[mac.line][mac.column] == "a":
        #     print("\nYOU WIN !")
        #     break
        pygame.display.flip()
        continue

if __name__ == "__main__":
    main()
