import numpy as np

#행렬 정의
A = np.array([
    [1,2],
    [1,3]
],dtype = float)

B = np.array([
    [3,2],
    [2,2]
],dtype=float)

#각각의 역행렬
A_inv = np.linalg.inv(A)
B_inv = np.linalg.inv(B)

#행렬곱 AB
AB = A@B

#식의 왼쪽:(AB)^-1
left = np.linalg.inv(AB)

#식의 오른쪽: B^-1
right = B_inv @ A_inv

np.set_printoptions(precision=3, suppress=True)

print("A^-1 =")
print(A_inv)

print("\nB^-1 =")
print(B_inv)

print("\nAB =")
print(AB)

print("\n(AB)^-1=")
print(left)

print("\nB^-1 A^-1 =")
print(right)

#두 결과가 같은지 확인
print("\n(AB)^-1 = B^-1 A^-1인가?")
print(np.allclose(left,right))