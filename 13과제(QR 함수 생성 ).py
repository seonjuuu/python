from re import T
import numpy as np

#1-1
#output : (u,v)/(u,u)*u
def proj_uv(u,v):
    t0=np.dot(u,v)
    t1=np.dot(u,u)
    
    return (t0/t1)*u

#input : matrix A (nxn) , column vectors of A are linarly independent
#output : orthonomal basis

def gram_schmidt_mat(A):
    _,ncol=A.shape
    
    Q=np.zeros([ncol,ncol])
    Q[0]=A[:,0]                           # Q의 0번쨰 행
    for i in range(1,ncol):               # 1부터
        Q[i]=A[:,i]
        
        for j in range(0,i):                     #0부터 
            Q[i]=Q[i]-proj_uv(Q[j],Q[i])
            
    #normalize = 크기가 1인 애들 만들기
    for i in range(0,ncol):
        Q[i]=Q[i]/(np.linalg.norm(Q[i],2))
        
    return Q.T

#check
A=np.array([[1,1,0],[0,1,1],[1,1,1]])

Q=gram_schmidt_mat(A)

print(np.round(np.matmul(Q,Q.T)))


#1-2
#imput : nxn matrix A
#output : Q,R such that A=QR , and Q^-1=Q^T , R=upper triangular
def QR_decompose(A):
    nrow,ncol=A.shape
    
    Q=gram_schmidt_mat(A)                                       # 1번 문제의 함수 이용
    R=np.zeros([nrow,nrow])                                # R구하기
    
    for i in range(0,nrow): #row
        for j in range(0,nrow): #column
            if i<= j :
                R[i,j]=np.dot(A[:,j],Q[:,i])
                
    return Q,R

#check
A=np.array([[2,0,0],[1,2,1],[-1,0,1]])
Q,R=QR_decompose(A)

#A=QR
chk=np.matmul(Q,R) 
print(A)
print(np.round(chk))  