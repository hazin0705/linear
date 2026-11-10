import numpy as np

np.set_printoptions(precision=4, suppress=True)

A = np.array([
    [1,2],
    [4,3]
],dtype=float)

x = np.array([1,2],dtype=float)

eigenvalues, eigenvectors = np.linalg.eig(A)

order = np.argsort(eigenvalues)[::-1]

print("고유값과 대표 고유벡터")

for i in order:
    vector = eigenvectors[:,i]

    first = np.flatnonzero(np.abs(vector)> 1e-12)[0]
    vector = vector/vector[first]

    print(f"𝜆 = {eigenvalues[i]:g},고유벡터 = {vector}")

Ax = A @ x

print("\nx=",x)
print("Ax =",Ax)
print("5x =",5*x)
print("Ax = 5x인가?",np.allclose(Ax,5*x))

