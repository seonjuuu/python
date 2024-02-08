
#연습문제

import numpy as np
A = np.array([[1,0,-1,2],[2,3,4,1],[-5,2,1,0],[7,2,1,0]])
B = np.array([[1,2,0,-1]])

print(A+B)
print(A-B)
print(A*B)

# 단위벡터를 계산하는 함수 만들기
import numpy as np

# input : v
#output : 1/llvll * v

def unit_vector(v) :
    nlen = len(v)
    k = 0
    for i in range(0,nlen):
        k = (k +v[i]**2)
    k = k**(1/2)
    if k==0:
        print("zero vector")
        return 0
    
    return(1/k)*v

w=np.array([1,2,3])
print("unit vector", unit_vector(w))
