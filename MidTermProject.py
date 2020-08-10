#Author: Stephen Bernauer 
#Midterm Project: Udemy Python Course 
#Date: 8/5/20
#interactive game of tiktactoe (2 human players) 

import random	
from time import sleep

#user chooses player names 
player1 =input('Enter a name for player1: ')
print('player 1 is '+player1)
player2 =input('Enter a name for player2: ')
print('player 2 is '+player2)

print('\n'*5)

#player chooses a marker
def player_input():
	
	marker = ' '

	while marker not in ['X', 'O']:
		marker = input(player1 + ' do you want to be X\'s or O\'s ?').upper()
		if marker not in ['X','O']:
			print('I am sorry, would you like to be X\'s or O\'s ?')	
		elif marker == 'X': 
			return('X','O')
		else:	
			return('O','X')

player_input()

#clear screen
print('\n'*5)

#Game Board  
#board is made of dictoinaries, set around a number keypad: 
#789
#456
#123
my_board={
	'7':' ','8':' ','9':' ',
	'4':' ','5':' ','6':' ',
	'1':' ','2':' ','3':' ',
	}
def the_board():
	print(my_board['7'] + '|' + my_board['8'] + ' |' + my_board['9'])
	print('-+--+-')
	print(my_board['4'] + '|' + my_board['5'] + ' |' + my_board['6'])
	print('-+--+-')
	print(my_board['1'] + '|' + my_board['2'] + ' |' + my_board['3'])

the_board()

#THIS IF STATEMENT WILL BE CHANGED AND ADDED INTO THE GAME FUNCTION

#check if there is a winner 
#def win_check(board,mark):
    
#   return ((board['7'] == mark and board['8'] == mark and board['9'] == mark) or # across the top
#   (board['4'] == mark and board['5'] == mark and board['6'] == mark) or # across the middle
#   (board['1'] == mark and board['2'] == mark and board['3'] == mark) or # across the bottom
#   (board['7'] == mark and board['4'] == mark and board['1'] == mark) or # down the middle
#   (board['8'] == mark and board['5'] == mark and board['2'] == mark) or # down the middle
#   (board['9'] == mark and board['6'] == mark and board['3'] == mark) or # down the right side
#   (board['7'] == mark and board['5'] == mark and board['3'] == mark) or # diagonal
#   (board['9'] == mark and board['5'] == mark and board['1'] == mark)) # diagonal

#there is an error here somewhere 
#if win_check(my_board,'X') == True 
#	print("WINNER 'X'")
#if win_check(my_board,'O') == True
#	print("'WINNER 'O'")

#clear screen
print('\n'*5)

#this function runs the game.
def game():

	turnz = random.choice(range[1-3]) #random turn assignment #CURRENTLY AN ERROR HERE 
	print('it is player'+turnz +'turn') 
	count = 0 

	for n in range(10):
		the_board()
		print("Where would you like to play?")

		move = input()

		if the_board[move] == ' ':
			the_board[move].update(move = turn) 
			count += 1

		else: 
			print('That spot is already been taken.\n Where would you like to play?')
	
		#if count > 5 

#def replay():
	#   return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')
print('GAME TIME:')
game()