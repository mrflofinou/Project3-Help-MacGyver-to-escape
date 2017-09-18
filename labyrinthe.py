#! /usr/bin/env python3
# coding: utf-8

"""
Project 3 of Python web developer course of OpenClassrooms
This is a game where we have to help MacGyver to escape
Mac Gyver must find 3 items to fight the guardian of the labyrinth
"""

import classes

def main():
    """
    Main function of the programm
    """
    board = classes.Board()
    board.initialization()
    board.display()


if __name__ == "__main__":
    main()
