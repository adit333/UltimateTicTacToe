
class NumTicTacToe:
    def __init__(self,player_1,player_2):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        self.entered = 0
        self.board_type = 'Num'
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(0)
            self.board.append(row)
            
        self.entered_num = []
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn = self.player_1
        self.continue_game = True          
                                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           

        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    self.board[i][j] = ' '
                 
        border = '|'
        dashes = '-'
        print('   ','0','  ','1','  ', '2',sep = ' ')
        print('0', self.board[0][0], border, self.board[0][1], border,self.board[0][2], sep = '  ')
        print('  ', dashes*13)
        print('1', self.board[1][0], border, self.board[1][1], border,self.board[1][2], sep = '  ')
        print('  ', dashes*13)
        print('2', self.board[2][0], border, self.board[2][1], border,self.board[2][2], sep = '  ')
        
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == ' ':
                    self.board[i][j] = 0        

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        if self.board[row][col] == 0:
            return True
        else:
            return False 
        
    def update(self, row, col, num):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col):
            self.board[row][col] = num
            self.entered += 1
            return True
        else:
            return False
                
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        full = True
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    full = False
        return full
                      
    def isTie(self):
        # Checks to see if there is a tie and returns True if there is a tie
        if self.entered == 9:
            return True
        else:
            return False
        
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        adds up to 15. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        if self.rowWin() or self.colWin() or self.diagonalWin():
            return True
        else:
            return False
             
    def rowWin(self):
        # Considering a row win
        rowWin = False
        for row in self.board:
            if sum(row) == 15:
                rowWin = True
        return rowWin
                    
    def colWin(self):
        # Considering column win
        colWin = False
        for col_index in range(0,self.size):
            column = []
            for row_index in range(0,self.size):
                num = self.board[row_index][col_index]
                column.append(num)
            if sum(column) == 15:
                colWin = True
        return colWin
    
    def diagonalWin(self):
        # Checks for a diagonal win
        diagonal_1 = []
        diagonal_2 = []
        for index in range(0,self.size):
            # Left to right diagonal
            num = self.board[index][index]
            diagonal_1.append(num)
            
            # Right to left diagonal
            num = self.board[index][self.size-1-index]
            diagonal_2.append(num)
        if sum(diagonal_1) == 15 or sum(diagonal_2) == 15:
            return True
        else:
            return False
        
    def play(self):
        while self.continue_game == True:
            self.drawBoard()
            self.handle_events()
            result = self.decide_continue()
            return result
                
    def handle_events(self):
        if self.turn == self.player_1:
            num = int(input('Player 1, please enter an odd number (1-9): '))
            while num % 2 == 0:
                num = int(input('Player 1, please enter an odd number (1-9): '))
                
            while num >= 10:
                num = int(input('Player 1, please enter an odd number (1-9): '))
                
            while num in self.entered_num:
                num = int(input('Player 1, please enter an odd number (1-9): '))
            
            row = int(input('Player 1, please enter a row: '))
            col = int(input('Player 1, please enter a column: '))
            while not self.squareIsEmpty(row, col):
                row = int(input('Player 1, please enter a row: '))
                col = int(input('Player 1, please enter a column: '))
            
        else:
            num = int(input('Player 2, please enter an even number (1-9): '))
            while num % 2 != 0:
                num = int(input('Player 1, please enter an even number (1-9): '))
            
            while num >= 10:
                num = int(input('Player 1, please enter an odd number (1-9): '))            
                
            while num in self.entered_num:
                num = int(input('Player 1, please enter an even number (1-9): '))
            
            row = int(input('Player 2, please enter a row: '))
            col = int(input('Player 2, please enter a column: '))
            while not self.squareIsEmpty(row, col):
                row = int(input('Player 2, please enter a row: '))
                col = int(input('Player 2, please enter a column: '))
            
        if self.update(row, col, num):
            self.entered_num.append(num)
            self.change_turn()            

    
    def change_turn(self):
        if self.turn == self.player_1:
            self .turn = self.player_2
        else:
            self.turn = self.player_1
    
    def decide_continue(self):       
        if self.isWinner() or self.isTie():
            self.continue_game = False
    
        if self.isWinner():
            self.drawBoard()
            self.change_turn()
            print(self.turn, end = '')
            print(' wins. Congrats!')
            return True
            
        if self.isTie():
            self.drawBoard()
            print('It was a tie')
            return False
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: True
        '''
        # TO DO: delete pass (and this comment) and complete method
        pass        
   
   
   
   
   
    
    
class ClassicTicTacToe:
    def __init__(self, player_1, player_2):
        '''
        Initializes an empty Numerical Tic Tac Toe board.
        Inputs: none
        Returns: None
        '''       
        self.board = [] # list of lists, where each internal list represents a row
        self.size = 3   # number of columns and rows of board
        self.entered = 0
        self.board_type = 'Classical'
        
        # populate the empty squares in board with 0
        for i in range(self.size):
            row = []
            for j in range(self.size):
                row.append(' ')
            self.board.append(row)
            
        self.entered_num = []
        self.player_1 = player_1
        self.player_2 = player_2
        self.turn = self.player_1
        self.continue_game = True 
        
                                
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indicies shown.
        Inputs: none
        Returns: None
        '''
        # e.g. an empty board should look like this:
        #    0   1   2  
        # 0    |   |   
        #   -----------
        # 1    |   |   
        #   -----------
        # 2    |   |           
                 
        border = '|'
        dashes = '-'
        print('   ','0','  ','1','  ', '2',sep = ' ')
        print('0', self.board[0][0], border, self.board[0][1], border,self.board[0][2], sep = '  ')
        print('  ', dashes*13)
        print('1', self.board[1][0], border, self.board[1][1], border,self.board[1][2], sep = '  ')
        print('  ', dashes*13)
        print('2', self.board[2][0], border, self.board[2][1], border,self.board[2][2], sep = '  ')    

    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square is empty, or if it already contains a number 
        greater than 0.
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is empty; False otherwise
        '''
        if self.board[row][col] == ' ':
            return True
        else:
            return False 
        
    def update(self, row, col, mark):
        '''
        Assigns the integer, num, to the board at the provided row and column, 
        but only if that square is empty.
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           num (int) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col):
            self.board[row][col] = mark
            self.entered += 1
            return True
        else:
            return False
                
    def boardFull(self):
        '''
        Checks if the board has any remaining empty squares.
        Inputs: none
        Returns: True if the board has no empty squares (full); False otherwise
        '''
        full = True
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 0:
                    full = False
        return full
                      
    def isTie(self):
        # Checks to see if there is a tie and returns True if there is a tie
        if self.entered == 9:
            return True
        else:
            return False
        
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) that 
        are all X's or O's. That line can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        if self.rowWin() or self.colWin() or self.diagonalWin():
            return True
        else:
            return False
             
    def rowWin(self):
        # Considering a row win
        rowWin = False
        for row in self.board:
            if self.is_same(row):
                rowWin = True
        return rowWin
                    
    def colWin(self):
        # Considering column win
        colWin = False
        for col_index in range(0,self.size):
            column = []
            for row_index in range(0,self.size):
                num = self.board[row_index][col_index]
                column.append(num)
            if self.is_same(column):
                colWin = True
        return colWin
    
    def diagonalWin(self):
        # Checks for a diagonal win
        diagonal_1 = []
        diagonal_2 = []
        for index in range(0,self.size):
            # Left to right diagonal
            num = self.board[index][index]
            diagonal_1.append(num)
            
            # Right to left diagonal
            num = self.board[index][self.size-1-index]
            diagonal_2.append(num)
        if self.is_same(diagonal_1) or self.is_same(diagonal_2):
            return True
        else:
            return False
        
    def is_same(self, alist):
        first = alist[0]
        index = 1
        same = True
        if first != ' ':
            while index < len(alist) and same:
                if alist[index] != first:
                    same = False
                index += 1
        else:
            same = False
            
        return same 
        
    def play(self):
        while self.continue_game == True:
            self.drawBoard()
            self.handle_events()
            self.decide_continue()
            
                
    def handle_events(self):
        if self.turn == self.player_1:
            mark = 'X'
            row = int(input('Player 1, please enter a row: '))
            col = int(input('Player 1, please enter a column: '))
            
            while not self.squareIsEmpty(row, col):
                row = int(input('Player 1, please enter a row: '))
                col = int(input('Player 1, please enter a column: '))
            
        else:
            mark = 'O'
            row = int(input('Player 2, please enter a row: '))
            col = int(input('Player 2, please enter a column: '))    
            
            while not self.squareIsEmpty(row, col):
                row = int(input('Player 2, please enter a row: '))
                col = int(input('Player 2, please enter a column: '))
            
        if self.update(row, col, mark):
            self.change_turn()            

    
    def change_turn(self):
        if self.turn == self.player_1:
            self .turn = self.player_2
        else:
            self.turn = self.player_1
    
    def decide_continue(self):       
        if self.isWinner() or self.isTie():
            self.continue_game = False
    
        if self.isWinner():
            self.drawBoard()
            self.change_turn()
            print(self.turn, end = '')
            print(' wins. Congrats!')
            
            
        if self.isTie():
            self.drawBoard()
            print('It was a tie')
            
    
    def isNum(self):
        '''
        Checks whether this is a Numerical Tic Tac Toe board or not
        Inputs: none
        Returns: False
        '''
        # TO DO: delete pass (and this comment) and complete method
        pass     





