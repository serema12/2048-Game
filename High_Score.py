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
