import numpy as np

A=np.array([[2,0,0],[1,2,1],[-1,0,1]])

v=np.zeros([3,1])
u1=np.linalg.norm(A[:,0],2)
t0=2*u1*u1-2*A[0,0]*u1
t0=t0**(1/2)
print(t0)

v=np.zeros([3,1]) 

v[0,0]=A[0,0]-u1
v[0,0]=v[0,0]/t0
v[1,0]=A[1,0]/t0
v[2,0]=A[2,0]/t0

H1=np.identity(3)   #3x3
H1=H1-2*np.matmul(v,v.T)

A1=np.round(np.matmul(H1,A))
print(A1)

u2=np.linalg.norm(A1[1:,1],2)
t0=2*u2*u2-2*A1[1,1]*u2
t0=t0**(1/2)

v=np.zeros([2,1])
v[0,0]=A1[1,1]-u2
v[0,0]=v[0,0]/t0
v[1,0]=A1[2,1]/t0
H2=np.identity(2)
H2=H2-2*np.matmul(v,v.T)

#print(H2)

H=np.identity(3)
H[1:,1:]=H2

#print(H)

R=np.round(np.matmul(H,A1))
print(R)

Q=np.matmul(H,H1)
Q=Q.T

#check
print(np.round(np.matmul(Q,R)))

#연습문제1
import numpy as np

A=np.array([[3,1,0],[2,0,1],[1,1,1]])

nn=np.linalg.norm(A[:,0],2)
t0=2*nn*nn-2*A[0,0]*nn
t0=t0**(1/2)

v=np.zeros([3,1]) 

v[0,0]=A[0,0]-nn
v[0,0]=v[0,0]/t0
v[1,0]=A[1,0]/t0
v[2,0]=A[2,0]/t0

H1=np.identity(3)   #3x3
H1=H1-2*np.matmul(v,v.T)

A1=np.round(np.matmul(H1,A))
print(A1)

n2=np.linalg.norm(A1[1:,1],2)
t0=2*n2*n2-2*A1[1,1]*n2
t0=t0**(1/2)

v=np.zeros([2,1])
v[0,0]=A1[1,1]-n2
v[0,0]=v[0,0]/t0
v[1,0]=A1[2,1]/t0
H2=np.identity(2)
H2=H2-2*np.matmul(v,v.T)

#print(H2)

H=np.identity(3)
H[1:,1:]=H2

#print(H)

R=np.round(np.matmul(H,A1))
print(R)

Q=np.matmul(H,H1)
Q=Q.T

#check
print(np.round(np.matmul(Q,R)))