class MetaTicTacToe:
    def __init__(self, configFile):
        '''
        Initializes an empty Meta Tic Tac Toe board, based on the contents of a 
        configuration file.
        Inputs: 
           configFile (str) - name of a text file containing configuration information
        Returns: None
        '''       
        self.size = 3
        self.board = []
        file = open(configFile, 'r')
        for line in file:
            line = line.strip()
            line = line.split()
            self.board.append(line)  
        file.close()
        
        self.entered = 0
        self.entered_num = []
        self.player_1 = 'Player 1'
        self.player_2 = 'Player 2'
        self.turn = self.player_1
        self.continue_game = True            
             
    def drawBoard(self):
        '''
        Displays the current state of the board, formatted with column and row 
        indices shown.
        Inputs: none
        Returns: None
        '''
        border = '|'
        dashes = '-'
        print('   ','0','  ','1','  ', '2',sep = ' ')
        print('0', self.board[0][0], border, self.board[0][1], border,self.board[0][2], sep = '  ')
        print('  ', dashes*13)
        print('1', self.board[1][0], border, self.board[1][1], border,self.board[1][2], sep = '  ')
        print('  ', dashes*13)
        print('2', self.board[2][0], border, self.board[2][1], border,self.board[2][2], sep = '  ')


    def squareIsEmpty(self, row, col):
        '''
        Checks if a given square contains a non-played local game board ("empty"),
        or the result of a played local game board (not "empty").
        Inputs:
           row (int) - row index of square to check
           col (int) - column index of square to check
        Returns: True if square is "empty"; False otherwise
        '''
        if self.board[row][col] == 'c' or self.board[row][col] == 'n':
            return True
        else:
            return False 
    
    
    def update(self, row, col, result):
        '''
        Assigns the string, result, to the board at the provided row and column, 
        but only if that square is "empty".
        Inputs:
           row (int) - row index of square to update
           col (int) - column index of square to update
           result (str) - entry to place in square
        Returns: True if attempted update was successful; False otherwise
        '''
        if self.squareIsEmpty(row,col):
            self.board[row][col] = result
            self.entered += 1
            return True
        else:
            return False
    
    
    def boardFull(self):
        '''
        Checks if the board has any remaining "empty" squares (i.e. any un-played
        local boards).
        Inputs: none
        Returns: True if the board has no "empty" squares (full); False otherwise
        '''
        full = True
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                if self.board[i][j] == 'c' or self.board[i][j] == 'n':
                    full = False
        return full
        
           
    def isWinner(self):
        '''
        Checks whether the current player has just made a winning move.  In order
        to win, the player must have just completed a line (of 3 squares) of their
        mark (three Xs for Player 1, three Os for Player 2), or 3 draws. That line
        can be horizontal, vertical, or diagonal.
        Inputs: none
        Returns: True if current player has won with their most recent move; 
                 False otherwise
        '''
        if self.rowWin() or self.colWin() or self.diagonalWin():
            return True
        else:
            return False 
        
    def isTie(self):
        # Checks to see if there is a tie and returns True if there is a tie
        if self.entered == 9:
            return True
        else:
            return False
        
        
    def rowWin(self):
        # Considering a row win
        rowWin = False
        for row in self.board:
            if self.is_same(row):
                rowWin = True
        return rowWin
                    
    def colWin(self):
        # Considering column win
        colWin = False
        for col_index in range(0,self.size):
            column = []
            for row_index in range(0,self.size):
                num = self.board[row_index][col_index]
                column.append(num)
            if self.is_same(column):
                colWin = True
        return colWin
    
    def diagonalWin(self):
        # Checks for a diagonal win
        diagonal_1 = []
        diagonal_2 = []
        for index in range(0,self.size):
            # Left to right diagonal
            num = self.board[index][index]
            diagonal_1.append(num)
            
            # Right to left diagonal
            num = self.board[index][self.size-1-index]
            diagonal_2.append(num)
        if self.is_same(diagonal_1) or self.is_same(diagonal_2):
            return True
        else:
            return False
        
    def is_same(self, alist):
        first = alist[0]
        index = 1
        same = True
        if first != 'c' and first != 'n':
            while index < len(alist) and same:
                if alist[index] != first:
                    same = False
                index += 1
        else:
            same = False
            
        return same 
    
    def getLocalBoard(self, row, col, player_1, player_2):
        '''
        Returns the instance of the empty local board at the specified row, col 
        location (i.e. either ClassicTicTacToe or NumTicTacToe).
        Inputs:
           row (int) - row index of square
           col (int) - column index of square
        Returns: instance of appropriate empty local board if un-played; 
                 None if local board has already been played
        '''
        if self.board[row][col] != 'c' and self.board[row][col] != 'n':      
            return None
        else:
            if self.board[row][col] == 'c':
                classic = ClassicTicTacToe(player_1, player_2)
                #classic.play()
                #result = classic.isWinner()
                return classic
            else:
                numerical = NumTicTacToe(player_1, player_2)
                #numerical.play()
                #result = numerical.isWinner()
                return numerical
            
            
            
            
            
    def play(self):
        while self.continue_game == True:
            self.drawBoard()
            self.handle_events()
            self.decide_continue()
                
    def handle_events(self):
        if self.turn == self.player_1:
            mark = 'X'
            row = int(input('Player 1, please enter a row: '))
            col = int(input('Player 1, please enter a column: '))
            
            while not self.squareIsEmpty(row, col):
                row = int(input('Player 1, please enter a row: '))
                col = int(input('Player 1, please enter a column: '))
            
        else:
            mark = 'O'
            row = int(input('Player 2, please enter a row: '))
            col = int(input('Player 2, please enter a column: '))    
            
            while not self.squareIsEmpty(row, col):
                row = int(input('Player 2, please enter a row: '))
                col = int(input('Player 2, please enter a column: '))
    
        #local_game = self.getLocalBoard(row, col)
        #local_game.play()
        #result = local_game.isWinner()
        
        if self.turn == 'Player 1':
            print('Entered 1')
            local_game = self.getLocalBoard(row, col, self.player_1, self.player_2)
            local_game.play()
            result = local_game.isWinner()  
        else:
            print('Entered 2')
            local_game = self.getLocalBoard(row, col, self.player_2, self.player_1)
            local_game.play()
            result = local_game.isWinner()                   
        
        if result == True:
            if self.update(row, col, mark):
                self.change_turn() 
        else:
            if self.update(row, col, 'D'):
                self.change_turn()            
    
    
    def change_turn(self):
        if self.turn == self.player_1:
            self .turn = self.player_2
        else:
            self.turn = self.player_1
    
    def decide_continue(self):       
        if self.isWinner() or self.isTie():
            self.continue_game = False
    
        if self.isWinner():
            self.drawBoard()
            self.change_turn()
            print(self.turn, end = '')
            print(' wins. Congrats!')
            
        if self.isTie():
            self.drawBoard()
            print('It was a tie')        
                
def main():
    uttt = MetaTicTacToe('MetaTTTconfig.txt')
    uttt.play()

if __name__ == "__main__":


    main()
