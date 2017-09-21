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
    size_side = constants.number_cases_side * constants.size_sprite
    window = pygame.display.set_mode((size_side, size_side))
    #Title of window
    pygame.display.set_caption(constants.title)
    #this is for the character stay in movement whent you stay press on a key
    pygame.key.set_repeat(400, 30)
    #creation of the object board from class Board
    board = game.Board()
    #creation of object mac from class Macgyver
    mac = game.Macgyver()
    #creation of object murdock from class Murdock
    murdock = game.Murdock()
    play = 1
    while play:
        #to limit the framerate
        pygame.time.Clock().tick(30)
        #management of keys with pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mac.move('right', board)
                if event.key == K_LEFT:
                    mac.move('left', board)
                if event.key == K_UP:
                    mac.move('up', board)
                if event.key == K_DOWN:
                    mac.move('down', board)
        #Display the labyrinth in the window
        board.display(window)
        window.blit(mac.avatar, (mac.pixels_x, mac.pixels_y))
        window.blit(murdock.avatar, (murdock.pixels_x, murdock.pixels_y))
        pygame.display.flip()
        if board.STRUCTURE[mac.line][mac.column] == "a":
            print("\nYOU WIN !")
            play = 0

if __name__ == "__main__":
    main()
