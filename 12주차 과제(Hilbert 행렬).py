#실습1-1

import numpy as np
import random

A=np.array([[1,-2,2],[2,-1,-2],[2,2,1]])
A=(1/3)*A

# Finction : generates random vector
# input : len , randrange
# output : vector

def gen_random_vec(nlen,n) :
    v=[]
    for i in range(0,nlen):
        v.append(random.randrange(0,n))
        
    return v

flag=0
for i in range(0,1000):
    x=gen_random_vec(3,1000)          # 3x3 행렬이므로 (3,1000)
    y=gen_random_vec(3,1000)
    
    chk1=np.dot(x,y)
    
    ax=np.matmul(A,np.array(x).T)
    ay=np.matmul(A,np.array(y).T)
    chk2=int(np.round(np.dot(ax,ay),0))
    
    if chk1 != chk2 :
        print("different")
        flag=1
        
if flag==1:
    print("different")
else:
    print("PASS")
    
1-2
#input : n
#output : nxn Hilbert martrix

def gen_hilbert(n):
    H=np.zeros([n,n])
    for i in range(0,n):
        for j in range(0,n):
            H[i,j]=1/(i+j+1)
    return H
#2
def compare_matrix(A,B):                        # 행렬 비교하는 함수 생성
    rA,cA=A.shape
    rB,cB=B.shape
    
    if rA!=rB:
        return 1
    if cA!=cB:
        return 2
    for i in range(0,rA):
        for j in range(0,cA):
            if A[i,j]!=B[i,j]:
                return 3
    return 0

# check if every eigenvalue >= 0
# 1 -> not positive definite                          # positive 행렬인지 확인
# 0 -> positive definite
def check_positive_definite(A):
    val,_=np.linalg.eig(A)
    val=np.round(val,2)
    for i in range(0,len(val)):
        if val[i]<0 :
            return 1
    
    return 0

H6=gen_hilbert(6)
HT=H6.T
ret=compare_matrix(H6,HT)
if ret == 0:
    print("Symmetric")
else:
    print("non-Symmetric")
    
val,vec = np.linalg.eig(H6)
val=np.round(val,2)
print(val)

ret = check_positive_definite(H6)
print(ret)

if ret == 0 :
    print("Possitive definite")
else :
    print("not positive definite")