
# 연습문제1 (L1-norm)

import numpy as np

def L1norm(v):         # v = 벡터
    nlen=len(v)       # 벡터의 길이를 먼저 파악
    out=0
    for i in range(0,nlen):
        out = out + abs(v[i])       # abs = 절댓값
    return out

tv = np.array([-1,2,3])

print("my nrom",L1norm(tv))
print("python norm", np.linalg.norm(tv,1))


# 연습문제2 (L2-norm)
import numpy as np        

def L2norm(v):
    nlen = len(v)
    out = 0
    for i in range(0,nlen):
        out = out + (v[i])**2
    out = out**(1/2)
    return out

tv = np.array([-1,2,3])

print('my l2 norm', L2norm(tv))
print('python l2 norm', np.linalg.norm(tv,2))


import numpy as np        
def Lpnorm(v,p):
    nlen = len(v)
    out = 0
    for i in range(0,nlen):
        out = out + (abs(v[i]))**p
    out = out**(1/p)
    return out

tv = np.array([-1,2,3])
    
print('my L5 norm ', Lpnorm(tv,5))
print("python l5 norm", np.linalg.norm(tv,5))
'''