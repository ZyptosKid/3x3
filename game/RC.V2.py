from getpass import getpass

#slots=['0','1','2','3','4','5','6','7','8','9']
def showBoard(Gboard):
    '''showboard(board) makes the board and assigns a number for each slot,
making the board nd its contents susebtable for modification'''
    print('' +Gboard[1]+ ' | ' +Gboard[2]+ ' | '+Gboard[3] )
    print('----------------')
    print('' +Gboard[4]+ ' | ' +Gboard[5]+ ' | '+Gboard[6] )
    print('----------------')
    print('' +Gboard[7]+ ' | ' +Gboard[8]+ ' | '+Gboard[9] )
#showBoard(slots)



def runGame():
    '''runGame() starts the game by initiating the code that takes intial places from players'''
    Baby_steps()




def Baby_steps():
    '''rungame() runs the initial choice of slots sequence,
with no need for parameters, the board is printed and the game starts RIGHT NOW'''
    slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
    showBoard(slots)
    print()
    initialmoves = []
    for i in range(1,4): #starts taking the initial places of the players
        Start_point=input('P{} Pick a start point: '.format(i))
        
        

        while Start_point.isdigit() == False: #Makes sure the entery is digits
            Start_point=input('''!Cell invalid!
P{} Pick an valid cell: '''.format(i))
        print()
        Start_point=int(Start_point)
        
        
        
        while Start_point>9 or Start_point<0 : #makes sure the entery is valid numbers
            Start_point=int(input('''!Cell invalid!
P{:d} Pick an valid cell: '''.format(i)))
            print()
            if 0<Start_point and Start_point<10:
                break
        
        
        
        while Start_point in initialmoves: #ensures that no 2 players have the same slot
            Start_point=int(input('P{:d} Pick an unoccupied cell: '.format(i)))
            print()
            if Start_point not in initialmoves:
                print()
                break
        
        
        
        initialmoves.append(Start_point) #To check that no 2 players take the same slot
        slots[Start_point]='P{} '.format(i)
    #slots[Start_point]='P{} '.format(i)
    showBoard(slots)
    print()
    print(
        '''!Movement System!
you are practically allowed to move anyhow and go anywhere
as long as you donnt collide
goodluck surviving the rocket mash'''
        )
    print()
    Win_Condition()





def Win_Condition():
    '''
Win_Condition() is a function that needs no peremeters, it runs and tests for wining,
losing, draw, according to the movement of the players stored in the Movement_tracing() function'''
    x=[]
    while x!=0: #infinite loop to run the game infinitly or till a player wins
        slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
        
        
        
        for i in range(1,4): #Takes the next move
            Next_move=getpass('P{:d} Pick a slot to move to \n(don\'t worry, it won\'t show on screen): '.format(i))
            print()
            x.append(Next_move)
            
            
            
            while Next_move.isdigit() == False: #Makes sure the entery is digits
                Next_move=getpass('''!Cell invalid!
P{} Pick an valid cell to move to: '''.format(i))
            Next_move=int(Next_move)
            slots[Next_move]='P{} '.format(i)
            print()
        showBoard(slots)
        
        

        p1move = x[len(x)-3] #assigning each a player's move to a variable
        p2move = x[len(x)-2]
        p3move = x[len(x)-1]
        if p2move == p1move == p3move: #Functions that check for the win
            print('Draww')
            print()
            break
        
        elif p3move == p2move :
            print("Player 1 Winssss" )
            print()
            break
        
        elif p3move == p1move :
            print("Player 2 Winssss" )
            print()
            break
        
        elif p2move == p1move :
            print("Player 3 Winssss" )
            print()
            break      
runGame()


#     Newgame()

# def Newgame():
#     '''NewGame() is a function that starts a new round of the game
#after taking the concent of the user'''
#     New_game=input('Wanna play again? Y/A-Z ')
#     if New_game.lower() == 'y':
#         rungame()
#     else:
#         print('Thanks for playing our game XD')