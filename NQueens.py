n=int(input("enter the dimension:"))
import numpy as np
board=[[" "]*n for i in range(n)]
board=np.array(board)
n_fill=0
def checkPos(pos):
    pair=pos_ord.items()
    x,y=pos
    if y in pos_ord.values():
        return 0
    while x>=0 and y>=0:
        if (x,y) in pair:
            return 0
        x-=1;y-=1
    
    x,y=pos
    while x>=0 and y<n:
        if (x,y) in pair:
            return 0;
        x-=1;y+=1
    return 1
    pass
def queens(row=0):
    global n_fill,pos_ord;
    for x in range(n):
        if row==0 and n_fill!=n:
            n_fill=1
            pos_ord[row]=x;
            queens(row+1)
            if n_fill==row:
                n_fill-=1
    
        else:
            b=checkPos((row,x))
            if b:
                pos_ord[row]=x;
                
                n_fill+=1
    
                if n_fill!=n:
                    
                    queens(row+1)
                    
                    if n_fill==row+1:
                        del pos_ord[row]
                        n_fill-=1
            
            
pos_ord={}
queens()
for x in pos_ord.items():
    board[x]='Q'
print(board)
