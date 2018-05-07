import Siga
import TicTacToe as Tic
import RocketCollider as Rocket
from time import sleep

Y = {'Y', 'y', 'yes', 'Yes', 'YES'}
N = {'N', 'n', 'no', 'No', 'NO'}

print('Welcome to our game!\n')

print('3x3 is a game project that consists of 3 board games made by 3 students.')
print('The games share a 3x3 grid layout too. Hence the name.\n')

print('One of the games is the famous tic tac toe, \nthe second is the beloved traditional egyptian game \'Siga\', \nand the third is an original game that we created from scratch called \'Rocket Collider\'. ')

print('We hope you enjoy your time playing!\n\n\n')

Valid = True

while True:

	answer = input('Do you want to play one of our three games? [Y/N]:  ')

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
			print('		[3] Rocket Collider\n\n')

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
				Rocket.runGame()
			else:
				Valid = False
				break		
			
			answer = input('Wanna play again? [Y/N]:  ')

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
		print ('That\'s not a valid answer!\n')
		Valid = True
