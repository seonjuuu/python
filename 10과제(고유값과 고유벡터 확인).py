#선형사상에 대응하는 행렬 구하기

import numpy as np

A=np.array([[-1,2,1,3,4],[0,0,2,-1,0]])

v1 = np.array([[1],[2],[3],[4],[5]])
v2 = np.array([[1],[0],[1],[0],[1]])
v3 = np.array([[1],[-1],[1],[-1],[1]])

print(A)

print("==1==")
print(np.matmul(A,v1))

print("==2==")
print(np.matmul(A,v2))

print("==3==")
print(np.matmul(A,v3))





#고유값과 고유벡터 확인

import numpy as np
A=np.array([[1,-1],[-1,1]])
values, vectors = np.linalg.eig(A)

print(values)
print(vectors)

#check eigenvector
# imput : matrix , vector
# output : 0 (not eigenvector) 1 (eigenvector)

def check_eigen(A,v):
    nrow, ncol = A.shape
    res = np.matmul(A,v)
    k=(res[0]/v[0])
    chk=k*v
    
    ret = 0
    for i in range(0,nrow):
        if chk[i] != res[i]:
            ret=1
            
    return ret

def check_eigen2(A,v):
    res = np.matmul(A,v)
    res=res/v
    nrow,ncol = res.shape
    print(res)
    c=res[0]
    ret=0
    for i in range(1,nrow):
        if c != res[i]:
            ret=1
    return ret

print("==check eigenvector==")
r=check_eigen(A,vectors[:,[0]])
v2=np.array([[2],[1]])
r2 = check_eigen2(A,v2)
print(vectors[:,[0]])

if(r==0):
    print("eigenvector")
else:
    print("Not eigenvector")
    
A=np.array([[-3,1,-3],[20,3,10],[2,-2,4]])
B=np.array([[7,4,6,],[-3,-1,-8],[0,0,1]])

valA,vecA=np.linalg.eig(A)
valB,vecB=np.linalg.eig(B)

print("A:eigenvector/value")
print(valA)
print(vecA)

print("B:eigenvector/value")
print(valB)
print(vecB)