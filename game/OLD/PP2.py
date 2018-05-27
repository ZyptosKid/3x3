from getpass import getpass

def showBoard(Gboard):
    '''showboard(board) makes the board and assigns a number for each slot,
making the board and its contents susebtable for modification'''
    print('' +Gboard[1]+ ' | ' +Gboard[2]+ ' | '+Gboard[3] )
    print('----------------')
    print('' +Gboard[4]+ ' | ' +Gboard[5]+ ' | '+Gboard[6] )
    print('----------------')
    print('' +Gboard[7]+ ' | ' +Gboard[8]+ ' | '+Gboard[9] )



def runGame():
    '''runGame() starts the game by initiating the code that takes intial places from players'''
    slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
    Start_point(slots)
    showBoard(slots)
    print()
    print(
        '''!Movement System!
you are practically allowed to move anyhow and go anywhere,
as long as you donnt collide,
goodluck surviving the rocket mash'''
        )
    print()
    Next_move()




def Start_point(s):
    '''Start_point() runs the initial choice of slots sequence,
with no need for parameters, the board is printed and the game starts RIGHT NOW'''
    showBoard(s)
    print()
    initialmoves = []
    
    #starts taking the initial places of the players
    for i in range(1,4): #range 1,4 to run the loop only three times, and not range(3) because i is used as an actual condition checker that requires it to be 1, 2, and 3.
        Start_point=input('P{} Pick a start point (only digits, please): '.format(i))
        
        

        while Start_point.isdigit() == False: #Makes sure the player entery is digits.
            Start_point=input('''!Cell invalid!
P{} Pick an valid cell: '''.format(i))
        print()
        Start_point=int(Start_point) #After taking the start place in turns it to an integer for further use in the following codes.
        
        
        while Start_point>10 or Start_point<=0 : #makes sure the entery is valid numbers (from 1 to 9).
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
        
        initialmoves.append(Start_point) #To check that no 2 players take the same slot ## this comment is better suited in the list assignment up there
        s[Start_point]='P{} '.format(i) # assigns the player number to the valid chosen position



def Next_move():
    x=[] # A list for saving player movements to use in the win conditions
    slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
    for i in range(1,4): #Takes the next move
        Next_move=getpass('P{:d} Pick a slot to move to \n(don\'t worry, it won\'t show on screen): '.format(i)) # here get pass was used to ensure that the players donnt see each others enteries.
        print()
        x.append(Next_move)
        
        
        while Next_move.isdigit() == False: #Makes sure the entery is digits
            Next_move=getpass('''!Cell invalid!
P{} Pick an valid cell to move to: '''.format(i))
        Next_move=int(Next_move)
        print()
        
        
        while Next_move>10 or Next_move<=0 : #makes sure the entery is valid numbers (from 1 to 9).
            Next_move=int(input('''!Cell invalid!
P{:d} Pick an valid cell: '''.format(i)))
            print()
            if 0<Next_move and Next_move<10:
                break
        slots[Next_move]='P{} '.format(i)
    z=Win_Condition(x)
    while z == 'replay':
        showBoard(slots)
        Next_move()
        Win_Condition(x)
    showBoard(slots)
        
        
def Win_Condition(x):
    '''
Win_Condition() is a function that needs no peremeters, it runs and tests for wining,
losing, draw, according to the movement of the players stored in X'''
    p1move = x[len(x)-3] #assigning each a player's move to a variable. every three indexes
    p2move = x[len(x)-2]
    p3move = x[len(x)-1]
    if p2move == p1move == p3move: #Functions that checks if player 1,2,and 3's moves were all to the same place then prints Draww
        print('Draww')
        print()
    
    elif p3move == p2move :
        print("Player 1 Winssss" )
        print()
    
    elif p3move == p1move :
        print("Player 2 Winssss" )
        print()
    
    elif p2move == p1move :
        print("Player 3 Winssss" )
        print()
    
    else:
        return 'replay'
runGame() ## remove this after testing. runGame is called from mainframe