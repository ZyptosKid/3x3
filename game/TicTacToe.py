

from random import choice
slots=['','','','','','','','',''] #global list used to insert (1 or more user's) or the computer's input. 
demo=['1','2','3','4','5','6','7','8','9'] #demo list to show the user how to use the board.
#player 1 chooses between single or multi
def help():
    print('''hello! this is TicTacToe made by Adham and supervised by our team '3x3.'
the concept is pretty simple, you choose whether you want to play with the computer or with your friend and based on turns
each player will try to hit his/her letter (X or Z) horizontally, vertically, or diagonally in 3 slots.
who ever claims three consecutive of his letter, Wins the game!
''') 

def SingleOrMulti():
    gametype=''
    while gametype=='':
        mode=input('are you alone? y for yes and n for no please.')
        if mode == 'y':
            gametype+='single'
            print("alright! you'll play with Ultron :)")
            return gametype
        elif mode == 'n':
            print("oh, you are with a friend. this will be interesting.")
            gametype+='multi'
            return gametype
        else:
            print('oh-oh. use y for yes and n for no. no capitalization.')
     

 
def shwBoard(board): #function that prints the board using a list.
    print('' +board[0]+ '  | ' +board[1]+ '  | '+board[2] )
    print('' +board[3]+ '  | ' +board[4]+ '  | '+board[5] )
    print('' +board[6]+ '  | ' +board[7]+ '  | '+board[8] )
    print('-------------')


#shwBoard(slots)    
    
    

#player1 chooses who goes first, whether P1 is playing W comp or P2            

def whosfirst():
    answertype=''
    while answertype=='':
        answer=input('Player 1, do you wanna go first? y for yes and n for no please.')
        if answer== 'y':
            print('okay! good luck. make your first move player.')
            answertype+='yes'
            return answertype
        elif answer == 'n':
            print('Ultron will go first. be careful from his moves.')
            answertype+='no'
            return answertype
        else:
            print('please stick with y for yes and n for no, no capitalization.')


###def multiTTT():


def emptyspace(plyr_mve): #function that identifies blank spaces in the global list (slot)

    if slots[plyr_mve] == '':
        return True
    else:
        return False


def compmove(): #Function that chooses the comp move based on random choice built in function and stores it in (slots) list

    state=bool
    while state != True:    
        x =choice(list(range(8)))
        y=emptyspace(x)
        state=y     
    if state == True:
        slots[x]='Z'
        shwBoard(slots)



def player1move(symb): #function that lets the player choose his move and stores it into (slots) list 
     
    shwBoard(demo)
    while True:

        loc=int(input("choose your move's place from 1-9 as stated in the board infront of you"))-1
        if emptyspace(loc) == True:
            slots[loc]=symb
            shwBoard(slots)

            break

                
            
            
    
        
        
        
def boardfull(): #checks if the board is full and prints that game has ended.

    marker=0
    for i in slots:
        if i == "":
            marker+=1
            return False
    if marker == 0:
        print("oh no it's a draw.")        
        return True
        

def checkwin(symb):#checks if either X or Z hit one of the possible winning combinations.
    status=True

    possible=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    
    for item in possible:
        emp_lst=[]
        for i in item:
            emp_lst.append(slots[i])
        if emp_lst[0]!='' and emp_lst[0] == emp_lst[1] and emp_lst[1] == emp_lst[2]:
            status=True
            return status
    else:
        status=False
        return status

                    
'''
def gameon():
    status=True
    if checkwin==False:
        status=True
        return status
    if checkwin==True:
        status=False
        return status
'''

def runGame(): # the central code that runs the game
    help() #introduces player to the rules and the team
    mode=SingleOrMulti() #user chooses game mode
    if mode == 'multi':
        if whosfirst() == 'yes': #if player chooses to go first
            while True:
                player1move('X')
                checkwin('X')
                boardfull()

                if checkwin('X')==False: #if p1 move causes the game to move on without winning condition or draw, p2 plays
                    player1move('Z')
                    checkwin('Z')
                    boardfull()
                else:
                    print('you won recent player!')  #congrats the recent player for the win
                    break
        else:#if P2 is going to start first
            while True:
                player1move('Z')
                checkwin('Z')
                if checkwin('Z')==False: #if p2 move causes the game to move on without winning condition or draw, p1 plays
                    player1move('X')
                    checkwin('X')
                else:
                    print('you won recent player!')  #congrats player for his win
                    break
    if mode == 'single': #if player chooses single with comp
        if whosfirst()== 'yes': #player chooses to go first

            while True:
                player1move('X')
                checkwin('X')
                boardfull()

                if checkwin('X')==False: #if p1 move causes the game to move on without winning condition or draw, comp plays
                    compmove()
                    checkwin('Z')
                    boardfull()
                else:
                    print('you won recent player!') #congrats recent player for the win
                    break
        else: #if comp plays first
            while True:
                compmove()
                checkwin('Z')
                if checkwin('Z')==False: #if Comp move causes the game to move on without winning condition or draw, p1 plays
                    player1move('X')
                    checkwin('X')
                else:
                    print('you won recent player!')
                    break



        


        
