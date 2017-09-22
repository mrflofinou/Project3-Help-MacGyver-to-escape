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
    # Initialization of pygame module
    pygame.init()
    # Creation of window for display
    size_side = constants.number_cases_side * constants.size_sprite
    window = pygame.display.set_mode((size_side, size_side))
    # Title of window
    pygame.display.set_caption(constants.title)
    # This is for the character stay in movement whent you stay press on a key
    pygame.key.set_repeat(400, 30)
    # Creation of the object board from class Board
    board = game.Board()
    # Creation of object mac from class Macgyver
    mac = game.Macgyver()
    # Creation of object murdoc from class Murdock
    murdoc = game.Murdoc()
    # Creation of objects from class Items
    needle = game.Items(board)
    plastic = game.Items(board)
    poison = game.Items(board)
    play = 1
    while play:
        # To limit the framerate
        pygame.time.Clock().tick(30)
        # Management of keys with pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    mac.move('right', board)
                    mac.catch(needle, plastic, poison)
                if event.key == K_LEFT:
                    mac.move('left', board)
                    mac.catch(needle, plastic, poison)
                if event.key == K_UP:
                    mac.move('up', board)
                    mac.catch(needle, plastic, poison)
                if event.key == K_DOWN:
                    mac.move('down', board)
                    mac.catch(needle, plastic, poison)
        # Display the labyrinth in the window
        board.display(window)
        window.blit(needle.avatar, (needle.pixels_x, needle.pixels_y))
        window.blit(plastic.avatar, (plastic.pixels_x, plastic.pixels_y))
        window.blit(poison.avatar, (poison.pixels_x, poison.pixels_y))
        window.blit(mac.avatar, (mac.pixels_x, mac.pixels_y))
        window.blit(murdoc.avatar, (murdoc.pixels_x, murdoc.pixels_y))
        pygame.display.flip()
        if board.STRUCTURE[mac.line][mac.column] == "a":
            play = 0

    end = 1
    start_ticks = pygame.time.get_ticks() # Starter tick
    # Final loop to display the end window to know if you win or not
    while end:
        seconds = (pygame.time.get_ticks()-start_ticks)/1000 # Calculate how many seconds
        game.Rules.win(mac, board)
        if seconds > 4: # If more than 5 seconds close the game
            end = 0

if __name__ == "__main__":
    main()
