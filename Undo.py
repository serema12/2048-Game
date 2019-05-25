#def undo
def Undo (board,boardr):
        
        
        for y in range (4):
            for x in range(4):
                board[y][x]=boardr[y][x]
        Draw_Board(board)
def main():
    while True:
        if event.type == game.KEYDOWN:
                if event.key == game.K_u and undo == 0:
                    Undo(board,boardr)
                    undo+=1
                for y in range (4):
                        for x in range (4):
                            boardr[y][x]= board[y][x]
