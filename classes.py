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


class Board:
    """
    This class is use for:
    - initialization of game board
    - display of game board
    """

    #Class attribute to save the structure of the labyrinth in a list
    STRUCTURE = []

    def initialization(self):
        """
        This method is to initialize the game board
        from the file "structure" wich contains the structure of the labyrinth
        """
        #Read the file "structure" and save the structure of the labyrinth
        #as a list in STRUCTURE[]
        with open("structure", "r") as labyrinth:
            for line in labyrinth:
                self.STRUCTURE += line.split()

    def display(self):
        """
        This method is to display the game board
        """
        #for each line of list STRUCTURE we print the line
        for line in self.STRUCTURE:
            print(line)
