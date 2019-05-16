def Score(board):
    Sum=0
    for y in range(4):
        for x in range (4):
             Sum+=(int)(board[y][x])
    return Sum
