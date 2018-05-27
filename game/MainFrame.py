__author__="Hazem Elmasry @ZyptosKid"

import Siga as Siga
import TicTacToe as Tic
import RocketCollider as Rc
from time import sleep
from os import path, chdir



print('Welcome to our game!\n')

print('3x3 is a game project that consists of 3 board games made by 3 students.')
print('The games share a 3x3 grid layout too. Hence the name.\n')

print('One of the games is the famous tic tac toe (By Adham 1710056), \nthe second is the beloved traditional egyptian game \'Siga\' (By Hazem 1710653), \nand the third is an original game that we created from scratch called \'Rocket Collider\'. (By Mahmoud 1710472) ')

print('We hope you enjoy your time playing!\n\n\n')

# Options to choose from later on, static set variables
Y = Siga.Y
N = Siga.N
Q = Siga.Q
Valid = True # Checker for the validity of answer, makes sure the loop continues on invalid answer

# The Program Runner loop, only useful when answer is undecided. Falls back to the first input.
while True:

	answer = input('Do you want to play one of our three games? [Y/ N=quit]:  ')

	# The loop the program spends most of its runtime on
	while Valid:

		if answer in N or answer in Q:

			print('See you!')
			sleep(1)
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
			answer = answer.lower()

			# Dict for most of the possible game name choices/typos
			answerOptions = {
				'Tic':{'1','tic tac toe','tictactoe','tictac toe','tic tactoe'},
				'Siga':{'2','siga','seega','sega'},
				'Rc':{'3','rocket collider','rocketcollider','roket colider','rocket colider','roket collider'}
			}


			if answer in answerOptions['Tic']:
				Tic.runGame()
			
			elif answer in answerOptions['Siga']:
				Siga.runGame()
			
			elif answer in answerOptions['Rc']:
				Rc.runGame()

			else:
				chdir(path.dirname(__file__)) # make sure you're on the correct directory
				
				with open('answerlogs.txt','a') as logs: # open your log file once 
					logs.write("- "+answer+"\n") # write the answer for future typo reference
				
				Valid = False # invalidate the answer to exit the loop "while Valid"
				break		
			

			answer = input('Wanna play another game? [Y/ N=leave to main / Q=quit]:  ')

			if answer in Y:
				print()
				print('Alright! Another round!')
				continue

			elif answer in N:
				print()
				print('Alright, returning to main...')
				break

			elif answer in Q:
				print()
				print('Hope you enjoyed!')
				quit()

			else:
				Valid = False
				break
		

		else: # an else for the case if the very first input was invalid
			Valid = False

	if not Valid: # general fallback for all the invalid answers inside the "while Valid" loop 	
		print ('Undecided. Returning to main...\n')
		Valid = True
