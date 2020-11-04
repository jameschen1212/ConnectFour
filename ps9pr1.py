#James Chen
#jamesche@bu.edu

class Board:
    def __init__(self, height, width):
        """constructor class"""
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]

    def __repr__(self):
        """Returns a string representation for a Board object."""
        s = ''  # begin with an empty string

            # add one row of slots at a time
        for row in range(self.height):
            s += '|'    # one vertical bar at the start of the row

            for col in range(self.width):
                s += self.slots[row][col] + '|'

            s += '\n'   # newline at the end of the row

            # Add code here for the hyphens at the bottom of the board
            # and the numbers underneath it.

        hypen = ''
        for i in range((self.width*2)+1):
            hypen += '-'

        number = ' '
        
        for i in range((self.width)):
            number += str(i%10)
            number += ' '

        
        s += hypen
        s += '\n'
        s += number

        return s

    def add_checker(self, checker, col):
        """ adds a checker either x or o to the board """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        # put the rest of the method here
        row = 0
        

        while self.slots[row][col] == ' ':
            row += 1
            if(row == self.height):
               self.slots[self.height - 1][col] = checker
               break
        if (row != self.height):
            self.slots[row - 1][col] = checker

    def reset(self):
        """ resets the board to all empty slots """
        for i in range(self.height):
            for c in range(self.width):
                self.slots[i][c] = ' '

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'

    def can_add_to(self, col):
        """ returns True if it is valid to place a checker in the column col on the calling Board object. Otherwise, it should return False"""
        if(col < 0):
            return False
        elif(col > (self.width - 1)):
            return False
        else:
            if(self.slots[0][col] != ' '):
                return False
            else:
                return True

    def is_full(self):
        """returns True if the called Board object is completely full of checkers, and returns False otherwise"""
        for i in range(self.width):
            if(self.can_add_to(i) == True):
                return False
        return True

    def remove_checker(self, col):
        """removes the top checker from column col of the called Board object. If the column is empty, then the method should do nothing."""
        for i in range(self.height):
            if self.slots[i][col]!= ' ':
                self.slots[i][col] = ' '
                break

    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the checker """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a diagonal win for the checker"""
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False

    def is_up_diagonal_win(self, checker):
        """Checks for a diagonal win for the checker"""
        for row in range(3, self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False

    def is_win_for(self, checker):
        """Checks for all wins for the checker"""
        assert(checker == 'X' or checker == 'O')
        if(self.is_horizontal_win(checker) == True or \
           self.is_vertical_win(checker) == True or \
           self.is_down_diagonal_win(checker) == True or \
           self.is_up_diagonal_win(checker) == True):
            return True
        return False
        
        
            

                


    
            

        
        
        
    

    

