
import numpy as np

A=np.array([[3,2],[2,3],[2,-2]])
B=A.T

#Step 1 : B^T(3x2).B(2x3) => (3x3)
BtB=np.matmul(B.T,B)

val,vec=np.linalg.eig(BtB)

val=np.round(val,2)
print(val)

#Step 2 : Sigma => B
S=np.zeros([2,3])

cnt=0 #S의 index
for i in range(0,len(val)):
    if val[i]!=0:
        S[cnt,cnt]=val[i]
        cnt=cnt+1
S=S**(1/2)
#print(S) 
V=np.hstack((vec[:,[0]],vec[:,[2]],vec[:,[1]]))
#print(vec)
#print(V)

#Last step : U
# U[:,i]=1/S[i,i]*B*V[:,[i]]
u1=(1/S[0,0])*np.matmul(B,V[:,[0]])
u2=(1/S[1,1]*np.matmul(B,V[:,[1]]))
U=np.hstack((u1,u2))

print(U)

#B=U*S*V^T
ret=np.matmul(U,S)
ret=np.matmul(ret,V.T)
print(ret)

#A=V*S^T*U*T
Ub=V
S=S.T
V=U
#A=Ub*S*V^T
chk=np.matmul(Ub,S)
chk=np.matmul(chk,V.T)
print(chk)


# 실습 (Gran-Schmidt process를 이용해서 orthogonal basis 구하기)
import numpy as np

# proj_uv ( v->u 로 정사영 )
# (u.v)/(u.u) * u

def proj_uv(u,v):
    t0=np.dot(u,v)
    t1=np.dot(u,u)
    
    return (t0/t1)*u

v1=np.array([1,0,1])
v2=np.array([1,1,1])
v3=np.array([0,1,1])

u1=v1  #기준
u2=v2-proj_uv(u1,v2)
u3=v3-proj_uv(u1,v3)-proj_uv(u2,v3)

# orthogonal basis = 자기자신의 크기로 나눈 것
e1=u1/(np.linalg.norm(u1,2))  
e2=u2/(np.linalg.norm(u2,2))
e3=u3/(np.linalg.norm(u3,2))

#확인
A=np.vstack((e1,e2,e3))
ret=np.matmul(A,A.T)
print(np.round(ret))




# QR

#Step1
import numpy as np

A=np.array([[2,0,0],[1,2,1],[-1,0,1]])
a1=A[:,0]                                          # 열벡터 하나씩 뜯어오기
a2=A[:,1]
a3=A[:,2]

#gram schmidt
u1=a1
u2=a2-proj_uv(u1,a2)
u3=a3-proj_uv(u1,a3)-proj_uv(u2,a3)

# orthonomal basis = Q 구하기
e1=u1/(np.linalg.norm(u1,2))
e2=u2/(np.linalg.norm(u2,2))
e3=u3/(np.linalg.norm(u3,2))

Q=np.vstack((e1,e2,e3))
Q=Q.T

print(np.round(np.matmul(Q,Q.T)))

# R
R=np.zeros([3,3])
R[0,0]=np.dot(a1,e1)
R[0,1]=np.dot(a2,e1)
R[0,2]=np.dot(a3,e1)
R[1,1]=np.dot(a2,e2)
R[1,2]=np.dot(a3,e2)
R[2,2]=np.dot(a3,e3)

ret = np.matmul(Q,R)
print(A)
print(np.round(ret))