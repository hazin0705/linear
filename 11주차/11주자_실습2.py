import numpy as np
from fractions import Fraction
from math import lcm

np.set_printoptions(precision=4, suppress=True)

A = np.array([
    [3,-1,-1],
    [-12,0,5],
    [4,-2,-1]
])

coefficients = (-1)**len(A)*np.poly(A)

print("특성다항식 det(A-ƛI):")
print(np.poly1d(np.round(coefficients,10), variable="ƛ"))

eigenvalues, eigenvectors = np.linalg.eig(A)

for i in np.argsort(eigenvalues):
    eigenvalue = eigenvalues[i]
    vector = eigenvectors[:,i]

    vector = vector/vector[np.argmax(np.abs(vector))]
    fractions = [
        Fraction(float(t)).limit_denominator(1000)
        for t in vector
    ]
    common = lcm(*(f.denominator for f in fractions))
    x = np.array([int(f*common) for f in fractions])

    if x[np.flatnonzero(x)[0]] < 0:
        x = -x

    print(f"\n고유값 ƛ = {eigenvalue:g}")
    print("고유벡터 x = ",x)
    print("Ax =",A@x)
    print("Ax = ƛx확인:",
          np.allclose(A@x,eigenvalue*x))

