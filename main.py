# This program runs the Ultimat Meta Tic Tac Toe game.
from UltimateMetaTTT import NumTicTacToe
from UltimateMetaTTT import ClassicTicTacToe
from UltimateMetaTTT import MetaTicTacToe

def main():
    
    game = MetaTicTacToe('MetaTTTconfig.txt')
    player_1 = 'Player 1'
    player_2 = 'Player 2'
    turn = player_1
    continue_game = True
    entered = 0
    
    def play():
        # Runs the game
        while continue_game == True:
            game.drawBoard()
            handle_events()
            decide_continue()
                
    def handle_events():
        nonlocal entered
        if turn == player_1:
            mark = 'X'
            row = int(input('Player 1, please enter a row: '))
            # Ensuring the correect row no. input
            while row > 2 or row < 0:
                row = int(input('Error: row not in correct range. Player 1, please enter a row: '))
                
            col = int(input('Player 1, please enter a column: '))
            # Ensuring the correect row no. input
            while col > 2 or col < 0:
                col = int(input('Error: column not in correct range. Player 1, please enter a col: ')) 
            
            # Ensuring that an empty square is selected
            while not game.squareIsEmpty(row, col):
                row = int(input('Player 1, please enter a row: '))
                col = int(input('Player 1, please enter a column: '))
            
        else:
            mark = 'O'
            row = int(input('Player 2, please enter a row: '))
            # Ensuring the correect row no. input
            while row > 2 or row < 0:
                row = int(input('Error: row not in correct range. Player 2, please enter a row: '))
                
            col = int(input('Player 2, please enter a column: '))
            # Ensuring the correect row no. input
            while col > 2 or col < 0:
                col = int(input('Error: column not in correct range. Player 2, please enter a col: '))    
            
            # Ensuring that an empty square is selected
            while not game.squareIsEmpty(row, col):
                row = int(input('Player 2, please enter a row: '))
                col = int(input('Player 2, please enter a column: '))
                        
        
        # Handling the local game
        local_game = game.getLocalBoard(row,col)
        if local_game.isNum() == True:
            # Local game is NumTicTacToe
            print('-' * 40)
            print('This is a Numerical Tic Tac Toe.')
            result, local_winner = num_play(local_game,turn)
        else:
            # Local game is ClassicTicTacToe
            print('-' * 40)
            print('This is a Classic Tic Tac Toe.')
            result, local_winner = classic_play(local_game,turn)

        
        # Making the necessary update based on the result of the local game
        if result == True:
            if turn == 'Player 1':
                if local_winner == 'Player 1':
                    if game.update(row, col, 'X'):
                        change_turn() 
                else:
                    if game.update(row, col, 'O'):
                        change_turn() 
            else: # Turn is of Player 2
                if local_winner == 'Player 1':
                    if game.update(row, col, 'X'):
                        change_turn() 
                else:
                    if game.update(row, col, 'O'):
                        change_turn()                
                 
        else:
            if game.update(row, col, 'D'):
                change_turn()             
        entered += 1        
                
    def change_turn():
        # Changes the turn of the player
        nonlocal turn
        if turn == player_1:
            turn = player_2
        else:
            turn = player_1
    
    def decide_continue(): 
        # Decides on whether to continue with the game
        nonlocal continue_game
        nonlocal entered
        if game.isWinner() or entered == 9:
            continue_game = False
    
        if game.isWinner():
            game.drawBoard()
            change_turn()
            print(turn, end = '')
            print(' wins the Meta Tic Tac Toe game. GOOD GAME!')
        elif entered == 9:
            game.drawBoard()
            print('It was a tie')    
   
    play()
    
    
