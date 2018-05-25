from random import choice
from Siga import showBoard


# global list used to insert (1 or more user's) or the computer's input.
slots = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
# demo list to show the user how to use the board.
demo = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# player 1 chooses between single or multi


def help():
    '''prints game manual'''
    print('''hello! this is TicTacToe made by Adham and supervised by our team '3x3.'
the concept is pretty simple, you choose whether you want to play with the computer or with your friend and based on turns
each player will try to hit his/her letter (X or Z) horizontally, vertically, or diagonally in 3 slots.
who ever claims three consecutive of his letter, Wins the game!
''')


def SingleOrMulti():
    '''multiplayer / single player checker'''

    gametype = ''
    while gametype == '':
        mode = input('are you alone? y for yes and n for no please.')
        if mode == 'y':
            gametype += 'single'
            print("alright! you'll play with Ultron :)")
            return gametype
        elif mode == 'n':
            print("oh, you are with a friend. this will be interesting.")
            gametype += 'multi'
            return gametype
        else:
            print('oh-oh. use y for yes and n for no. no capitalization.')


def shwBoard(board):
    '''function that prints the board using a list.'''

    showBoard(board, Labels=False)


def whosfirst():
    '''player1 chooses who goes first, whether P1 is playing W comp or P2   '''

    answertype = ''
    while answertype == '':
        answer = input(
            'Player 1, do you wanna go first? y for yes and n for no please.')
        if answer == 'y':
            print('okay! good luck. make your first move player 1.')
            answertype += 'yes'
            return answertype
        elif answer == 'n':
            print('okay! good luck. make your first move player 2.')
            answertype += 'no'
            return answertype
        else:
            print('please stick with y for yes and n for no, no capitalization.')


def emptyspace(plyr_mve):
    '''function that identifies blank spaces in the global list (slot)'''

    if slots[plyr_mve] == ' ':
        return True
    else:
        return False


def compmove():
    '''Function that chooses the comp move based on random choice built in function and stores it in (slots) list'''

    state = bool
    while state != True:
        x = choice(list(range(8)))
        y = emptyspace(x)
        state = y
    if state == True:
        slots[x] = 'Z'
        shwBoard(slots)


def player1move(symb):
    '''function that lets the player choose his move and stores it into (slots) list '''

    shwBoard(demo)
    while True:
        loc = input(
            "choose your move's place from 1-9 as stated in the board infront of you")
        if loc.isnumeric():
            if float(eval(loc)) == 1.0 or float(eval(loc)) == 2.0 or float(eval(loc)) == 3.0 or float(eval(loc)) == 4.0 or float(eval(loc)) == 5.0 or float(eval(loc)) == 6.0 or float(eval(loc)) == 7.0 or float(eval(loc)) == 8.0 or float(eval(loc)) == 9.0:
                if emptyspace(eval(loc)-1) == True:
                    slots[eval(loc)-1] = symb
                    shwBoard(slots)

                    break

            else:
                print('please choose between 1-9 only!!')
        else:
            print('dont use complex expression.')


def boardfull():
    '''checks if the board is full and prints that game has ended.'''

    marker = 0
    for i in slots:
        if i == ' ':
            marker += 1
            return False
    if marker == 0:
        print("oh no it's a draw.")
        return True


def checkwin(symb):
    '''checks if the designated player X or Z has won and returns the status'''
    status = True

    possible = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for item in possible:
        emp_lst = []
        for i in item:
            emp_lst.append(slots[i])
        if emp_lst[0] != ' ' and emp_lst[0] == emp_lst[1] and emp_lst[1] == emp_lst[2]:
            if emp_lst[0] == symb:
                print('you won player using letter {}!'.format(symb))
                status = True

            else:
                print('experimental: you lost to the opposing opponent')

            return status


def Gene_checkwin():
    '''Checks if either of players has won.'''
    status = False

    possible = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for item in possible:
        emp_lst = []
        for i in item:
            emp_lst.append(slots[i])
        if emp_lst[0] != ' ' and emp_lst[0] == emp_lst[1] and emp_lst[1] == emp_lst[2]:

            status = True
        else:
            status = False

        return status
    else:
        status = False
        return status


def gameon(func):
    '''used to check if game is still going on or not using function checkwin'''
    status = True
    if func == False:  # if checkwin is false
        status = True  # game is still on
        return status
    if func == True:  # if checkwin is true
        status = False  # game ends returns false
        return status


def runGame():
    ''' the central code that runs the game'''
    help()  # introduces player to the rules and the team
    mode = SingleOrMulti()  # user chooses game mode
    if mode == 'multi':
        if whosfirst() == 'yes':  # if player chooses to go first
            while Gene_checkwin() == False:  # condition to keep the game going if false
                player1move('X')
                if checkwin('X') == True:  # if player one "X" wins game breaks and player wins
                    break
                else:
                    if boardfull() != True:  # player 2 plays
                        # if p1 move causes the game to move on without winning condition or draw, p2 plays
                        if checkwin('Z') != True:
                            player1move('Z')
                            if checkwin('Z') == True:
                                break
                            else:
                                boardfull()
                    else:
                        break

        else:  # if P2 is going to start first
            while Gene_checkwin() == False:

                player1move('Z')
                if checkwin('Z') == True:
                    break
                else:
                    if boardfull() != True:
                        # if p1 move causes the game to move on without winning condition or draw, p2 plays
                        if checkwin('X') != True:
                            player1move('X')
                            if checkwin('X') == True:
                                break
                            else:
                                boardfull()
                    else:
                        break

    if mode == 'single':  # if player chooses single with comp
        if whosfirst() == 'yes':
            while Gene_checkwin() == False:

                player1move('X')
                if checkwin('X') == True:
                    break
                else:
                    if boardfull() != True:
                        # if p1 move causes the game to move on without winning condition or draw, p2 plays
                        if checkwin('Z') != True:
                            compmove()
                            if checkwin('Z') == True:
                                break
                            else:
                                boardfull()
                    else:
                        break

        else:  # if P2 is going to start first
            while Gene_checkwin() == False:

                compmove()
                if checkwin('Z') == True:
                    break
                else:
                    if boardfull() != True:
                        # if p1 move causes the game to move on without winning condition or draw, p2 plays
                        if checkwin('X') != True:
                            player1move('X')
                            if checkwin('X') == True:
                                break
                            else:
                                boardfull()
                    else:
                        break
