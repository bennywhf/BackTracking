left = 0
up = 1
right = 2
down = 3

from time import sleep
class iq_solve:
    def __init__(self):
        self.board = [
                      ['u','u','p','p','p','u','u'],
                      ['u','u','p','p','p','u','u'],
                      ['p','p','p','p','p','p','p'],
                      ['p','p','p','e','p','p','p'],
                      ['p','p','p','p','p','p','p'],
                      ['u','u','p','p','p','u','u'],
                      ['u','u','p','p','p','u','u']]
        self.peg = 32
        self.inv = [] # stack of previous move

    def move(self,i,j,d):
        p = self.board[i][j]
        if(p == 'u' or p == 'e'):
            raise Exception('Invalid Move. Tried moving '+ p + ' at location '+ str(i)+" "+str(j))

        if(d == 0): #left
            if (self.board[i][j-1] != 'p' or self.board[i][j-2]!= 'e') and j>=2:
                raise Exception('Invalid Move. Left at',i,j)
            self.board [i][j-1] = 'e'
            self.board [i][j-2] = 'p'
                
        if(d == 1): #up
            if (self.board[i-1][j] != 'p' or self.board[i-2][j] != 'e') and i>=2:
                raise Exception('Invalid Move. Up at',i,j)
            self.board [i-1][j] = 'e'
            self.board [i-2][j] = 'p'
                
        if(d == 2):#right
            if self.board[i][j+1] != 'p' or self.board[i][j+2] != 'e':
                raise Exception('Invalid Move. Right at',i,j)
            self.board [i][j+1] = 'e'
            self.board [i][j+2] = 'p'
                
        if(d == 3):#down
            if self.board[i+1][j] != 'p' or self.board[i+2][j] != 'e':
                raise Exception('Invalid Move. Down at',i,j)
            self.board [i+1][j] = 'e'
            self.board [i+2][j] = 'p'
            
        self.board[i][j] = 'e'
        self.inv.append((i,j,d))
        self.peg-=1
        return

    def pegNum(self):
        return self.peg

    def Solve(self):
        PM = []
        
        while (self.peg > 1):
            temp = []
            for i in range(7):
                for j in range(7):
                    if self.board[i][j] == 'p':
                        try:
                            if (self.board[i-2][j] =='e' and self.board[i-1][j] == 'p') and i>=2:
                                temp.append(lambda v,i=i,j=j: v.move(i,j,up))
                        except Exception:
                            pass
                        try:
                            if self.board[i+2][j] =='e' and self.board[i+1][j] == 'p':
                                temp.append(lambda v,i=i,j=j: v.move(i,j,down))
                        except Exception:
                            pass
                        try:
                            if self.board[i][j+2] =='e' and self.board[i][j+1] == 'p':
                                temp.append(lambda v,i=i,j=j: v.move(i,j,right))
                        except Exception:
                            pass
                        try:
                            if (self.board[i][j-2] =='e' and self.board[i][j-1] == 'p') and j>=2:
                                temp.append(lambda v,i=i,j=j: v.move(i,j,left))
                        except Exception:
                            pass
            while(len(temp) == 0):
                self.backTrack()
                temp = PM.pop()
            Nex = temp.pop()
            PM.append(temp)
            Nex(self)
            
        return (self.inv)
            
            
    def backTrack(self):
        i,j,d = self.inv.pop()
        self.board[i][j] = 'p'
        if d == 0: #left
            self.board[i][j-1] = 'p'
            self.board[i][j-2] = 'e'
        elif d == 1:#up
            self.board[i-1][j] = 'p'
            self.board[i-2][j] = 'e'
        elif d == 2:#right
            self.board[i][j+1] = 'p'
            self.board[i][j+2] = 'e'            
        else:#down
            self.board[i+1][j] = 'p'
            self.board[i+2][j] = 'e'
        self.peg+=1

    def __str__(self):
        s = '\n'
        for i in self.board:
            s+= str(i) + "\n"

        return s

if __name__ == '__main__':
    print('this solution assumes that the board is 7 x 7.')
    print('only 32 valid tiles,however.')
    d = {0:'left',1:'up',2:'right',3:'down'}
    q = iq_solve()
    l = q.Solve()
    for i in l:
        print(i[0],i[1],d[i[2]])
        
