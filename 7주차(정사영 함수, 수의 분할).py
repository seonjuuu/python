import numpy as np

# np.dot
v = np.array([-1,0,1])
w = np.array([2,3,4])

print(np.dot(v,w))



# 벡터의 내적 구하는 함수 만들기
def vector_dot(v,w):
    nlen = len(v)                        #길이측정
    out = 0
    for i in range(0,nlen):
        out = out +v[i]*w[i]
        return out
    
v=np.array([-1,2,3])                      #테스트
w=np.array([2,-1,0])

print("my 내적:", vector_dot(v,w))
print("python 내적 :",np.dot(v,w))

    
# 오류측정 ( 두벡터의 길이가 다를때 => 에러 )
def vector_dot(v,w):
    nlen1 = len(v)
    nlen2 = len(w)
    #오류측정
    if nlen1 != nlen2 :
        print("error, 길이가 다름")
        return                       
    out = 0
    for i in range(0,nlen1):
        out = out +v[i]*w[i]
        return out
    
v=np.array([-1,2,3])                      
w=np.array([2,-1,0])
u=np.array([1,2])

print("my 내적:", vector_dot(v,u))
print("python 내적 :",np.dot(v,w))


      
# 정사영 벡터 구하는 함수 만들기

#input:v,w
#output : w로 정사영시킨 v벡터

def proj_wv(v,w):
    vw=np.dot(v,w)
    ww=np.dot(w,w)
    k=vw/ww 
    return k*w

v=np.array([-1,2,3])                      
w=np.array([2,-1,0])

print("proj_w(v)", proj_wv(v,w))


#Lpnorm과 max 합치기
import numpy as np

  #input : v, p
  #output : norm
def Lpnorm(v,p):
    #if inf
    if p=='inf':
        w=abs(v)
        out = max(w)
        return out
    #p>=1
    else :
        out=0
        w=abs(v)
        for i in range(0,len(w)):
            out = out + w[i]**p
        return out**(1/p)
            
v=np.array([-5,1,2])
print('my nrom:', Lpnorm(u,3))
print("python norm:", np.linalg.norm(u,3))
print("my inf norm:", Lpnorm(u,'inf'))
print('python inf norm:', np.linalg.norm(u,np.inf))



#수의 분할 구하기
import numpy as np

A=np.zeros([10,10],dtype=int)

A[0,0]=1

A[1,0]=1
A[1,1]=1

A[2,0]=1
A[2,1]=1
A[2,2]=1

A[3,0]=1
A[3,1]=2
A[3,2]=1
A[3,3]=1

A[4,0]=1
A[4,1]=2
A[4,2]=2
A[4,3]=1
A[4,4]=1

for n in range(5,10): #행
    A[n,0]=1                
    for r in range(1,n):
        A[n,r]=A[n-1,r-1]+A[n-r-1,r]
    A[n,n]=1
    
print(A)