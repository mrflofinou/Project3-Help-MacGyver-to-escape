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
    height_size = constants.height_number_sprite * constants.sprite_size
    width_size = constants.width_number_sprite * constants.sprite_size
    window = pygame.display.set_mode((width_size, height_size))
    # Title of window
    pygame.display.set_caption(constants.title)
    # This is for the character stay in movement whent you stay press on a key
    pygame.key.set_repeat(400, 30)
    # Pygame module to play music with loops
    music = pygame.mixer.Sound(constants.music)
    music.play(loops=1)
    # Creation of the object board from class Board
    board = game.Board()
    # Creation of the start position of MacGyver
    position_macgyver = game.Position(14, 0)
    #Creation of the position of Murdoc
    position_murdock = game.Position(0, 14)
    # Creation of object mac from class Macgyver
    macgyver = game.Macgyver(position_macgyver)
    # Creation of object murdoc from class Murdock
    murdoc = game.Murdoc(position_murdock)
    # Creation of objects from class Items
    items = [game.Items(board), game.Items(board), game.Items(board)]
    play = 1
    end = 1
    while play:
        # To limit the framerate
        pygame.time.Clock().tick(30)
        # Management of keys with pygame
        for event in pygame.event.get():
            if event.type == QUIT:
                play = 0
                end = 0
            if event.type == KEYDOWN:
                if event.key == K_RIGHT:
                    macgyver.move('right', board)
                    macgyver.catch_if_item(*items)
                if event.key == K_LEFT:
                    macgyver.move('left', board)
                    macgyver.catch_if_item(*items)
                if event.key == K_UP:
                    macgyver.move('up', board)
                    macgyver.catch_if_item(*items)
                if event.key == K_DOWN:
                    macgyver.move('down', board)
                    macgyver.catch_if_item(*items)
        # Display the labyrinth in the window
        window.fill((0, 0, 0)) # reset the display to the inventory
        board.display(window, macgyver)
        for item in items:
            window.blit(item.picture, (item.position.pixels_x, item.position.pixels_y))
        window.blit(macgyver.avatar, (macgyver.position.pixels_x, macgyver.position.pixels_y))
        window.blit(murdoc.avatar, (murdoc.position.pixels_x, murdoc.position.pixels_y))
        pygame.display.flip()
        if board.STRUCTURE[macgyver.position.line][macgyver.position.column] == board.STRUCTURE[murdoc.position.line][murdoc.position.column]:
            play = 0

    start_ticks = pygame.time.get_ticks() # Starter tick
    # Final loop to display the end window to know if you win or not
    while end:
        seconds = (pygame.time.get_ticks()-start_ticks)/1000 # Calculate how many seconds
        game.Rules.win(macgyver, board)
        if seconds > 4: # If more than 4 seconds close the game
            end = 0

if __name__ == "__main__":
    main()
