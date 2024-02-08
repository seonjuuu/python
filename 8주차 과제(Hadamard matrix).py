#1
import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])
B=np.array([[-1,0,1,3,2],[1,1,6,11,-5],[3,-10,2,3,5]])
C=np.array([[-1,0,1],[2,3,10],[-7,3,2]])
D=np.zeros([5,15],dtype=int)
for i in range(0,5):
    for j in range(0,15):
        D[i][j] = 3*i-4*j+5
E=np.zeros([15,5],dtype=int)
for i in range(0,15):
    for j in range(0,5):
        E[i][j] = (-1)**(i+j)
      
print(A+C)
R2 = np.matmul(D,E)
print(R2)
print(np.matmul(B,R2))
print(A*C)

#2
import numpy as np

H2 = np.array([[1,1],[1,-1]])
print(H2)
print("row:", np.dot(H2[0],H2[1]))              
print("col", np.dot(H2[:,0],H2[:,1]))            # 열끼리 내적

  #H4
t = np.hstack((H2,H2))
print(t)
H4=np.hstack((H2,-H2))
H4=np.vstack((t,H4))

print(H4)

   #H8
t=np.hstack((H4,H4))
H8 = np.hstack((H4,-H4))
H8=np.vstack((t,H8))

print(H8)
