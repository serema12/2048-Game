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
smallfont=game.font.SysFont(None,30)
mediumfont=game.font.SysFont(None,40)
largefont=game.font.SysFont(None,130)
image=game.image.load('2048.png')
icon=game.image.load('2048alpha.png')
menu=game.image.load('Menu2048.png')
volume=game.image.load('Volume.png')
volumeoff=game.image.load('VolumeOff.png')
volume=game.transform.scale(volume,(50,50))
volumeoff=game.transform.scale(volumeoff,(50,55))
image=game.transform.scale(image,(215,135))
menu=game.transform.scale(menu,(315,350))

game.display.set_icon(icon)
game.mixer.init()
game.mixer.music.load('Music.mp3')
sfx=game.mixer.Sound("NoSFX.mp3")
clock=game.time.Clock()
##set color
class Color(Enum):
    Screen = (140, 235, 205)
    Cream = (255,235,205)
    White = (255,255,255)
    WhiteB = (185,226,247)
    
    DeepOrange = (234,120,33)
    Block0 = (204, 192, 179)
    Block2 = (238, 228, 218)
    Block4 = (255, 218, 195)
    Block8 = (231, 176, 142)
    Block16 = (231, 191, 142)
    Block32 = (255, 196, 195)
    Block64 = (231, 148, 142)
    Block128 = (183, 94, 132)
    Block256 = (190, 94, 86)
    Block512 = (156, 57, 49)
    Block1024 = (112, 23, 16)
    Block2048 = (86, 46, 95)
    TextLight = (255, 244, 234)
    TextDark = (119, 110, 101)
    Inactive_Color = (255,255,255)
    Active_Color = (255,0,0)
    Board=(79,79,255)
    Yellow=(255,255,0)
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
            
        
        #Mess_To_Screen("2048",Color.White.value,275,20,60,60,size='Large')
        Button_For_Text("Start Game",430,60,60,60,370,70,170,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Start Game',None)
        Button_For_Text("Intro",430,120,60,60,370,130,170,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Intro',None)
        Button_For_Text("Options",430,180,60,60,370,190,170,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Options','Active')
        Button_For_Text("Quit",430,240,60,60,370,250,170,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Quits',None)
        Gamedisplay.blit(menu,[0,0])
        game.display.update()
#Introduction
def Intro():
    Gamedisplay.fill(Color.Screen.value)
    introduction=True
    while introduction:
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
        game.draw.rect(Gamedisplay,(0,0,0),[70,50,450,210],5)
        game.draw.rect(Gamedisplay,Color.Board.value,[70,50,450,210])
        Mess_To_Screen('- To play the game simply use  ',Color.Inactive_Color.value,150,0,300,150)
        Mess_To_Screen('up, down, left and right arrows.',Color.Inactive_Color.value,110,0,350,200)
        Mess_To_Screen('- This game have restart, undo:  ',Color.Inactive_Color.value,105,0,400,275)
        Mess_To_Screen('function as well as score system.',Color.Inactive_Color.value,70,0,450,325)
        Button_For_Text('Back',285,265,60,60,230,270,170,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Back',None)
        game.display.update()
#def button
def Button_For_Text(text,x_text,y_text,width_text,height_text,x_rec,y_rec,width_rec,height_rec,color_rec,inactive_color,active_color,size,action=None,default=None):
    Mouse_Pos=game.mouse.get_pos()
    Mouse_Click=game.mouse.get_pressed()
    if x_text+width_text>Mouse_Pos[0]>x_text and y_text+height_text>Mouse_Pos[1]>y_text:
        game.draw.rect(Gamedisplay,Color.TextDark.value,[x_rec,y_rec,width_rec,height_rec],5)
        game.draw.rect(Gamedisplay,color_rec,[x_rec,y_rec,width_rec,height_rec])
        Mess_To_Screen(text,active_color,x_text,y_text,width_text,height_text,size)
        if Mouse_Click[0]==1 and action!=None:
            if action=='Quits':
                game.quit()
                quit()
            elif action=='Start Game':
                main()
            elif action=='Options':
                if default == 'Active':
                    Option('Menu')
                else:
                    Option('Game')
            elif action=='Intro':
                Intro()
            elif action=='Back':
                Menu()
            elif action=='Back2':
                return False    
            elif action=='Play Again':
                main()
            elif action=='Restart':
                Restart()
            elif action=='Quit':
                game.quit()
                quit()
        game.display.update()       
    else:
        game.draw.rect(Gamedisplay,Color.TextDark.value,[x_rec,y_rec,width_rec,height_rec],5)
        game.draw.rect(Gamedisplay,color_rec,[x_rec,y_rec,width_rec,height_rec])
        Mess_To_Screen(text,inactive_color,x_text,y_text,width_text,height_text,size)
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
def Option(Case):
    
    option=True
    while option:
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
        if (Case=='Menu'):
            Gamedisplay.fill(Color.Screen.value)
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
            Button_For_Text('Back',315,280,60,60,260,290,170,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Back')
        elif (Case=='Game'):
            Gamedisplay.fill(Color.Block8.value)
            game.draw.rect(Gamedisplay,(0,0,0),[120,100,400,175],5)
            game.draw.rect(Gamedisplay,Color.Block4.value,[120,100,400,175])
            Mess_To_Screen(' Music ',Color.White.value,180,105,60,60)
            Gamedisplay.blit(volume,[325,105])
            Gamedisplay.blit(volumeoff,[420,105])
            Button_For_Icon(325,105,50,50,'Volume')
            Button_For_Icon(420,105,50,50,'Volume Off')
            Mess_To_Screen(' SFX   ',Color.White.value,180,185,60,60)
            Gamedisplay.blit(volume,[325,185])
            Gamedisplay.blit(volumeoff,[420,185])
            Button_For_Icon(325,185,50,50,'SFX')
            Button_For_Icon(420,185,50,50,'SFXOff')
            regis=Button_For_Text('Back',315,280,60,60,260,290,170,40,Color.Block4.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Back2')
            if regis == False:
                option=False
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
                if (SCORE[pow(2,i)]=='128'):
                    text=mediumfont.render(board[y][x],True,Color.White.value)
                elif (SCORE[pow(2,i)]=='256'):
                    text=mediumfont.render(board[y][x],True,Color.White.value)
                elif (SCORE[pow(2,i)]=='512'):
                    text=mediumfont.render(board[y][x],True,Color.White.value)
                elif (SCORE[pow(2,i)]=='1024'):
                    text=mediumfont.render(board[y][x],True,Color.White.value)
                elif (SCORE[pow(2,i)]=='2048'):
                    text=mediumfont.render(board[y][x],True,Color.White.value)
               
                game.draw.rect(Gamedisplay,COLOR_SWITCHER[pow(2,i)],[y*(GAME_WIDTH_END-GAME_WIDTH_START)/4 +GAME_WIDTH_START,x*(GAME_HEIGHT_END-GAME_HEIGHT_START)/4 +GAME_HEIGHT_START,(GAME_HEIGHT_END-GAME_HEIGHT_START)/4,(GAME_HEIGHT_END-GAME_HEIGHT_START)/4])
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
def Score(board):
    Sum=0
    for y in range(4):
        for x in range (4):
             Sum+=(int)(board[y][x])
    return Sum
def High_Score(score):
    h=open('highscore.txt','r')
    highscore=h.read()
    if (int)(highscore)<(int)(score):
        h1=open('highscore.txt','w')
        h1.write(score)
        h1.close()
        h.close()
        
        return score
    else:
        h.close()
        return highscore

    
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
#def undo
def Undo (board,boardr):
        
        
        for y in range (4):
            for x in range(4):
                board[y][x]=boardr[y][x]
        Draw_Board(board)
        
#text when win
def Win(score,highscore):
    Gamedisplay.fill(Color.Screen.value)
    Over= True
    while Over :
        Mess_To_Screen("Score",Color.Board.value,200,2,60,60,size='Medium')
        Mess_To_Screen(str(score),Color.TextDark.value,200,30,60,60,size='Medium')
        Mess_To_Screen("Highest",Color.Board.value,400,2,60,60,size='Medium')
        Mess_To_Screen(str(highscore),Color.TextDark.value,400,30,60,60,size='Medium')
        Mess_To_Screen("YOU WIN !",Color.Yellow.value,300,130,60,60,size='Large')
        Button_For_Text("Play Again",170,210,60,60,110,220,180,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,"Medium","Play Again",None)
        Button_For_Text("Quit",420,210,60,60,360,220,180,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,"Medium","Quit",None)
        Button_For_Text("Menu",300,280,60,60,240,290,180,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,"Medium","Menu",None)
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
        game.display.update()   
    event = game.event.wait()
#text when game over
def Game_Over(score,highscore):
    Gamedisplay.fill(Color.Screen.value)
    Over= True
    while Over :
                       
        Mess_To_Screen("Score",Color.Board.value,200,2,60,60,size='Medium')
        Mess_To_Screen(str(score),Color.TextDark.value,200,30,60,60,size='Medium')
        Mess_To_Screen("Highest",Color.Board.value,400,2,60,60,size='Medium')
        Mess_To_Screen(str(highscore),Color.TextDark.value,400,30,60,60,size='Medium')
        Mess_To_Screen("GAME OVER!",Color.Yellow.value,300,130,60,60,size='Large')
        Button_For_Text("Play Again",170,210,60,60,110,220,180,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,"Medium","Play Again",None)
        Button_For_Text("Quit",420,210,60,60,360,220,180,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,"Medium","Quit",None)
        Button_For_Text("Menu",300,280,60,60,240,290,180,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,"Medium","Menu",None)
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
        game.display.update()   
    event = game.event.wait()
#Restart
def Restart():
    main()
#main play 
def main():
    
    board = Init_Board()
    #undo
    boardr=Init_Board()
    undo = 0 
    while True:
        Gamedisplay.fill(Color.Block8.value)
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
            if event.type == game.KEYDOWN:
                if event.key == game.K_u and undo == 0:
                    Undo(board,boardr)
                    undo+=1
                for y in range (4):
                        for x in range (4):
                            boardr[y][x]= board[y][x]
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
                

        #undo
        
        #draw the game board
        Sum=Score(board)
        HighScore=High_Score((str)(Sum))
        game.draw.rect(Gamedisplay,Color.Block4.value,[45,170,215,140])
        Gamedisplay.blit(image,[45,20])
        game.draw.rect(Gamedisplay,Color.Block0.value,[GAME_WIDTH_START,GAME_HEIGHT_START,BOARD_THICKNESS,BOARD_THICKNESS])
        Draw_Board(board)
        for y in range (4):
            for x in range(4):
                game.draw.rect(Gamedisplay,Color.TextDark.value,[y*(GAME_WIDTH_END-GAME_WIDTH_START)/4 +GAME_WIDTH_START,x*(GAME_HEIGHT_END-GAME_HEIGHT_START)/4 +GAME_HEIGHT_START,BLOCK_WIDTH,BLOCK_HEIGHT],5)
        Draw_Board(board)
        if Check_Lose(board):
            Game_Over(Sum,HighScore)
        if Check_Win(board):
            Win(Sum,HighScore)
        game.draw.rect(Gamedisplay,Color.TextDark.value,[45,170,215,145],5)
        
        game.draw.rect(Gamedisplay,Color.Block128.value,[60,180,75,65])
        Mess_To_Screen("Score",Color.WhiteB.value,65,170,65,60,size='Small')
        Mess_To_Screen(str(Sum),Color.TextLight.value,65,195,65,60,size='Small')
        game.draw.rect(Gamedisplay,Color.TextDark.value,[60,180,75,65],2)
        
        game.draw.rect(Gamedisplay,Color.Block128.value,[155,180,90,65])
        Mess_To_Screen("Highest",Color.WhiteB.value,170,170,60,60,size='Small')
        Mess_To_Screen(str(HighScore),Color.TextLight.value,170,195,60,60,size='Small')
        game.draw.rect(Gamedisplay,Color.TextDark.value,[155,180,90,65],2)

        Button_For_Text('Restart',88,250,20,60,60,260,75,40,Color.Block128.value,Color.Inactive_Color.value,Color.Active_Color.value,'Small','Restart',None)

        Button_For_Text('Options',190,250,20,60,155,260,90,40,Color.Block128.value,Color.Inactive_Color.value,Color.Active_Color.value,'Small','Options','Game')
       
        game.display.update()
   
if __name__ == '__main__':
    
    Menu()
    
