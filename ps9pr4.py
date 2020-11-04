#
# ps9pr4.py  (Problem Set 9, Problem 4)
#
# AI Player for use in Connect Four   
#

import random  
from ps9pr3 import *

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ constructs a new AIPlayer object
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)
        super().__init__(checker)
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        """returns a string representing an AIPlayer object"""
        s = 'Player'
        s+= (' ' + self.checker + ' ' + '(' + self.tiebreak + ',' + ' ' + str(self.lookahead) + ')')
        return s

    def max_score_column(self, scores):
        """takes a list scores containing a score for each column of the board, and that returns the index of the column with the maximum score."""
        maxscore = max(scores)
        listindices = []
        for i in range(len(scores)):
            if(scores[i] == maxscore):
                listindices += [i]
        
        if(self.tiebreak == 'LEFT'):
            return listindices[0]
        elif(self.tiebreak == 'RIGHT'):
            return listindices[-1]
        else:
            return random.choice(listindices)

    def scores_for(self, board):
        """takes a Board object board and determines the called AIPlayer‘s scores for the columns in board"""
        scores = [50] * board.width
        for i in range(board.width):
            if(board.can_add_to(i) == False):
                scores[i] = -1
            elif(board.is_win_for(self.checker) == True):
                scores[i] = 100
            elif(board.is_win_for(self.opponent_checker()) == True):
                scores[i] = 0
            elif(self.lookahead == 0):
                scores[i] = 50
            else:
                board.add_checker(self.checker, i)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, (self.lookahead - 1))
                scores_opponent = opponent.scores_for(board)
                if(scores_opponent[i] == 100):
                    for num in range(len(scores)):
                        scores[num] = 0
                    scores[i] = 100
                elif(scores_opponent[i] == 0):
                    for num in range(len(scores)):
                        scores[num] = 0
                    scores[i] = 100
                elif(scores_opponent[i] == 50):
                    scores[i] = 50
                board.remove_checker(i)

        return scores

    def next_moves(self, board):
        """Rather than asking the user for the next move, this version of next_move should return the called AIPlayer‘s judgment of its best possible move"""
        self.num_moves += 1
        return max_score_column(scores_for(board))

    
                
                
        

    


