#!/usr/bin/env python3

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
the_board={
	'7':' ','8':' ','9':' ',
	'4':' ','5':' ','6':' ',
	'1':' ','2':' ','3':' ',
	}
def print_the_board(board):
	print(board['7'] + '|' + board['8'] + ' |' + board['9'])
	print('-+--+-')
	print(board['4'] + '|' + board['5'] + ' |' + board['6'])
	print('-+--+-')
	print(board['1'] + '|' + board['2'] + ' |' + board['3'])

#print_the_board(board)

#clear screen 5 lines 
print('\n'*5)

#this function runs the game.
def game():

    turn = 'X'
    count = 0


    for i in range(10):
        print_the_board(the_board)
        print("It's your turn," + turn + ". Where would you line to go?")

        move = input()        

        if the_board[move] == ' ':
            the_board[move] = turn
            count += 1
        else:
            print("That place is already filled.\nMove to which place?")
            continue

        # Now we will check if player X or O has won,for every move after 5 moves. 
        if count >= 5:
            if the_board['7'] == the_board['8'] == the_board['9'] != ' ': # across the top
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")                
                break
            elif the_board['4'] == the_board['5'] == the_board['6'] != ' ': # across the middle
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif the_board['1'] == the_board['2'] == the_board['3'] != ' ': # across the bottom
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif the_board['1'] == the_board['4'] == the_board['7'] != ' ': # down the left side
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif the_board['2'] == the_board['5'] == the_board['8'] != ' ': # down the middle
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif the_board['3'] == the_board['6'] == the_board['9'] != ' ': # down the right side
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
            elif the_board['7'] == the_board['5'] == the_board['3'] != ' ': # diagonal
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break
            elif the_board['1'] == the_board['5'] == the_board['9'] != ' ': # diagonal
                print_the_board(the_board)
                print("\nGame Over.\n")                
                print(" **** " +turn + " won. ****")
                break 
        #Tie Game
        if count == 9: 
        	print('\nGame Over.\n')
        	print('Cats Game')

        #change player turn
        if turn == 'X':
        	turn = 'O'
        else: 
        	turn = 'X'


print('GAME TIME: \n use the number pad to chose a place.')
game()
