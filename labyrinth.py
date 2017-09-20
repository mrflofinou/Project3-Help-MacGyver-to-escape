#! /usr/bin/env python3
# coding: utf-8

"""
Project 3 of Python web developer course of OpenClassrooms
This is a game where we have to help MacGyver to escape
Mac Gyver must find 3 items to fight the guardian of the labyrinth
"""

import game

def main():
    """
    Main function of the programm
    """
    board = game.Board()
    mac = game.Characters()
    board.display(mac)
    loop = 1
    while loop:
        direction = input("choose the direction: ")
        mac.move(direction, board)
        board.display(mac)
        if board.STRUCTURE[mac.line][mac.column] == "a":
            print("\nYOU WIN !")
            break

if __name__ == "__main__":
    main()
