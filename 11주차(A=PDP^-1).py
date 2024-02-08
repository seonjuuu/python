import numpy as np

A=np.array([[3,2,4],[2,0,2],[4,2,3]])
value, vector = np.linalg.eig(A)

Q=vector
D=np.diag(value)

print(D)

Qinv = np.linalg.inv(Q)
ret = np.matmul(Q,D)
ret=np.matmul(ret,Qinv)

print(ret)

I5=np.identity(3)  #3X3
I5=5*I5
print(I5)

Dp=D-I5       # B eigenvalues

#Q'DpQ'^-1 = B
chk = np.matmul(Q,Dp)
chk=np.matmul(chk,Qinv)

print(chk)

#B=A-5I
B=A-I5
print(B)
