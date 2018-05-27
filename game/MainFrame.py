__author__="Hazem Elmasry @ZyptosKid"

import Siga as Siga
import TicTacToe as Tic
import RocketCollider as Rc
from time import sleep



print('Welcome to our game!\n')

print('3x3 is a game project that consists of 3 board games made by 3 students.')
print('The games share a 3x3 grid layout too. Hence the name.\n')

print('One of the games is the famous tic tac toe (By Adham 1710056), \nthe second is the beloved traditional egyptian game \'Siga\' (By Hazem 1710653), \nand the third is an original game that we created from scratch called \'Rocket Collider\'. (By Mahmoud 1710472) ')

print('We hope you enjoy your time playing!\n\n\n')


Y = {'Y', 'y', 'yes', 'Yes', 'YES'}
N = {'N', 'n', 'no', 'No', 'NO', 'quit', 'QUIT', 'Quit'}

Valid = True

# Program runner
while True:

	answer = input('Do you want to play one of our three games? [Y/ N=quit]:  ')

	while Valid:

		if answer in N:

			sleep(1)
			print('See you!')

			quit()

		elif answer in Y:

			print()
			print('Which game do you want to play?')
			print('Choose a number from the following list:\n')
			print('		[1] Tic Tac Toe')
			print('		[2] Siga')
			print('		[3] Rocket Collider')
			print('		[*] Any other choice = leave to main\n\n')

			answer = input('- I want to play:  ')

			answerOptions = {
				1:{'tic tac toe','tictactoe','tictac toe','tic tactoe'},
				2:{'siga','seega','sega'},
				3:{'rocket collider','rocketcollider','roket colider','rocket colider','roket collider'}
			}

			if answer == '1' or answer.lower() in answerOptions[1]:
				Tic.runGame()
			elif answer == '2' or answer.lower() in answerOptions[2]:
				Siga.runGame()
			elif answer == '3' or answer.lower() in answerOptions[3]:
				Rc.runGame()
			else:
				Valid = False
				break		
			
			answer = input('Wanna play again? [Y/ N=quit]:  ')

			if answer in Y:
				print()
				print('Alright! Another round!')
				continue
			elif answer in N:
				print()
				print('Hope you enjoyed!')
				break
			else:
				Valid = False
				break
		
		else:
			Valid = False

	if not Valid: 	
		print ('Undecided. Returning to main...\n')
		Valid = True