#-------------------------------------------------------------------------------
# ClassicTicTacToe
def classic_play(game, player_turn):
    
    player_1 = 'Player 1'
    player_2 = 'Player 2'
    turn = player_turn
    cl_continue_game = True
    i = 0
    entered = 0
    
    def cl_play():
        # Runs the local game
        while cl_continue_game == True:
            game.drawBoard()
            cl_handle_events()
            cl_decide_continue()

        return cl_result()
               
    def cl_handle_events():
        nonlocal i
        nonlocal entered
        if turn == player_1:
            row = int(input('Player 1, please enter a row: '))
            # Ensuring the correect row no. input
            while row > 2 or row < 0:
                row = int(input('Error: row not in correct range. Player 1, please enter a row: '))
                
            col = int(input('Player 1, please enter a column: '))
            # Ensuring the correect row no. input
            while col > 2 or col < 0:
                col = int(input('Error: column not in correct range. Player 1, please enter a col: '))            
                
            # Ensuring an empty square is chosen
            while not game.squareIsEmpty(row, col):
                print('Error: could not make move!')
                game.drawBoard()
                row = int(input('Player 1, please enter a row: '))
                # Ensuring the correect row no. input
                while row > 2 or row < 0:
                    row = int(input('Error: row not in correct range. Player 1, please enter a row: '))
                    
                col = int(input('Player 1, please enter a column: '))
                # Ensuring the correect row no. input
                while col > 2 or col < 0:
                    col = int(input('Error: column not in correct range. Player 1, please enter a col: '))
            
        else:
            row = int(input('Player 2, please enter a row: '))
            # Ensuring the correect row no. input
            while row > 2 or row < 0:
                row = int(input('Error: row not in correct range. Player 2, please enter a row: '))
                
            col = int(input('Player 2, please enter a column: '))
            # Ensuring the correect row no. input
            while col > 2 or col < 0:
                col = int(input('Error: column not in correct range. Player 2, please enter a col: '))             
            
            # Ensuring an empty square is chosen
            while not game.squareIsEmpty(row, col):
                print('Error: could not make move!')
                game.drawBoard()
                row = int(input('Player 2, please enter a row: '))
                # Ensuring the correect row no. input
                while row > 2 or row < 0:
                    row = int(input('Error: row not in correct range. Player 2, please enter a row: '))
                    
                col = int(input('Player 2, please enter a column: '))
                # Ensuring the correect row no. input
                while col > 2 or col < 0:
                    col = int(input('Error: column not in correct range. Player 2, please enter a col: ')) 
        
        # Ensuring that the first player always is represented by X
        if i % 2 == 0:
            mark = 'X'
            i += 1
        else:
            mark = 'O'
            i += 1
           
        if game.update(row, col, mark):
            cl_change_turn()            
            entered += 1
    
    def cl_change_turn():
        # Changes the turn of the player
        nonlocal turn
        if turn == player_1:
            turn = player_2
        else:
            turn = player_1
    
    def cl_decide_continue(): 
        # Decides to whether continue with the game
        nonlocal entered
        nonlocal cl_continue_game
        if game.isWinner() or entered == 9:
            cl_continue_game = False
    
        if game.isWinner():
            game.drawBoard()
            cl_change_turn()
            print(turn, end = '')
            print(' wins. Congrats!')
        elif entered == 9:
            game.drawBoard()
            print('It was a tie')
    
    def cl_result():
        # Result a bool value for the winner of the game. True is game is won.
        return game.isWinner()
   
    return cl_play(), turn
#-------------------------------------------------------------------------------


