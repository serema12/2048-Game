def Game_Over():
    Gamedisplay.fill(Color.Cream.value)
    Over= True
    while Over :
        Mess_To_Screen("Game Over",Color.TextDark.value,300,70,60,60,size='Large')
        Button_For_Text("Play Again",150,180,60,60,80,190,200,40,Color.Inactive_Color.value,Color.Active_Color.value,"Medium","Play Again")
            
        for event in game.event.get():
            if event.type==game.QUIT:
                game.quit()
                quit()
        game.display.update()   
    event = game.event.wait()
