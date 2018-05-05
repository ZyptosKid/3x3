#slots=['0','1','2','3','4','5','6','7','8','9']
def shwBoard(board):
    print('' +board[1]+ '  | ' +board[2]+ '  | '+board[3] )
    print('' +board[4]+ '  | ' +board[5]+ '  | '+board[6] )
    print('' +board[7]+ '  | ' +board[8]+ '  | '+board[9] )
#shwBoard(slots)

def Start_Game():
    slots=['0','1','2','3','4','5','6','7','8','9']
    Movement_Tracing=[]
    z=len(Movement_Tracing)-1
    x=1
    shwBoard(slots)
    for i in range(1,4):
        Start_point=int(input('P{:d} Pick a start point: '.format(i)))
        Movement_Tracing+='{}'.format(Start_point)
        if slots[Start_point]=='P2' or slots[Start_point]=='P1' or slots[Start_point]=='P3':
            Start_point=int(input('P{:d} Pick an unoccupied cell: '.format(i)))
            slots[Start_point]='P{}'.format(i)
            Movement_Tracing+='{}'.format(Start_point)
        else:    
            slots[Start_point]='P{}'.format(i)
            Movement_Tracing+='{}'.format(Start_point)
    shwBoard(slots)
    print(
        '''!Movement System!
        you are practically allowed to move anyhow and go anywhere
        as long as you donnt collide
        goodluck surviving the rocket mash'''
        )
    while x!=0:
        slots=['0','1','2','3','4','5','6','7','8','9']
        for i in range(1,4):
            Next_move=int(input('P{:d} Pick a slot to move to: '.format(i)))
            slots[Next_move]='P{}'.format(i)
            Movement_Tracing+='{}'.format(Next_move)
        shwBoard(slots)
        if Movement_Tracing[z] == Movement_Tracing[z-1]:
            print("Player 1 Winssss" )
            break
        elif Movement_Tracing[z] == Movement_Tracing[z-2]:
            print("Player 2 Winssss" )
            break
        elif Movement_Tracing[z-1] == Movement_Tracing[z-2]:
            print("Player 3 Winssss" )
            break
        else:
            print('Draww')
    Newgame()


def Newgame():
    New_game=input('Wanna play again? Y/A-Z ')
    if New_game.lower() == 'y':
        Start_Game()
    else:
        print('Thanks for playing our game XD')

Start_Game()
