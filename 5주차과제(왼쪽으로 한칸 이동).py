
#1
import numpy as np

A=np.zeros([15,15],dtype=int)

for i in range(0,15):
    for j in range(0,15):
        if (i+j)%2 == 0 :
            A[i,j] = 2
        else :
            A[i,j] = -1
print(A)

#2
import numpy as np
B=np.zeros([10,10],dtype=int)
B[0] = [1,2,0,-2,4,5,1,2,10,7]

for i in range(0,10):
    for j in range(0,10):
        if (i+j)%10 == 0 :
            B[i,j] = 1
        if (i+j)%10 == 1 :
            B[i,j] = 2
        if (i+j)%10 == 2 :
            B[i,j] = 0
        if (i+j)%10 == 3 :
            B[i,j] = -2
        if (i+j)%10 == 4 :
            B[i,j] = 4
        if (i+j)%10 == 5 :
            B[i,j] = 5
        if (i+j)%10 == 6 :
            B[i,j] = 1
        if (i+j)%10 == 7 :
            B[i,j] = 2
        if (i+j)%10 == 8 :
            B[i,j] = 10
        if (i+j)%10 == 9 :
            B[i,j] = 7
print(B)


#2
import numpy as np

B=np.zeros([10,10],dtype=int)
B[0] = [1,2,30,-2,4,5,1,2,10,7]                    # 첫번쨰 행에 대해서 나타내준것

for i in range(1,10) :
    for j in range(0,10):                            #0부터 시작 !! (열에 대한것은 아무것도 하기 않았기 때문)                  
        B[i,j]=B[i-1,(j+1)%10]
    
print(B)


#2 (좀 어려운 버전)
import numpy as np
C=np.zeros([10,10],dtype=int)
tt = [1,2,0,-2,4,5,1,2,10,7]

# ar을 입력받아 nshift만큼 왼쪽으로 이동시킴
def shift_lrotate(ar,nshift):
    out=[]
    nlen=len(ar)
    # ar 의 0번쨰부터 마지막까지
    for i in range(0,nlen):
        out.append(ar[(i+nshift)%nlen])
    return out

for i in range(0,10):
    C[i]=shift_lrotate(tt,i)
    
print(C)


#2 
import numpy as np
t1 = [1,2,0,-2,4,5,1,2,10,7,1,2,0,-2,3,4,1,2,10,7]    #2배행렬
B=np.zeros([10,10],dtype=int)

for i in rane(0,10):
    B[i] = t1[i:i+10]
    
print(B)


#실습2

import re
import numpy as np

def sum_row(A,nrow) :                      # A=행렬 nrow=입력받을 행
    nArow, nAcol = A.shape                   # shape => 순수하게 행과 열의 갯수 => TT의 행 갯수 : 2개 
    if nrow>=nArow :
        print("ERROR")
        return
    else:
        total=0
        for i in range(0,nAcol):
            total = total+A[nrow,i]
    return total

TT=np.array([[1,2,3],[4,5,6]])   # TT = 텍스트용 행렬
print('sum:',sum_row(TT,1))       # (TT,1) = 1행(4,5,6)의 합