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




