'''
# 삼각행렬
import numpy as np

A=np.array([[1,2,3],[4,5,6],[7,8,9]])

lower = np.tril(A)
upper = np.triu(A)

print(lower)
print("")
print(upper)
'''
# 대각 성분 추출
import numpy as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

Ad = np.diag(A)
print("==Diagonal element of A ==")
print(Ad)
print("==Generating diagonal matrix==")
D = np.diag(Ad)
print(D)

print("==Generating diagonal matrix==")
l = [1,2,3,4]
Dl = np.diag(l)
print(Dl)

# Transpose 
import numpy  as np

A = np.array([[1,2,3],[4,5,6],[7,8,9]])

At = A.T
print("== A ==")
print(A)

print("==Transpose of A ==")
print(A)

# 역행렬
import numpy as np

C = np.array([[1,2],[3,4]])
print("==Inverse of C ==")
print(np.linalg.inv(C))

# Trace
import numpy as np

B = np.array([[1,2,3,1],[4,5,6,2],[7,8,9,3]])
print("Trace:", np.trace(B))

# Rank
import numpy as np

A1 = np.array([[1,1,1],[0,1,1],[0,0,1]])
print("Ranj A1 :", np.linalg.matrix_rank(A1))

A2 = np.array([[1,1,1],[1,0,1],[2,1,2]])
print("Rank A2: ", np.linalg.matrix_rank(A2))

# 연습문제
#1
import numpy as np

A = np.array([[3,5,7,2],[1,4,7,2],[6,3,9,17],[13,5,4,16]])

print(A.T)
print("Trace:", np.trace(A))
Ad = np.diag(A)
print(np.diag(Ad))
print(np.linalg.det(A))
print(np.linalg.inv(A))

B = np.array([[4,-2,3],[8,-3,5],[7,-2,4]])
print(B.T)
print("Trace:", np.trace(B))
print(np.diag(B[1]))
print(np.linalg.det(B))
print(np.linalg.inv(B))

#2 (trace 를 계산하는 함수)

#input : 행렬
#output : trace (대각 성분의 합)

#버전1 (추천)
def matrix_trace(A):
    d = np.diag(A)
    return sum(d)

#버전2
def matrix_trace_2(A):
    nrow, ncol = A.shape
    ret = 0
    for i in range(0,nrow):
        for j in range(0,ncol):
            if i == j :
                ret = ret+A[i,j]
    return ret
 
# 테스트 함수
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[1,2,3],[4,5,6]])

print(matrix_trace(A))
print(matrix_trace(B))
print(matrix_trace_2(A))
print(matrix_trace_2(B))

#3-1 ( 두 벡터 사이의 넓이 구하기)
import numpy as np

#input : v1, v2
#output : area (넓이,스칼라)

def ares_bycrossproduct(v1,v2):
    k=np.cross(v1,v2)
    
    return abs(k)

v1 = np.array([1,2])
v2 = np.array([3,4])

print("area_cross", ares_bycrossproduct(v1,v2))

#3-2 
import numpy as np

def area_by_def(v1,v2):
    d = np.vstack((v1,v2))
    ret = np.linalg.det(d)
    return abs(ret)


v1 = np.array([1,2])
v2 = np.array([3,4])

print("area_det", area_by_def(v1,v2))