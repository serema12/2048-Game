def Menu():
    
    Intro = True
    Gamedisplay.fill(Color.Screen.value)
    game.mixer.music.play(-1)
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
                
    else:
        game.draw.rect(Gamedisplay,(0,0,0),[board,y+10,170,40],5)
        game.draw.rect(Gamedisplay,(176,106,72),[board,y+10,170,40])
        Mess_To_Screen(text,inactive_color,x,y,width,height,size)
#button for icon
def Button_For_Icon(x,y,width,height,action=None):
    Mouse_Pos=game.mouse.get_pos()
    Mouse_Click=game.mouse.get_pressed()
    if x+width>Mouse_Pos[0]>x and y+height>Mouse_Pos[1]>y:
        if Mouse_Click[0]==1 and action!=None:
            if action=='Volume Off':
                game.mixer.music.stop()
            elif action=='Volume':
                game.mixer.music.play(-1)
#option
def Option():
    Gamedisplay.fill(Color.Screen.value)
    Option=True
    while Option:
        game.draw.rect(Gamedisplay,(0,0,0),[120,100,400,175],5)
        game.draw.rect(Gamedisplay,Color.Board.value,[120,100,400,175])
        Mess_To_Screen('Music',Color.Inactive_Color.value,180,100,60,60)
        Gamedisplay.blit(volume,[300,105])
        Gamedisplay.blit(volumeoff,[400,105])
        Button_For_Icon(300,105,50,50,'Volume')
        Button_For_Icon(400,105,50,50,'Volume Off')
        Button_For_Text('Back',315,280,60,60,260,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Back')
        game.display.update()