#-------------------------------------------------------------------------------
# NumTicTacToe
def num_play(game, player_turn):
    
    player_1 = 'Player 1'
    player_2 = 'Player 2'
    turn = player_1
    meta_turn = player_turn
    continue_game = True
    entered_num = []
    entered = 0
    
    def n_play():
        while continue_game == True:
            game.drawBoard()
            n_handle_events()
            n_decide_continue()
            
        return n_result()
                
    def n_handle_events():
        nonlocal entered
        if meta_turn == 'Player 1':
            if turn == player_1:
                num = int(input('Player 1, please enter an odd number (1-9): '))
                while num % 2 == 0 or num >= 10 or num <= 0:
                    num = int(input('Error: entry not odd. Player 1, please enter an odd number (1-9): '))
                    
                while num in entered_num:
                    num = int(input('Error: that number has already been entered. Player 1, please enter an odd number (1-9): '))
                
                # Getting the row and col input
                row = int(input('Player 1, please enter a row: '))
                # Ensuring the correct input
                while row > 2 or row < 0:
                    row = int(input('Error: row not in correct range. Player 1, please enter a row: '))                
                col = int(input('Player 1, please enter a column: '))
                # Ensuring the correct input
                while row > 2 or row < 0:
                    col = int(input('Error: col not in correct range. Player 1, please enter a column: ')) 
                    
                # Ensuring an empty square is selected
                while not game.squareIsEmpty(row, col):
                    row = int(input('Player 1, please enter a row: '))
                    # Ensuring the correct input
                    while row > 2 or row < 0:
                        row = int(input('Error: row not in correct range. Player 1, please enter a row: '))                
                    col = int(input('Player 1, please enter a column: '))
                    # Ensuring the correct input
                    while col > 2 or col < 0:
                        col = int(input('Error: col not in correct range. Player 1, please enter a column: ')) 
                
            else:
                num = int(input('Player 2, please enter an even number (1-9): '))
                while num % 2 != 0 or num >= 10 or num <= 0:
                    num = int(input('Error: entry not even. Player 2, please enter an even number (1-9): '))           
                    
                while num in entered_num:
                    num = int(input('Error: that number has already been entered. Player 2, please enter an even number (1-9): '))
                
                # Getting the row and col input
                row = int(input('Player 2, please enter a row: '))
                # Ensuring the correct input
                while row > 2 or row < 0:
                    row = int(input('Error: row not in correct range. Player 2, please enter a row: '))                 
                col = int(input('Player 2, please enter a column: '))
                # Ensuring the correct input
                while col > 2 or col < 0:
                    col = int(input('Error: col not in correct range. Player 2, please enter a col: '))  
                
                # Ensuring an empty suare is chosen
                while not game.squareIsEmpty(row, col):
                    row = int(input('Player 2, please enter a row: '))
                    # Ensuring the correct input
                    while row > 2 or row < 0:
                        row = int(input('Error: row not in correct range. Player 2, please enter a row: '))                 
                    col = int(input('Player 2, please enter a column: '))
                    # Ensuring the correct input
                    while col > 2 or col < 0:
                        col = int(input('Error: col not in correct range. Player 2, please enter a col: '))  
                    
        else:
            if turn == player_1:
                num = int(input('Player 2, please enter an odd number (1-9): '))
                while num % 2 == 0 or num >= 10 or num <= 0:
                    num = int(input('Error: entry not odd. Player 2, please enter an odd number (1-9): '))

                while num in entered_num:
                    num = int(input('Error: that number has already been entered. Player 2, please enter an odd number (1-9): '))
                
                # Getting the row and col input
                row = int(input('Player 2, please enter a row: '))
                # Ensuring the correct input
                while row > 2 or row < 0:
                    row = int(input('Error: row not in correct range. Player 2, please enter a row: '))                 
                col = int(input('Player 2, please enter a column: '))
                # Ensuring the correct input
                while col > 2 or col < 0:
                    col = int(input('Error: col not in correct range. Player 2, please enter a col: '))  
                
                # Ensuring an empty suare is chosen
                while not game.squareIsEmpty(row, col):
                    row = int(input('Player 2, please enter a row: '))
                    # Ensuring the correct input
                    while row > 2 or row < 0:
                        row = int(input('Error: row not in correct range. Player 2, please enter a row: '))                 
                    col = int(input('Player 2, please enter a column: '))
                    # Ensuring the correct input
                    while col > 2 or col < 0:
                        col = int(input('Error: col not in correct range. Player 2, please enter a col: '))
                
            else:
                num = int(input('Player 1, please enter an even number (1-9): '))
                while num % 2 != 0 or num >= 10 or num <= 0:
                    num = int(input('Error: entry not even. Player 1, please enter an even number (1-9): '))     
                    
                while num in entered_num:
                    num = int(input('Error: that number has already been entered. Player 1, please enter an even number (1-9): '))
                
                # Getting the row and col input
                row = int(input('Player 1, please enter a row: '))
                # Ensuring the correct input
                while row > 2 or row < 0:
                    row = int(input('Error: row not in correct range. Player 1, please enter a row: '))                
                col = int(input('Player 1, please enter a column: '))
                # Ensuring the correct input
                while row > 2 or row < 0:
                    col = int(input('Error: col not in correct range. Player 1, please enter a column: ')) 
                    
                # Ensuring an empty square is selected
                while not game.squareIsEmpty(row, col):
                    row = int(input('Player 1, please enter a row: '))
                    # Ensuring the correct input
                    while row > 2 or row < 0:
                        row = int(input('Error: row not in correct range. Player 1, please enter a row: '))                
                    col = int(input('Player 1, please enter a column: '))
                    # Ensuring the correct input
                    while col > 2 or col < 0:
                        col = int(input('Error: col not in correct range. Player 1, please enter a column: '))           
              
        if game.update(row, col, num):
            entered_num.append(num)
            n_change_turn() 
            entered += 1

    def n_change_turn():
        nonlocal turn
        if turn == player_1:
            turn = player_2
        else:
            turn = player_1
    
    def n_decide_continue(): 
        # Deciedes whether game should continue
        nonlocal continue_game
        nonlocal entered 
        if game.isWinner() or entered == 9:
            continue_game = False
    
        if game.isWinner():
            game.drawBoard()
            n_change_turn()
            print(turn, end = '')
            print(' wins. Congrats!')  
        elif entered == 9:
            game.drawBoard()
            print('It was a tie')  
            
    def n_result():
        # Result a bool value for the winner of the game. True is game is won.
        return game.isWinner()

    return n_play(), turn
#-------------------------------------------------------------------------------

def play_again():
        # Prompts player to play again
        main_continue_game = True
        reply = input('Do you want to play another game? (Y/N)')
        if reply.lower() != 'y':
            main_continue_game = False      
        return main_continue_game 

    
if __name__ == "__main__":
    main_continue_game = True
    while main_continue_game:
        main()
        main_continue_game = play_again()
        
    print('Thanks for playing! Goodbye.')