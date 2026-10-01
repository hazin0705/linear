import numpy as np

#행렬 A와 B 정의
A= np.array([
    [1,0,2],
    [2,-1,3],
    [4,1,8]
])

B = np.array([
    [-11,2,2],
    [-4,0,1],
    [6,-1,-1]
])

#3x3 단위행렬
I = np.eye(3,dtype=int)

#행렬곱 계산
AB = A@B
BA = B@A

print("A=")
print(A)

print("\nB=")
print(B)

print("\nAB=")
print(AB)

print("\nBA")
print(BA)

#단위행렬과 같은지 확인
print("\nAB=I",np.array_equal(AB,I))
print("BA=I",np.array_equal(BA,I))

if np.array_equal(AB,I) and np.array_equal(BA,I):
    print("\n A와 B는 서로 역행렬입니다")
    print("즉, B = A^-1이고 A = B^-1입니다.")

else :
    print("\n A와 B는 서로 역행렬이 아닙니다.")
 