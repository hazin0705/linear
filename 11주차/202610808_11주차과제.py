import numpy as np

A = np.array([
    [3,-1,-1],
    [-12,0,5],
    [4,-2,-1]
], dtype=float)


eigenvalues, X =np.linalg.eig(A)

order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:,order]

lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("X =")
print(X)
print("\nlamda =")
print(lamda)


# 행렬 A 정의: A = [3, 2; 3, -2]
A = np.array([[3, 2],
              [3, -2]])

# 고유값과 고유벡터 구하기: [X, lamda] = eig(A)
eigenvalues, X = np.linalg.eig(A)

# MATLAB의 lamda처럼 대각행렬 형태로 변환
lamda = np.diag(eigenvalues)

print("X (고유벡터 행렬) =\n", np.round(X, 4))
print("\nlamda (고유값 대각행렬) =\n", lamda)



A = np.array([
    [3, -1, -1],
    [-12, 0, 5],
    [4, -2, -1]
], dtype=float)

# 고유값과 고유벡터 계산
eigenvalues, X = np.linalg.eig(A)

# MATLAB 화면처럼 고유값을 2, 1, -1 순서로 정렬
order = np.argsort(eigenvalues)[::-1]
eigenvalues = eigenvalues[order]
X = X[:, order]

# 고유값을 대각행렬로 변환
lamda = np.diag(eigenvalues)

np.set_printoptions(precision=4, suppress=True, floatmode="fixed")

print("X =")
print(X)
print("\nlamda =")
print(lamda)


# (1) 상부삼각행렬 A 정의 및 고유값 계산
A = np.array([[0, 0, 0],
              [0, 2, 5],
              [0, 0, -1]])
eig_A = np.linalg.eigvals(A)
print("(1) 행렬 A의 고유값:", eig_A)

# (2) 하부삼각행렬 B 정의 및 고유값 계산 (MATLAB 창에서는 변수명 A로 입력됨)
B = np.array([[4, 0, 0],
              [0, 0, 0],
              [1, 0, -3]])
eig_B = np.linalg.eigvals(B)
print("(2) 행렬 B의 고유값:", eig_B)
