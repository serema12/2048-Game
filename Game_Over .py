def Win(score):
    Gamedisplay.fill(Color.Screen.value)
    Over= True
    while Over :
        Mess_To_Screen("Score",Color.Board.value,200,2,60,60,size='Medium')
        Mess_To_Screen(str(score),Color.TextDark.value,200,30,60,60,size='Medium')
        Mess_To_Screen("Highest",Color.Board.value,400,2,60,60,size='Medium')
        Mess_To_Screen(str(score),Color.TextDark.value,400,30,60,60,size='Medium')
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
def Game_Over(score):
    Gamedisplay.fill(Color.Screen.value)
    Over= True
    while Over :
                       
        Mess_To_Screen("Score",Color.Board.value,200,2,60,60,size='Medium')
        Mess_To_Screen(str(score),Color.TextDark.value,200,30,60,60,size='Medium')
        Mess_To_Screen("Highest",Color.Board.value,400,2,60,60,size='Medium')
        Mess_To_Screen(str(score),Color.TextDark.value,400,30,60,60,size='Medium')
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
