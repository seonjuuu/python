from operator import matmul
from re import U
import numpy as np

A=np.array([[4,11,14],[8,7,-2]])

#step 1  (정사각행렬 만들기)
ATA=np.matmul(A.T,A)

values,vectors = np.linalg.eig(ATA)    # (고유값과 고유벡터)
values=np.int_(values)
print(values)

#step 2 (대각행렬)
nrow, ncol = A.shape
Sigma = np.zeros([nrow,ncol])
cnt=0
for i in range(0,len(values)):
    if(values[i]!=0):
        Sigma[cnt,cnt]=values[i]
        cnt=cnt+1
print(Sigma)

Sigma=Sigma**(1/2)
print(Sigma)

#step 3 ( V )       ( 90 과 0의 순서 바꾸기 )
print(vectors)
V=np.hstack((vectors[:,[0]],vectors[:,[2]],vectors[:,[1]]))
print(V)

#step 4 ( U ) 
u1 = (1/(Sigma[0,0]))*np.matmul(A,V[:,[0]])
u2 = (1/(Sigma[1,1]))*np.matmul(A,V[:,[1]])
print(u1)
print(u2)

U=np.hstack((u1,u2))
print(U)

ret = np.matmul(U,Sigma)
ret = np.matmul(ret,V.T)
print(ret)

# 연습문제1

import numpy as np
import random

random.randrange(0,10000)

A=np.array([[4,3],[-3,4]])
A=(1/5)*A

res=np.matmul(A,A.T)
res=np.round(res,2)
print(res)

# llAxll = llxll ??
# x = (2,1)

x = np.zeros([2,1])

flag = 0
for i in range(0,2):
    x[0,0]=random.randrange(0,1000)
    x[1,0]=random.randrange(0,1000)
    
    #compute Ax
    chk=np.matmul(A,x)
    # lAxl 크기 확인
    n1=np.round(np.linalg.norm(chk,2),2)
    # lxl 크기 확인
    n2=np.round(np.linalg.norm(x,2),2)
    
    if n1 != n2 :
        print("Different Norm, ERROR")
        flag = 1

if flag == 0 :
    print("CORRECT")
    

# 연습문제 2
import numpy as np

A=np.array([[3,2,2],[2,3,-2]])

#step1 : A^T*A
ATA =np.matmul(A.T,A)
val, vec = np.linalg.eig(ATA)
val=np.round(val,2)
print(val)

# step 2 ( Sigma marix 2x3 생성)
S=np.zeros([2,3])
cnt=0
for i in range(0,len(val)):
    if val[i] != 0 :
        S[cnt,cnt]=val[i]
        cnt=cnt+1
S=S**(1/2)
print(S)

#step 3 : V 
V=np.hstack((vec[:,[0]],vec[:,[2]],vec[:,[1]]))
print(vec)
print(V)

#step 4 : U ( U[:,i]=(1/sig(i))*A*V[:,i])

u1 = (1/S[0,0])*np.matmul(A,V[:,[0]])
u2 = (1/S[1,1])*np.matmul(A,V[:,[1]])
U=np.hstack((u1,u2))
print(U)

#step 5 : check
# A = U*S*V^T
chk = np.matmul(U,S)
chk = np.matmul(chk,V.T)
print(chk)