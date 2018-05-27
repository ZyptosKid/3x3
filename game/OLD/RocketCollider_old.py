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
    '''rungame() initiates the gaming sequnce, with no need for parameters
    the board is printed and the game starts'''
    slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
    Movement_Tracing=[]
    z=len(Movement_Tracing)-1
    x=1
    showBoard(slots)
    print()
    initialmoves = set()
    for i in range(1,4):
        Start_point=int(input('P{:d} Pick a start point: '.format(i)))
        while Start_point>9 or Start_point<0 :
            print()
            Start_point=int(input('''!Cell invalid!
P{:d} Pick an valid cell: '''.format(i)))
            print()
            if 0<Start_point and Start_point<10:
                break

        while Start_point in initialmoves:
            Start_point=int(input('P{:d} Pick an unoccupied cell: '.format(i)))
            print()
            if Start_point not in initialmoves:
                print()
                break
        initialmoves.add(Start_point)

        slots[Start_point]='P{} '.format(i)
        Movement_Tracing+='{}'.format(Start_point)   
    slots[Start_point]='P{} '.format(i)
    Movement_Tracing+='{}'.format(Start_point)        
    showBoard(slots)
    print()
    print(
        '''!Movement System!
        you are practically allowed to move anyhow and go anywhere
        as long as you donnt collide
        goodluck surviving the rocket mash'''
        )
    print()
    while x!=0:
        slots=['[0]','[1]','[2]','[3]','[4]','[5]','[6]','[7]','[8]','[9]']
        for i in range(1,4):
            Next_move=int(getpass('P{:d} Pick a slot to move to \n(don\'t worry, it won\'t show on screen): '.format(i)))
            print()
            slots[Next_move]='P{} '.format(i)
            Movement_Tracing+='{}'.format(Next_move)
        showBoard(slots)
        if Movement_Tracing[z-1] == Movement_Tracing[z-2] == Movement_Tracing[z]:
            print('Draww')
            print()
            break
        elif Movement_Tracing[z] == Movement_Tracing[z-1]:
            print("Player 1 Winssss" )
            print()
            break
        elif Movement_Tracing[z] == Movement_Tracing[z-2]:
            print("Player 2 Winssss" )
            print()
            break
        elif Movement_Tracing[z-1] == Movement_Tracing[z-2]:
            print("Player 3 Winssss" )
            print()
            break
        
#     Newgame()


# def Newgame():
#     '''NewGame() is a function that starts a new round of the game
#      after taking the concent of the user
#     '''
#     New_game=input('Wanna play again? Y/A-Z ')
#     if New_game.lower() == 'y':
#         rungame()
#     else:
#         print('Thanks for playing our game XD')