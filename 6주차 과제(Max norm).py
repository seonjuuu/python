import numpy as np

# Max norm : 성분 중 절댓값이 가장 큰 값
def Maxnrom(v):
    nlen=len(v)       
    max_v = abs(v[0])                     # 먼저 벡터 첫번째 원소의 절댓값을 최댓값으로 생각
    for i in range(1,nlen):                
        if abs(v[i])>max_v:                 # 다음 원소의 절댓값을 비교
            max_v=abs(v[i])
    return max_v

tv = np.array([-1,2,-3])

print("my nrom",Maxnrom(tv))
print("python norm", np.linalg.norm(tv,np.inf))

def my_max(v):
    #길이확인
    nlen=len(v)
    max=v[0]
    for i in range(1,nlen):
        if max<v[i]:
            max=v[i]
    return max

w=np.array([-1,3,5,6,2,8,10,-12])
print("my mac:", my_max(w))

def max_norm(v):
    w=abs(v)
    out=max(w)
    return out

v=np.array([-5,1,2])
print("my_norm", max_norm(v))
print("python norm", np.linalg.norm(v,np.inf))

# 피보나치 수열 
def fibo(n):
    if n == 0 :
        return 0
    if n == 1 :
        return 1
    else:
        return fibo(n-1) + fibo(n-2)

#a=[]    
for i in range(5):
    print(fibo(i))
   # a.append(fibo(i))
#print(a)
