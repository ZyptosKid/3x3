# from random import choice as randomChoice


# Board = {
# 	1:" " , 2:"v" , 3:" " ,
# 	4:" " , 5:"v" , 6:"v" ,
# 	7:"^" , 8:"^" , 9:"^" ,
# }

# def showBoard(Board):

# 	print(
# 		' [1] | [2] | [3]\n  {}  |  {}  |  {} \n-----------------\n [4] | [5] | [6]\n  {}  |  {}  |  {} \n-----------------\n [7] | [8] | [9]\n  {}  |  {}  |  {} \n'.format(*Board.values())
# 		)



# currentPMark = 'v'
# otherPMark = '^'





# # moveOrigin = 7
# # print('mvorig: '+str(moveOrigin))
# # moveDest = 3
# # print('mvDst: '+str(moveDest))

# # moveSpace = moveDest - moveOrigin
# # print('mvSpace: '+str(moveSpace))

# # corners1 = {1,9}
# # corners2 = {3,7}

# # cornerJumps = {moveOrigin,moveDest} == corners1 or {moveOrigin,moveDest} == corners2
# # print('cornerJumps: '+str(cornerJumps))
# # normalJumps = abs(moveSpace) == 6 or abs(moveSpace) == 2
# # print('normalJumps: '+str(normalJumps))
# # ambitious = abs(moveSpace) == 7 or abs(moveSpace) == 5
# # print('ambitious: '+str(ambitious))

# # # error dict
# # # error action dict
# # # for error in error dict:
# # # if errordict[error]: 
# # # 	exec(erroractiondict[error]) and return False 

# # if (moveOrigin not in board) or (moveDest not in board):
# # 	print('you chose something that isn\'t on the board to begin with.')
# # 	print(False)

# # elif board[moveOrigin] != currentPMark:

# # 	print('please choose one of your pieces')
# # 	print(False)

# # elif board[moveDest] != " ":

# # 	print('you can\'t move there!')
# # 	print(False)

# # elif ambitious:

# # 	print('can\'t move this far!')
# # 	print(False)

# # elif (normalJumps or cornerJumps) and board[(moveDest + moveOrigin)/2] == otherPMark:

# # 	print('can\'t jump over the other player\'s piece!')
# # 	print(False)

# # else:

# # 	board[moveDest] = currentPMark
# # 	board[moveOrigin] = " "
# # 	print(board)


# moveOrigins = []
# moveDests = []

# for square in Board:
# 	if Board[square] == ' ':
# 		moveDests.append(square)
# 	elif Board[square] == currentPMark:
# 		moveOrigins.append(square)
# 	else:
# 		pass

# corners1 = {1,9}
# corners2 = {3,7}

# print('thinking...')

# while True:

# 	moveOrigin = randomChoice(moveOrigins)
# 	print('mvorig: '+str(moveOrigin))
# 	moveDest = randomChoice(moveDests)
# 	print('mvDst: '+str(moveDest))
# 	moveSpace = moveDest - moveOrigin

# 	cornerJumps = {moveOrigin,moveDest} == corners1 or {moveOrigin,moveDest} == corners2
# 	print('cornerJumps: '+str(cornerJumps))
# 	normalJumps = abs(moveSpace) == 6 or abs(moveSpace) == 2
# 	print('normalJumps: '+str(normalJumps))
# 	ambitious = abs(moveSpace) == 7 or abs(moveSpace) == 5
# 	print('ambitious: '+str(ambitious))

# 	if ambitious:
# 		print('can\'t move this far!')
# 		continue

# 	elif (normalJumps or cornerJumps) and Board[(moveDest + moveOrigin)/2] == otherPMark:
# 		print('can\'t jump over the other player\'s piece!')
# 		continue

# 	else:
# 		Board[moveDest] = currentPMark
# 		Board[moveOrigin] = " "
# 		showBoard(Board)
# 		break

# del(corners1,corners2)



#######################################3

from random import choice as randomChoice

