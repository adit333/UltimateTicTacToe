# UltimateTicTacToe
UTTT is a 3*3 TicTacToe board but each square represents another TicTacToe game on its own. So, 9 individual games!

Ultimate tic-tac-toe is a board game composed of nine tic-tac-toe boards arranged in a 3 × 3 grid.
Players take turns playing in the smaller tic-tac-toe boards until one of them wins in the larger tic-tac-toe board.
The twist in this game however, is that the 3*3 grid is made with a mixture of Numerical Tic Tac Toe and
Classical Tic Tac Toe. Each player choses a square in the Meta board and the players than zoom in to that square
chosen by the player. The player that chose the square in the Meta board becomes Player 1 in the square i.e. the mini game 
in the square. 
At the end, the player that wins overall is one that finishes a diagonal, horizontal or vertical square with the third win.
A player can also win overall, if the player finishes the third square with a draw and the entire diagonal, horizontal
or vertical is a draw.

This game has been implemented in two ways:
1) The first approach used a full Object Oriented approach with all the code encapsualted in three classes.
    One class to deal with the Numerical Tic Tac Toe game, another to deal with Classical Tic Tac Toe.
    The third class deals with the entire game flow i.e. MetaTicTacToe.
2) The second approach uses a partial OOP approach and a partaial functional programming approach. 
    The code for this approach is implemented across 2 files: UltimateMetaTTT_Partial_OOP.py and main.py
