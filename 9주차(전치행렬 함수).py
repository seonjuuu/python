#1번
import numpy as np

def my_function(A):
    nrow, ncol = A.shape
    At=np.zeros([ncol,nrow], dtype=int)
    for i in range(0,nrow):
        for j in range(0,ncol):
            At[i,i] = A[i,j]
    return At

A = np.array([[1,2,3],[4,5,6]])
print(my_function(A))

#2번 (위삼각)
import numpy as np

def my_triu(A):
    nrow,ncol = A.shape
    
    for i in range(0,nrow):
        for j in range(0, ncol):
            if i > j :
                A[i,j] = 0
    return A

def my_triu_new(A):
    nrow, ncol = A.shape
    B = np.zeros([nrow,ncol],dtype=int)
    
    for i in range(0,nrow):
        for j in range(0,ncol):
            if i<=j:
                B[i,j] = A[i,j]
    return B

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(my_triu_new(A))
print(A)
print(my_triu(A))

# 아래삼각

def my_tril(A):
    nrow,ncol = A.shape
    
    for i in range(0,nrow):
        for j in range(0, ncol):
            if i < j :
                A[i,j] = 0
    return A

def my_tril_new(A):
    nrow, ncol = A.shape
    B = np.zeros([nrow,ncol],dtype=int)
    
    for i in range(0,nrow):
        for j in range(0,ncol):
            if i>=j:
                B[i,j] = A[i,j]
    return B

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(my_tril_new(A))
print(A)
print(my_tril(A))
 
