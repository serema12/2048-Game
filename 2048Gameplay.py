import pygame as game
from enum import Enum
import random
import time,sys
#declare
WIDTH=630
HEIGHT=350
BLOCK_HEIGHT=80
BLOCK_WIDTH=80
GAME_WIDTH_START=280
GAME_HEIGHT_START=20
BOARD_THICKNESS=320
GAME_WIDTH_END=600
GAME_HEIGHT_END=340
BOARD=[]
#init
game.init()
Gamedisplay=game.display.set_mode((WIDTH,HEIGHT))
game.display.set_caption('2048')
smallfont=game.font.SysFont(None,25)
mediumfont=game.font.SysFont(None,40)
largefont=game.font.SysFont(None,75)
image=game.image.load('20.png')
icon=game.image.load('2048alpha.png')
menu=game.image.load('Menu2048.png')
volume=game.image.load('Volume.png')
volumeoff=game.image.load('VolumeOff.png')
volume=game.transform.scale(volume,(50,50))
volumeoff=game.transform.scale(volumeoff,(50,55))
image=game.transform.scale(image,(150,150))
menu=game.transform.scale(menu,(315,350))
game.display.set_icon(icon)
game.mixer.init()
game.mixer.music.load('Music.mp3')
sfx=game.mixer.Sound("NoSFX.mp3")
clock=game.time.Clock()
##set color
class Color(Enum):
    White = (255,255,255)
    DeepOrange = (234,120,33)
    Block0 = (204, 192, 179)
    Block2 = (238, 228, 218)
    Block4 = (237, 224, 200)
    Block8 = (242, 177, 121)
    Block16 = (244, 149, 99)
    Block32 = (245, 121, 77)
    Block64 = (245, 93, 55)
    Block128 = (238, 232, 99)
    Block256 = (237, 176, 77)
    Block512 = (236, 176, 77)
    Block1024 = (235, 148, 55)
    Block2048 = (234, 120, 33)
    TextLight = (255, 244, 234)
    TextDark = (119, 110, 101)
    Inactive_Color = (255,255,255)
    Active_Color = (255,0,0)
    Screen=(140,156,96)
    Board=(176,106,72)
BLACKGROUND_COLOR =Color.Block0.value
TEXT_COLOR=Color.TextDark.value
COLOR_SWITCHER={
        0   : Color.Block0.value,
        2   : Color.Block2.value,
        4   : Color.Block4.value,
        8   : Color.Block8.value,
        16  : Color.Block16.value,
        32  : Color.Block32.value,
        64  : Color.Block64.value,
        128 : Color.Block128.value,
        256 : Color.Block256.value,
        512 : Color.Block512.value,
        1024: Color.Block1024.value,
        2048: Color.Block2048.value,
        }
#set score
SCORE={
    0      : '0',
    2      : '2',
    4      : '4',
    8      : '8',
    16     : '16',
    32     : '32',
    64     : '64',
    128    : '128',
    256    : '256',
    512    : '512',
    1024   : '1024',
    2048   : '2048',
    }

        
#init the board
def Init_Board():
    board = []
    for i in range(4):
        board += [["0"] * 4]
    Create_Block(board, 2)      
    return board
