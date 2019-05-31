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
        Mess_To_Screen('Press U to undo 1 time (only 1 per',Color.Inactive_Color.value,100,0,390,250)
        Mess_To_Screen('game).',Color.Inactive_Color.value,80,0,75,300)
        Mess_To_Screen('- This game have restart, undo ',Color.Inactive_Color.value,105,0,400,375)
        Mess_To_Screen('function as well as score system.',Color.Inactive_Color.value,70,0,450,425)
        Button_For_Text('Back',285,265,60,60,230,270,170,40,Color.Board.value,Color.Inactive_Color.value,Color.Active_Color.value,'Medium','Back',None)
        game.display.update()
