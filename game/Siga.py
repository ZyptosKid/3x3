
from random import choice as randomChoice
from time import sleep


def help():
	print('''Siga v0.1 Beta
By: Hazem Elmasry

How to play:

	Two players place three pieces on a 3x3 grid and move one piece at a time each turn.

	The goal is to get your three pieces in a row

	You're allowed to move to the square next to you or the square after it, Horizontally, Vertically, or Diagonally.
	But you're not allowed to jump over the other player's piece.\n\n\n
	
Good luck!\n\n\n''')


def initialize():

	P1 = '^'
	P2 = 'v'
	comp = 'v'

	Board = {
		1:"v" , 2:"v" , 3:"v" ,
		4:" " , 5:" " , 6:" " ,
		7:"^" , 8:"^" , 9:"^" ,
	}
	
	# will make the player able to choose their symbol later.

	Y = {'Y', 'y', 'yes', 'Yes', 'YES'}
	N = {'N', 'n', 'no', 'No', 'NO'}

	while True:

		multi = input('Multiplayer? [Y/N]:  ')

		if multi in Y:
			multi = True
			break

		elif multi in N:
			multi = False
			break

		else:
			print('this isn\'t a correct choice!')
			continue

	while True:

		P1First = input('P1, wanna go first? [Y/N]:  ')

		if P1First in Y:
			P1First = True
			break

		elif P1First in N:
			P1First = False
			break

		else:
			print('this isn\'t a correct choice!')
			continue


	return {
		'Board':Board,
		'Multiplayer':multi,
		'P1First':P1First,
		'P1':P1,
		'P2':P2,
		'Computer':comp
		}


def showBoard(Board):

	if type(Board) == dict:
		PBoard = Board.values()

	print(
		'\n [1] | [2] | [3]\n  {}  |  {}  |  {} \n-----------------\n [4] | [5] | [6]\n  {}  |  {}  |  {} \n-----------------\n [7] | [8] | [9]\n  {}  |  {}  |  {} \n'.format(*PBoard)
		)


def playermoved(Board,currentPMark,otherPMark):

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
		{3,8},
		{3,9},
		{4,9},
		{6,7},
	]

	# error dict
	# error action dict
	# for error in error dict:
	# if errordict[error]: 
	# 	exec(erroractiondict[error]) and return False 

	while True:


		while True:

			moveOrigin = int(input('Choose a square where you have one of your pieces:  '))

			if Board[moveOrigin] != currentPMark:
				print('please choose one of your pieces')
				continue

			break
		
		while True:

			moveDest = int(input('Choose a square where you want it to go:  '))

			if Board[moveDest] != " ":
				print('you can\'t move there!')
				continue

			break

		cornerJumps = {moveOrigin,moveDest} in corners
		normalJumps = {moveOrigin,moveDest} in jumps
		ambitious = {moveOrigin,moveDest} in ambition

		if (moveOrigin not in Board) or (moveDest not in Board):

			print('you chose something that isn\'t on the Board to begin with.')
			continue


		elif ambitious:

			print('can\'t move this far!')
			continue

		elif (normalJumps or cornerJumps) and Board[(moveDest + moveOrigin)/2] == otherPMark:

			print('can\'t jump over the other player\'s piece!')
			continue

		else:
			Board[moveDest] = currentPMark
			Board[moveOrigin] = " "
			break

	del(corners,jumps,ambition)
	return moveOrigin


def compumoved(Board,currentPMark,otherPMark):

	moveOrigins = []
	moveDests = []

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
		{3,8},
		{3,9},
		{4,9},
		{6,7},
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

	win = [{1,2,3},{4,5,6},{7,8,9},{1,4,7},{2,5,8},{3,6,9},{1,5,9},{3,5,7}]
	
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

	help()

	info = initialize()
	Board = info['Board']

	while True:

		try:
			
			if info['Multiplayer']:

				P1 = info['P1']
				P2 = info['P2']
				P1moved = {7:False,8:False,9:False}
				P2moved = {1:False,2:False,3:False}

				print()
				print('P1\'s piece is "^"')
				print('P2\'s is "v"')

				if info['P1First']:

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

				P1 = info['P1']
				P2 = info['Computer']
				P1moved = {7:False,8:False,9:False}
				P2moved = {1:False,2:False,3:False}

				print()
				print('Computer\'s piece is "v"')

				if info['P1First']:

					while True:
						
						showBoard(Board)
						P1moved[playermoved(Board,P1,P2)] = True
						
						if wincheck(Board,P1,all(P1moved.values())):
							showBoard(Board)
							print('P1 Won!')
							break

						P2moved[compumoved(Board,P2,P1)] = True
						
						if wincheck(Board,P2,all(P2moved.values())):
							showBoard(Board)
							print('You lost to Ultron!')
							break
					break
				
				elif not info['P1First']:

					while True:

						P2moved[compumoved(Board,P2,P1)] = True
						
						if wincheck(Board,P2,all(P2moved.values())):
							showBoard(Board)
							print('You lost to Ultron!')
							break
						
						showBoard(Board)
						P1moved[playermoved(Board,P1,P2)] = True
						
						if wincheck(Board,P1,all(P1moved.values())):
							showBoard(Board)
							print('P1 Won!')
							break
					break

		except Exception as a:
			if a == KeyboardInterrupt:
				break
			
			else:
				print('your input was invalid')
				sleep(2)