#Menu
def Menu():
    
    Intro = True
    Gamedisplay.fill(Color.Screen.value)
    
    while Intro:
        
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
            if event.type==game.KEYDOWN:
                if event.key==game.K_p:
                    Intro=False
                if event.key==game.K_q:
                    game.quit()
                    quit()
        
        #Mess_To_Screen("2048",Color.White.value,275,20,60,60,size='Large')
        Button_For_Text("Start Game",430,60,60,60,370,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Start Game')
        Button_For_Text("Feats",430,120,60,60,370,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Feats')
        Button_For_Text("Options",430,180,60,60,370,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Options')
        Button_For_Text("Quits",430,240,60,60,370,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Quits')
      
        Gamedisplay.blit(menu,[0,0])
        
        
        game.display.update()
#def button
def Button_For_Text(text,x,y,width,height,board,inactive_color,active_color,size,action=None):
    Mouse_Pos=game.mouse.get_pos()
    Mouse_Click=game.mouse.get_pressed()
    if x+width>Mouse_Pos[0]>x and y+height>Mouse_Pos[1]>y:
        game.draw.rect(Gamedisplay,(0,0,0),[board,y+10,170,40],5)
        game.draw.rect(Gamedisplay,Color.Board.value,[board,y+10,170,40])
        Mess_To_Screen(text,active_color,x,y,width,height,size)
        if Mouse_Click[0]==1 and action!=None:
            if action=='Quits':
                game.quit()
                quit()
            elif action=='Start Game':
                main()
            elif action=='Options':
                Option()
            elif action=='Back':
                Menu()
        game.display.update()       
    else:
        game.draw.rect(Gamedisplay,(0,0,0),[board,y+10,170,40],5)
        game.draw.rect(Gamedisplay,(176,106,72),[board,y+10,170,40])
        Mess_To_Screen(text,inactive_color,x,y,width,height,size)
#button for icon
def Button_For_Icon(x,y,width,height,action=None):
    global sfx
    Mouse_Pos=game.mouse.get_pos()
    Mouse_Click=game.mouse.get_pressed()
    if x+width>Mouse_Pos[0]>x and y+height>Mouse_Pos[1]>y:
        if Mouse_Click[0]==1 and action!=None:
            if action=='Volume Off':
                game.mixer.music.stop()
            elif action=='Volume':
                game.mixer.music.play(-1)
            elif action=='SFX':
                sfx=game.mixer.Sound('SFX.mp3')
            elif action=='SFXOff':
                sfx=game.mixer.Sound('NoSFX.mp3')
#option
def Option():
    Gamedisplay.fill(Color.Screen.value)
    option=True
    while True:
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
            if event.type==game.KEYDOWN:
                if event.key==game.K_p:
                     Intro=False
                if event.key==game.K_q:
                    game.quit()
                    quit()
        game.draw.rect(Gamedisplay,(0,0,0),[120,100,400,175],5)
        game.draw.rect(Gamedisplay,Color.Board.value,[120,100,400,175])
        Mess_To_Screen(' Music ',Color.Inactive_Color.value,180,105,60,60)
        Gamedisplay.blit(volume,[325,105])
        Gamedisplay.blit(volumeoff,[420,105])
        Button_For_Icon(325,105,50,50,'Volume')
        Button_For_Icon(420,105,50,50,'Volume Off')
        Mess_To_Screen(' SFX   ',Color.Inactive_Color.value,180,185,60,60)
        Gamedisplay.blit(volume,[325,185])
        Gamedisplay.blit(volumeoff,[420,185])
        Button_For_Icon(325,185,50,50,'SFX')
        Button_For_Icon(420,185,50,50,'SFXOff')
        Button_For_Text('Back',315,280,60,60,260,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Back')
        game.display.update()

#Random block     
def Create_Block(board,n):
    for i in range(n):
        newNum =str(random.choice([2,4]))
        randomy = random.randrange(0,4)
        randomx = random.randrange(0,4)
        while (board [randomy][randomx]!="0"):
            randomy = random.randrange(0,4)
            randomx = random.randrange(0,4)
        board [randomy][randomx]=newNum   
#draw a text for menu
def Draw_Text(text,color,size):
    if   (size =='Medium'):
        textSurface=mediumfont.render(text,True,color)
    elif (size =='Small') :
        textSurface=smallfont.render(text,True,color)
    elif (size =='Large') :
        textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()
def Mess_To_Screen(text,color,buttonx,buttony,width,height,size='Medium'):
    textSurf,textRect=Draw_Text(text,color,size)
    textRect.centerx=buttonx + width/2   
    textRect.centery=buttony + height/2
    Gamedisplay.blit(textSurf,textRect)
#draw Block
def Build_Text(board,y,x):
    if board[y][x]=="0":
       text=mediumfont.render(" ",True,Color.DeepOrange.value)
    else :
       text=mediumfont.render(board[y][x],True,Color.TextDark.value)
       for i in range(1,12):
           if board[y][x]==SCORE[pow(2,i)]:
               
               game.draw.rect(Gamedisplay,COLOR_SWITCHER[pow(2,i)],
                              [y*(GAME_WIDTH_END-GAME_WIDTH_START)/4 +GAME_WIDTH_START,x*(GAME_HEIGHT_END-GAME_HEIGHT_START)/4 +GAME_HEIGHT_START,(GAME_HEIGHT_END-GAME_HEIGHT_START)/4,(GAME_HEIGHT_END-GAME_HEIGHT_START)/4])
               game.draw.rect(Gamedisplay,Color.TextDark.value,[y*(GAME_WIDTH_END-GAME_WIDTH_START)/4 +GAME_WIDTH_START,x*(GAME_HEIGHT_END-GAME_HEIGHT_START)/4 +GAME_HEIGHT_START,80,80],5)
    textRect=text.get_rect()
    textRect.centerx=y*(GAME_WIDTH_END-GAME_WIDTH_START)/4 +GAME_WIDTH_START +BLOCK_WIDTH/2
    textRect.centery=x*(GAME_HEIGHT_END-GAME_HEIGHT_START)/4 +GAME_HEIGHT_START +BLOCK_HEIGHT/2
    return text,textRect

def Draw_Board(board):
    for y in range(4):
        for x in range(4):
            Gamedisplay.blit(Build_Text(board,y,x)[0],Build_Text(board,y,x)[1])
#move
def Push(board,y_list,x_list,y_direction,x_direction):
    move=0
    for y in y_list:
        for x in x_list:
            if board[y+y_direction][x+x_direction]=="0":
                board[y+y_direction][x+x_direction]=board[y][x]
                if board[y][x]!=0:
                    move+=1
                board[y][x] ="0"
    return move
def Merge(board,y_list,x_list,y_direction,x_direction):
    move=0
    for y in y_list:
        for x in x_list:
            if board[y][x]==board[y+y_direction][x+x_direction]:
                board[y+y_direction][x+x_direction]=str(int(board[y+y_direction][x+x_direction])+int(board[y][x]))
                if board[y][x] != 0:
                    move+=1
                board[y][x]="0"
    return move
                
def Push_Direction(board,userInput):
    move =0
    if    userInput == "l":
        y_list,x_list=range(1,4),range(4)
        y_direction,x_direction=-1,0
    elif  userInput == "r":
        y_list,x_list=range(2,-1,-1),range(4)
        y_direction,x_direction=1,0
    elif  userInput == "u":
        y_list,x_list=range(4),range(1,4)
        y_direction,x_direction=0,-1
    elif  userInput == "d":
        y_list,x_list=range(4),range(2,-1,-1)
        y_direction,x_direction=0,1

    for i in range(4):
        move+=Push(board,y_list,x_list,y_direction,x_direction)
    move+=Merge(board,y_list,x_list,y_direction,x_direction)
    for i in range(4):
        move+=Push(board,y_list,x_list,y_direction,x_direction)
    return move
#check win 
def Check_Win(board):
    for y in range(4):
        for x in range(4):
            if board[y][x]=="2048":
                return True
    return False
#check each block if they can move 
def Check_Cell(board,y,x):
    move_y=[]
    move_x=[]
    board_size=len(board)
    if y>0:
        move_y.append(-1)
        move_x.append(0)
    if y<(board_size-1):
        move_y.append(1)
        move_x.append(0)
    if x>0:
        move_y.append(0)
        move_x.append(-1)
    if x<(board_size-1):
        move_y.append(0)
        move_x.append(1)
    
    for i in range(len(move_y)):
        if board[y+move_y[i]][x+move_x[i]]==board[y][x]:
            return True
    return False
def Can_Move(board):
    board_size=len(board)
    for y in range(board_size):
        for x in range(board_size):
            if  board[y][x]==0:
                return True
            if Check_Cell(board,y,x):
                return True
    return False
def Check_Lose(board):
    nozero= False
    for elt in board:
        nozero = nozero or ("0" in elt)
    if not nozero:
        return not Can_Move(board)
    return False
def Game_Loop(board,user_input):
    if not Check_Lose(board) and not Check_Win(board):
        move = Push_Direction(board,user_input)
        if move !=0:
            Create_Block(board,1)
        
    return board
#text when game over
def Game_Over():
    textGameOver = mediumfont.render("GAME OVER",True,Color.TextDark.value)
    textRect = Gamedisplay.get_rect()
    textRect.centerx=400
    textRect.centery=200
    Gamedisplay.blit(textGameOver,textRect)
    event = game.event.wait()

#main play 
def main():
    
    Gamedisplay.fill(Color.White.value)
    
    board = Init_Board()
    
    while True:
        
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
            if event.type == game.KEYDOWN:
                if event.key == game.K_DOWN:
                    board=Game_Loop(board,"d")
                    sfx.play()
                if event.key == game.K_UP:
                    board=Game_Loop(board,"u")
                    sfx.play()
                if event.key == game.K_LEFT:
                    board=Game_Loop(board,"l")
                    sfx.play()
                if event.key == game.K_RIGHT:
                    board=Game_Loop(board,"r")
                    sfx.play()
        #draw the game board
        Gamedisplay.blit(image,[0,0])
        game.draw.rect(Gamedisplay,Color.Block2048.value,[GAME_WIDTH_START,GAME_HEIGHT_START,BOARD_THICKNESS,BOARD_THICKNESS])
        Draw_Board(board)
        for y in range (4):
            for x in range(4):
                game.draw.rect(Gamedisplay,Color.TextDark.value,[y*(GAME_WIDTH_END-GAME_WIDTH_START)/4 +GAME_WIDTH_START,x*(GAME_HEIGHT_END-GAME_HEIGHT_START)/4 +GAME_HEIGHT_START,BLOCK_WIDTH,BLOCK_HEIGHT],5)
        Draw_Board(board)
        if Check_Lose(board):
            Game_Over()
        game.display.update()
   
if __name__ == '__main__':
    Menu()
    main()