Board = {
	1:1 , 2:0 , 3:1 ,
	4:1 , 5:0 , 6:2 ,
	7:0 , 8:2 , 9:2
}

currentPMark = 1
otherPMark = 2

allmoved = {1:True, 2:True, 3:True}

def compumoved(Board,currentPMark,otherPMark,allmoved):
	
	### AI ALGORITHM ###
	# all must move first
		# make a set of all the possible move dests and origins combinations as lists and pass them through all the forbidden movements as sets, popping/deleting any match
		# make another list of all the move origins that are still False [list(dict.keys(False))?] (from runGame) [another param needed]
		# you end up with a set of all the possible movement lists [origin,dist] and another of unmoved origins
		# copy the possibilities set for a fallback into random choice in case all moved
		# loop through the movement lists set with index[0] aka origin and see if it's in unmoved origins
		# again if yes pass if no pop/delete that list
		# no choice available:
			# check for winning moves
		# one choice or more:
			# randomChoice it
		
	# check for winning moves
		# get the filtered set of lists from above
		# loop every set item (as set) on winning moves and see if the len of your intersection is 2
			# if yes difference the intersection with the win move to find the required dist
				# if [origin,dist] in possible dists, keep it, else pass
		# no choice available:
			# fallback to regular random choice
		# one choice or more:
			# randomChoice it vs filtered for 67/33 chance to win/pass

	'''
	Processes the computer's movement and checks its validity specifically based on the Siga rules.
	This function is derived from playermoved() but with automated choosing system.

	Params:
		Board (dict)
		currentPMark (str): Current turn computer's mark. used for conditions and comparisons
		otherPMark (str): The player's mark. also used as the one above
		
	returns the movement origin of the player for using it to check if all the player's pieces moved or not
	'''

	moveOrigins = [] # all the possible move origins (computer's pieces placement on Board)
	moveDests = [] # all the possible free destinations


	# get a list of all the possible piece choices (3 choices only) and all the possible destination choices (3 choices only) proior to choosing
	# to reduce the number of random choices that could go wrong ( from 9 choices on board twice to three choices twice), and for condition checking

	for square in Board:
		if Board[square] == 0: # If the square is empty
			moveDests.append(square) # Make it a possible destination
		elif Board[square] == currentPMark: # else if the square has a piece that belongs to computer
			moveOrigins.append(square) # Make it a possible origin
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

	win = [
		{1,2,3},
		{4,5,6},
		{7,8,9},
		{1,4,7},
		{2,5,8},
		{3,6,9},
		{1,5,9},
		{3,5,7}
	]

	AIlist = []
	for origin in moveOrigins:
		for destination in moveDests:

			cornerJumps = {origin,destination} in corners
			normalJumps = {origin,destination} in jumps
			ambitious = {origin,destination} in ambition
			
			if ambitious:
				continue

			elif (normalJumps or cornerJumps) and Board[(origin+destination)/2] == otherPMark:
				continue

			else:
				AIlist.append([origin,destination])


	if all(allmoved.values()):

		options = AIlist


	else:

		unmovedset = set()
		for origin in allmoved:
			if allmoved[origin] == False:
				unmovedset.add(origin)

		options = []
		for option in AIlist:
			if option[0] in unmovedset:
				options.append(option)


	winoptions = []

	for winset in win:

		if len(set(moveOrigins).intersection(winset)) == 2:

			for option in options:
				if option[1] == winset.difference(set(moveOrigins)).pop() and option[0] not in winset:
					winoptions.append(option)



	movechoice = randomChoice([1,2,3])
	if movechoice%3 != 0 and winoptions:
		winmove = randomChoice(winoptions)
		[moveOrigin,moveDest] = winmove
		Board[moveOrigin] = 0
		Board[moveDest] = currentPMark
	else:
		move = randomChoice(options)
		[moveOrigin,moveDest] = move
		Board[moveOrigin] = 0
		Board[moveDest] = currentPMark


	return moveOrigin


compumoved(Board,currentPMark,otherPMark,allmoved)
