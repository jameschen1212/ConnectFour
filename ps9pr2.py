#
# ps9pr2.py  (Problem Set 9, Problem 2)
#
# A Connect-Four Player class 
#  

from ps9pr1 import Board

# write your class below
class Player:
    def __init__(self, checker):
        """constructs a new Player object"""
        assert(checker == 'X' or checker == 'O')
        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        """returns a string representing a Player object"""
        s = 'Player'
        s+= (' ' + self.checker)
        return s

    def opponent_checker(self):
        """returns a string representing the opponent"""

        if(self.checker == 'X'):
            return 'O'
        else:
            return 'X'

    def next_move(self, board):
        """accepts a Board object as a parameter and returns the column where the player wants to make the next move"""
        self.num_moves += 1
        while True:
            col = int(input('Enter a column: '))
            if(board.can_add_to(col) == True):
               return col
            else:
               print('Try Again!')

