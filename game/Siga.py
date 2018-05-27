__author__ = "Hazem Elmasry"


from random import choice as randomChoice
from time import sleep



# Globals:
Y = {'Y', 'y', 'yes', 'Yes', 'YES'}
N = {'N', 'n', 'no', 'No', 'NO'}

P1 = '^'
P2 = comp = 'v'

# initialized board
Board = {
	1:P2 , 2:P2 , 3:P2 ,
	4:" ", 5:" ", 6:" ",
	7:P1 , 8:P1 , 9:P1 ,
}


def help():

	'''
	Prints a brief manual for the game, no parameters needed
	No parameters, returns None
	'''

	print('''
	Siga v1
	By: Hazem Elmasry

	How to play:

		Two players place three pieces on a 3x3 grid and move one piece at a time each turn.

		The goal is to get your three pieces in a row

		You're allowed to move to the square next to you or the square after it, Horizontally, Vertically, or Diagonally.
		But you're not allowed to jump over the other player's piece.\n\n\n
		
	Good luck!\n\n\n''')


def initialize():
	'''
	Called once. initializes Siga's unchanging options. no parameters.

	Returns a dictionary as follows:

		'Multiplayer': 	(bool) 	Multiplayer T/F depending on user input,
		'P1First': 		(bool) 	Player 1 goes first T/F depending on user input

	THIS FUNCTION CONTAINS INPUT PROMPTS

	'''

	while True:

		multi = multiplayer(multi = input('Multiplayer? [Y/N]:  '))
		if any(multi):
			pass
		else:
			continue

		P1First = whoFirst(P1First = input('P1, wanna go first? [Y/N]:  '))
		if any(P1First):
			break
		else:
			continue


	return {
		'Multiplayer':multi[1],
		'P1First':P1First[1],
		}


def multiplayer(multi):

	global Y, N

	if multi in Y.union(N):

		if multi in Y:
			multi = True
		else:
			multi = False

		return True,multi

	else:

		print('this isn\'t a correct choice!')

		return False,False


def whoFirst(P1First):

	global Y, N

	if P1First in Y.union(N):

		if P1First in Y:
			P1First = True
		else:
			P1First = False

		return True,P1First

	else:

		print('this isn\'t a correct choice!')
		
		return False


def showBoard(Board,Labels=True):

	'''
	Prints the game board, returns None

	Params:
		Board (any linear indexed iterable),
		Labels = default True (bool) : either shows slot label or hides it

	examples:

		Labels = True:
			[1] | [2] | [3]
			 1  |  2  |  3
		   -----------------
			[4] | [5] | [6]
			 4  |  5  |  6
		   -----------------
			[7] | [8] | [9]
			 7  |  8  |  9

		Labels = False:
			 1  |  2  |  3
		   -----------------
			 4  |  5  |  6
		   -----------------
			 7  |  8  |  9

	This function is reusable for all linear iterables. Import it, no problems.

	'''

	if type(Board) == dict:
		PBoard = Board.values()

	else:
		PBoard = Board

	if Labels:
		print('\n [1] | [2] | [3]\n  {}  |  {}  |  {} \n-----------------\n [4] | [5] | [6]\n  {}  |  {}  |  {} \n-----------------\n [7] | [8] | [9]\n  {}  |  {}  |  {} \n'.format(*PBoard))
	
	else:
		print('\n  {}  |  {}  |  {} \n-----------------\n  {}  |  {}  |  {} \n-----------------\n  {}  |  {}  |  {} \n'.format(*PBoard))


def playermoved(Board,currentPMark,otherPMark):

	'''
	Processes the player's movement and checks its validity specifically based on the Siga rules.

	Params:
		Board (dict)
		currentPMark (str): Current turn player's mark. used for conditions and comparisons
		otherPMark (str): The other player's mark. also used as the one above
		
	returns the movement origin of the player for using it to check if all the player's pieces moved or not
	'''
	# list of possible corner movement combinations
	corners = [
		{1,9},
		{3,7}
	]

	# list of possible 2-block jump movement combinations
	jumps = [
		{1,3},
		{1,7},
		{1,9},
		{2,8},
		{3,7},
		{3,9},
		{4,6}
	]

	# list of possible out-of-range movement combinations
	ambition = [
		{1,8},
		{1,6},
		{2,9},
		{2,7},
		{3,4},
		{3,8},
		{4,9},
		{6,7}
	]

	# I used to try a mathematical approach instead off possible combinations approach but it was never consistent across all possible movements. For example: moving from square 4 to square 3 should mathematically mean a 1-block movement, but it actually is an out-of-range movement.

	# error dict
	# error action dict
	# for error in error dict:
	# if errordict[error]: 
	# 	exec(erroractiondict[error]) and return False 



	while True:

		try:

			moveOrigin = int(input('Type in a square number where you have one of your pieces:  '))

			if moveOrigin not in Board:

				print('you chose something that isn\'t on the Board to begin with.')
				continue

			elif Board[moveOrigin] != currentPMark:

				print('please choose one of your pieces')
				continue

			break
		
		except Exception as a:

			# To allow a ctrl+c exit
			if a == KeyboardInterrupt:
				break
			
			else:
				print('your input was invalid')
				continue

	while True:

		try:

			moveDest = int(input('Choose a square number where you want it to go:  '))

			if moveDest not in Board:

				print('you chose something that isn\'t on the Board to begin with.')
				continue

			elif Board[moveDest] != " ":
				
				print('you can\'t move there!')
				continue


			cornerJumps = {moveOrigin,moveDest} in corners
			normalJumps = {moveOrigin,moveDest} in jumps
			ambitious = {moveOrigin,moveDest} in ambition


			if ambitious:

				print('can\'t move this far!')
				continue

			elif (normalJumps or cornerJumps) and Board[(moveDest + moveOrigin)/2] == otherPMark:

				print('can\'t jump over the other player\'s piece!')
				continue

			else:

				# if there was no problem with the player choices
				Board[moveDest] = currentPMark
				Board[moveOrigin] = " "
				# one successful move done
				break

		except Exception as a:

			# To allow a ctrl+c exit
			if a == KeyboardInterrupt:
				break
			
			else:
				print('your input was invalid')
				continue


	del(corners,jumps,ambition) # no need to keep those around
	return moveOrigin # I use the move origin to make sure later that the player moved all the three pieces before winning, another rule of Sega. 
	# The condition is checked on both wincheck() and runGame()


