#Author: Stephen Bernauer 
#Midterm Project: Udemy Python Course 
#Date: 8/5/20
#interactive game of tiktactoe 

import time 
import os 

#clear function to clear the board
def clear():
	os.system( 'cls' )


#game board: function calls the rows, which at the start of the game are empty 
#will be appending the list to play tiktaktoe 

def my_board(row1,row2,row3):
	print(row1)
	print(row2)
	print(row3)

row1=[' ',' ',' ']
row2=[' ',' ',' ']
row3=[' ',' ',' ']

my_board(row1,row2,row3)
clear()
#user chooses player names 
player1 =input('Enter a name for player1: ')
print('player 1 is '+player1)
player2 =input('Enter a name for player2: ')
print('player 2 is '+player2)
clear()
#