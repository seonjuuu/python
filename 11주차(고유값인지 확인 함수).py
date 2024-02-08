import numpy as np

#행렬의 대각화
A=np.array([[1,-1],[-1,1]])

#step 1
values, vectors = np.linalg.eig(A)

print(values)
print(vectors)

#step 2
D=np.diag(values)
print(D)

#strp 3
P=vectors
pinv=np.linalg.inv(P)

#step 4
res=np.matmul(P,D)
res=np.matmul(res,pinv)
print(res)


# A^n 구현
import numpy as np
import time

 #일반적인 곱샘
ret = np.identity(2)
tic = time.perf_counter()
for i in range(0,200):      # A^200
    ret = np.matmul(ret,A)
toc = time.perf_counter()
print(f"Standard mul in {toc - tic:0.4f} seconds")
print(ret)

 #대각화 이용
tic = time.perf_counter()
dd = values**200
D=np.diag(dd)
res=np.matmul(P,D)
res=np.matmul(res,pinv)
toc = time.perf_counter()
print(f"diag mul in {toc-tic:0.4f} seconds")
print("res")




# A = PDP^-1 확인 

import numpy as np

A=np.array([[3,2,4],[2,0,2],[4,2,3]])

values, vectors = np.linalg.eig(A)

D=np.diag(values)
print(D)

P=vectors
pinv=np.linalg.inv(P)

res=np.matmul(P,D)
res=np.matmul(res,pinv)
print(res)



# PDP^-1 = PDP^T 확인
import numpy as np

B=np.array([[2,-1,0],[-1,2,-1],[0,-1,2]])

val2, vec2 = np.linalg.eig(B)
D=np.diag(val2)
P=vec2

pinv=np.linalg.inv(P)

#print(D)
#print(P)

res=np.matmul(P,D)
res=np.matmul(res,pinv)
print(res)

chk=np.matmul(P,D)
chk=np.matmul(chk,P.T)
print(chk)



# 주어진 값이 고유값인지 아닌지 확인하는 함수

import numpy as np

A=np.array([[6,-1],[2,3]])

#input : A (matric) n (scalar)
#output : eigenvalue(0) , not(1)

def is_eigenvalue(A,n):
    nrow , ncol = A.shape
    In = np.identity(nrow)
    In = n*In
    B=A-In
    if np.linalg.det(B) == 0 :
        return 0
    else:
        return 1
    
print(is_eigenvalue(A,5))
print(is_eigenvalue(A,3))