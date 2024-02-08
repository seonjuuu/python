import numpy as np
#연습문제1

A = np.array([[4,4,2,3,-2],[0,1,-2,-2,2],[6,12,11,2,-4],[9,20,10,10,-6],[15,28,14,5,-3]])

v1 = np.array([[4],[-3],[1],[2],[0]])
v2 = np.array([[2],[-2],[0],[2],[-2]])
v3 = np.array([[1],[1],[0],[1],[3]])

res1 = np.matmul(A,v1)
print(res1)
k=int(res1[0]/v1[0])
print(k)

chk1=k*v1
print(chk1)             # res1 값 = chk1 값이 같으면 고유벡터
ret = 0

for i in range(0,5) :
    if chk1[i] != res1[1] :
        ret = 1
        
if(ret==1):
    print("Not eigenvector")
else :
    print("eigenvector")
    
res2 = np.matmul(A,v2)
k2=int(res2[0]/v2[0])
chk2=k2*v2

ret2=0
for i in range(0,5):
    if chk2[i] != res2[i] :
        ret2 = 1

if(ret2==1):
    print("Not eigenvector")
else :
    print("eigenvector")
    
res3 = np.matmul(A,v3)
k3=int(res3[0]/v3[0])
chk3=k3*v3

print(res3)
ret3=0
for i in range(0,5):
    if chk3[i] != res3[i] :
        ret3 = 1
        
if(ret3==1) :
    print("Not eigenvector")
else :
    print("eigenvector")
    

    
#연습문제2 (고유벡터인지 확인하는 함수)

import numpy as np

A = np.array([[4,4,2,3,-2],[0,1,-2,-2,2],[6,12,11,2,-4],[9,20,10,10,-6],[15,28,14,5,-3]])

v1 = np.array([[4],[-3],[1],[2],[0]])
v2 = np.array([[2],[-2],[0],[2],[-2]])
v3 = np.array([[1],[1],[0],[1],[3]])

def chk_eigenvector(A,v):
    nrow, ncol=A.shape
    res=np.matmul(A,v)
    k=int(res[0]/v[0])
    chk=k*v
    
    ret=0
    for i in range(0,nrow):
        if (chk[i] != res[i]):
            ret=1
    
    if (ret==0) :
        print("eigenvector")
    else :
        print("Not eigenvector")
        
chk_eigenvector(A,v1)
chk_eigenvector(A,v2)
chk_eigenvector(A,v3)