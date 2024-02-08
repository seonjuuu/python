import numpy as np

def gram_schmidt(basis):
  n= len(basis)
  orthogonal_basis = np.zeros_like(basis,dtype=np.float64)  #basis 크기만큼 만들어줌(0으로 채움)
  
  orthogonal_basis[0] = basis[0] #첫번째 벡터는 그 자체로 직교 벡터
  for i in range(1, n):
        projection = np.zeros_like(basis[i],dtype=np.float64)
        for j in range(i):
            projection += np.dot(basis[i], orthogonal_basis[j]) / np.dot(orthogonal_basis[j], orthogonal_basis[j]) * orthogonal_basis[j]
        orthogonal_basis[i] = basis[i] - projection
  return orthogonal_basis


def lll_reduction(basis, delta):
      n = len(basis)
      orthogonal_basis = gram_schmidt(basis)
      mu = np.zeros((n, n), dtype=np.float64)
      flag=0
      while(flag==0):
        for i in range(2,n+1,1):
              for j in range(i-1, 0, -1):  #1까지
                mu[i-1,j-1] = np.dot(orthogonal_basis[j-1],basis[i-1])/np.dot(orthogonal_basis[j-1],orthogonal_basis[j-1])
                basis[i-1]=basis[i-1]-mu[i-1,j-1]*basis[j-1]
                orthogonal_basis = gram_schmidt(basis)
                print(mu[i-1,j-1])
              
              if np.dot(orthogonal_basis[i-1], orthogonal_basis[i-1]) <= (delta - mu[i-1, i-2]) * np.dot(orthogonal_basis[i-2], orthogonal_basis[i-2]):
                    basis[i-1], basis[i-2] = basis[i-2], basis[i-1]
                    orthogonal_basis = gram_schmidt(basis)
                    flag=0
              else:
                    flag=1
      return basis


def check_lll_reduced(basis, delta):
    n = len(basis)
    orthogonal_basis = gram_schmidt(basis)
    
    # 직교성 확인
    for i in range(n):
        for j in range(i):
            dot_product = np.dot(orthogonal_basis[i], orthogonal_basis[j])
            if not np.isclose(dot_product, 0):
                return False
            else:
                return True
            
    # 𝛿-LLL 조건 확인
    for i in range(2, n):
        for j in range(i-1, 0, -1):
            mu_ij = np.dot(orthogonal_basis[j], basis[i]) / np.dot(orthogonal_basis[j], orthogonal_basis[j])
            lhs = np.linalg.norm(mu_ij * orthogonal_basis[j]) ** 2
            rhs = np.linalg.norm(orthogonal_basis[i]) ** 2
            if not np.isclose(lhs * np.linalg.norm(basis[j]) ** 2, rhs, rtol=0, atol=delta):
                return False
            else:
                return True
    
'''   
    # 벡터의 길이 확인
    for i in range(n):
        length = np.linalg.norm(orthogonal_basis[i])
        if not np.isclose(length, 1):
            return False
        else:
            return True

    # 직교성 확인
    for i in range(n):
        for j in range(i):
            dot_product = np.dot(orthogonal_basis[i], orthogonal_basis[j])
            if not np.isclose(dot_product, 0):
                return False
    
    # 𝛿-LLL 조건 확인
    for i in range(2, n):
        for j in range(i-1, 0, -1):
            mu_ij = np.dot(orthogonal_basis[j], basis[i]) / np.dot(orthogonal_basis[j], orthogonal_basis[j])
            lhs = np.linalg.norm(mu_ij * orthogonal_basis[j]) ** 2
            rhs = np.linalg.norm(orthogonal_basis[i]) ** 2
            if not np.isclose(lhs * np.linalg.norm(basis[j]) ** 2, rhs, rtol=0, atol=delta):
                return False
'''    
    



basis = np.array([[1,2,3],[4,5,6],[7,8,9]])  # 격자 기저
delta = 3/4  # 매개변수 delta

reduced_basis = lll_reduction(basis, delta)
print(reduced_basis)
print(check_lll_reduced(basis, delta))             
                  