def compumoved(Board,currentPMark,otherPMark):

	'''
	Processes the computer's movement and checks its validity specifically based on the Siga rules.
	This function is derived from playermoved() but with automated choosing system.

	Params:
		Board (dict)
		currentPMark (str): Current turn computer's mark. used for conditions and comparisons
		otherPMark (str): The player's mark. also used as the one above
		
	returns the movement origin of the player for using it to check if all the player's pieces moved or not
	'''

	moveOrigins = []
	moveDests = []

	# get a list of all the possible piece choices (3 choices only) and all the possible destination choices (3 choices only) proior to choosing
	# to reduce the number of random choices (9 choices on board) and condition checking

	for square in Board:
		if Board[square] == ' ':
			moveDests.append(square)
		elif Board[square] == currentPMark:
			moveOrigins.append(square)
		else:
			pass

	corners = [
		{1,9},
		{3,7}
	]

	jumps = [
		{1,3},
		{1,7},
		{1,9},
		{2,8},
		{3,7},
		{3,9},
		{4,6}
	]

	ambition = [
		{1,8},
		{1,6},
		{2,9},
		{2,7},
		{3,4},
		{3,8},
		{4,9},
		{6,7}
	]

	while True:
	
		moveOrigin = randomChoice(moveOrigins)
		moveDest = randomChoice(moveDests)

		cornerJumps = {moveOrigin,moveDest} in corners
		normalJumps = {moveOrigin,moveDest} in jumps
		ambitious = {moveOrigin,moveDest} in ambition

		if ambitious:
			continue

		elif (normalJumps or cornerJumps) and Board[(moveDest + moveOrigin)/2] == otherPMark:
			continue

		else:
			Board[moveDest] = currentPMark
			Board[moveOrigin] = " "
			break

	del(corners,jumps,ambition)
	return moveOrigin


def wincheck(Board,player,allmoved=False):

	'''
	Checks if a player won based on the given params and specifically for Siga's rules.

	Params:
		Board (dict)
		player (str): the checked player's mark
		allmoved = default False (bool): True means that all the player's pieces moved.

	returns True for a win, False for not
	'''

	# the possible win cases
	win = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
	
	# this set is later compared to the win cases to see if it's part of that list
	P = set()

	for square in Board:
		if Board[square] == player:
			P.add(square)

	if allmoved:

		if P in win:
			return True

	else:
		return False
		

def runGame():
	'''
	Main game runner, called on mainframe. No parameters, returns None.
	'''

	help()

	info = initialize()
	global Board, P1, P2, comp, Y, N

	while True:		

		if info['Multiplayer']: # if multiplayer is true

			# turn this move checker into a function
			P1moved = {7:False,8:False,9:False} # all pieces didn't move: False False False
			P2moved = {1:False,2:False,3:False}

			print()
			print('P1\'s piece is "{}"'.format(P1))
			print('P2\'s is "{}"'.format(P2))

			if info['P1First']: # if player 1 goes first is True

				while True:

					print('P1\'s Turn:')
					showBoard(Board)
					P1moved[playermoved(Board,P1,P2)] = True

					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break
					
					print('P2\'s Turn:')
					showBoard(Board)
					P2moved[playermoved(Board,P2,P1)] = True

					if wincheck(Board,P2,all(P2moved.values())):
						showBoard(Board)
						print('P2 Won!')
						break
				break

			elif not info['P1First']:

				while True:

					print('P2\'s Turn:')
					showBoard(Board)
					P2moved[playermoved(Board,P2,P1)] = True

					if wincheck(Board,P2,all(P2moved.values())):
						showBoard(Board)
						print('P2 Won!')
						break
					
					print('P1\'s Turn:')
					showBoard(Board)
					P1moved[playermoved(Board,P1,P2)] = True

					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break
				break

		elif not info['Multiplayer']:

			P1moved = {7:False,8:False,9:False}
			P2moved = {1:False,2:False,3:False}

			print()
			print('Computer\'s piece is "{}"'.format(comp))

			if info['P1First']:

				while True:
					
					showBoard(Board)
					P1moved[playermoved(Board,P1,comp)] = True
					
					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break

					P2moved[compumoved(Board,comp,P1)] = True
					
					if wincheck(Board,comp,all(P2moved.values())):
						showBoard(Board)
						print('You lost to Ultron!')
						break
				break
			
			elif not info['P1First']:

				while True:

					P2moved[compumoved(Board,comp,P1)] = True
					
					if wincheck(Board,comp,all(P2moved.values())):
						showBoard(Board)
						print('You lost to Ultron!')
						break
					
					showBoard(Board)
					P1moved[playermoved(Board,P1,comp)] = True
					
					if wincheck(Board,P1,all(P1moved.values())):
						showBoard(Board)
						print('P1 Won!')
						break
				break

