from getpass import getpass

#slots=['0','1','2','3','4','5','6','7','8','9'] ## why do you still have those?
def showBoard(Gboard):
    '''showboard(board) makes the board and assigns a number for each slot,
making the board and its contents susebtable for modification'''
    print('' +Gboard[1]+ ' | ' +Gboard[2]+ ' | '+Gboard[3] )
    print('----------------')
    print('' +Gboard[4]+ ' | ' +Gboard[5]+ ' | '+Gboard[6] )
    print('----------------')
    print('' +Gboard[7]+ ' | ' +Gboard[8]+ ' | '+Gboard[9] )
#showBoard(slots) ## why do you still have those?



def runGame():
    '''runGame() starts the game by initiating the code that takes intial places from players'''
    Baby_steps()
    ## more stuff here, try to make the function more.. functional.. See code comments below to understand




def Baby_steps(): ## name this to something meaningful?
    ## fix the function description
    '''rungame() runs the initial choice of slots sequence,
with no need for parameters, the board is printed and the game starts RIGHT NOW'''
    slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]'] ## put this in runGame() and call it as an argument here. For variety. Or even put it in global code i dunno. whatever you think is better
    showBoard(slots)
    print()
    initialmoves = []
    
    #starts taking the initial places of the players
    for i in range(1,4): ## why range 1,4? needs explaining like "range 1,4 to run the loop only three times, and not range(3) because i is used as an actual condition checker that requires it to be 1, 2, and 3".
        Start_point=input('P{} Pick a start point: '.format(i)) ## I suggest making range(3), and .format(i+1) for just cosmetics and aesthetics.
        
        

        while Start_point.isdigit() == False: #Makes sure the player entery is digits ## what if the player enters the number like this: [1]? either specify the shape of input in the input prompt or make a condition to turn [1] into a valid int('1') input.
            Start_point=input('''!Cell invalid!
P{} Pick an valid cell: '''.format(i))
        print()
        Start_point=int(Start_point) ## what does this line do?
        
        
        while Start_point>9 or Start_point<0 : #makes sure the entery is valid numbers (from 1 to 9) ## 0 is not >9 or <0.. does that mean it won't enter the loop? Case Test here
            Start_point=int(input('''!Cell invalid!
P{:d} Pick an valid cell: '''.format(i))) ## why {:d} here but only {} there?
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
        slots[Start_point]='P{} '.format(i) ## a little explaination here as to what this assignment means
    #slots[Start_point]='P{} '.format(i) ## why do you still have those?
    
    ## move this to runGame() and make sure it still works...
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
    ##... up to here





def Win_Condition():
    '''
Win_Condition() is a function that needs no peremeters, it runs and tests for wining,
losing, draw, according to the movement of the players stored in the Movement_tracing() function'''
    x=[] ## what's this for? generally speaking, it's good to tell what your empty variable is assigned for in assigning, and giving it a meaningful name 
    while x!=0: #infinite loop to run the game infinitly or till a player wins
        ## will this loop have a better placement outside of the win checker? seems like win_condition() is both defining and running the game AND checking for wins. Too much functionality for one function. 
        ## Try to make another function from this that runs the game and keep this only for the win condition checking. The other function could have the x record list and the while loop (?)
        slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]'] ## redefining slots again?? what if the first move is the destination move (aka player stays in place?)
        
        
        
        for i in range(1,4): #Takes the next move
            Next_move=getpass('P{:d} Pick a slot to move to \n(don\'t worry, it won\'t show on screen): '.format(i)) ## explain your approach with getpass briefly, why did you use that function?
            print()
            x.append(Next_move)
            
            
            
            while Next_move.isdigit() == False: #Makes sure the entery is digits
                Next_move=getpass('''!Cell invalid!
P{} Pick an valid cell to move to: '''.format(i))
            Next_move=int(Next_move)
            slots[Next_move]='P{} '.format(i)
            print()
        showBoard(slots)
        
        ## do you have something that checks if the selection is digit but not in the board here? Test Case and see.
        
        

        p1move = x[len(x)-3] #assigning each a player's move to a variable. every three indexes
        p2move = x[len(x)-2]
        p3move = x[len(x)-1]
        if p2move == p1move == p3move: #Functions that check for the win ##very vague, try to describe each condition instead in english (ex. if player 1,2,and3's moves were all to the same place)
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
runGame() ## remove this after testing. runGame is called from mainframe


## why are those still here?
#     Newgame()

# def Newgame():
#     '''NewGame() is a function that starts a new round of the game
#after taking the concent of the user'''
#     New_game=input('Wanna play again? Y/A-Z ')
#     if New_game.lower() == 'y':
#         rungame()
#     else:
#         print('Thanks for playing our game XD')
