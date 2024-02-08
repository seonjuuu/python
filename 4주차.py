# 대각선이 1이고 나머지가 -1인 10x10 행렬

import numpy as np

A=np.zeros([10,10],dtype=int)

for i in range(0,10):
    for j in range(0,10):
        if i==j :
            A[i,j] = 1
        else :
            A[i,j] = -1
print(A)

# (i+j) 가 짝수이면 1 , 홀수이면 0 인 행렬
import numpy as np

B=np.zeros([10,10],dtype=int)

for i in range(0,10):
    for j in range(0,10):
        if (i+j) % 2 == 0:
            B[i,j] = 1
        else :
            B[i,j] = 0
print(B)


# 중요!!!!
import numpy as np

C=np.zeros([10,10],dtype=int)

for i in range(0,10):
    for j in range(0,10):
        C[i,j] = i+j+1
                
print(C)

      




