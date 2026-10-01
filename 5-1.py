import numpy as np

A = np.array([
    [2,1,3,4],
    [0,1,1,0],
    [1,0,1,1],
    [4,2,1,-1]
], dtype =int)

original_A = A.copy()
swap_count = 0

def show(step,matrix):
    print(f"\n{step}")
    print(matrix)

show("초기행렬 A", A)

#1 r1과 r3 교환
A[[0,2]]=A[[2,0]]
swap_count +=1
show("1단계:R1 <-> R3",A)

#2 첫 번째 열의 아래쪽 원소를 0으로 만듦
A[2] = A[2] - 2*A[0]
show("2단계:R3<- R3-2R1",A)

A[3] = A[3] - 4*A[0]
show("3단계:R4<- R4-4R1",A)

#3 두 번째 열의 아래쪽 원소를 0으로 만듦
A[2] = A[2]-A[1]
show("4단계:R3<- R3 - R2",A)

A[3] = A[3]-2*A[1]
show("5단계:R4<- R4 - 2R2",A)

#피벗 위치를 맞추기 위해 R3과 R4 교환
A[[2,3]] = A[[3,2]]
swap_count +=1
show("6단계:R3<->R4",A)

#상삼각행렬의 대각 원소 곱
diagonal_product = np.prod(np.diag(A))

#행 교환이 일어날 때마다 행렬식의 부호가 바뀜
det_A = ((-1)**swap_count)*diagonal_product

print("\n행 사다리꼴")
print(A)

print("\n대학 원소의 곱", diagonal_product)
print("행 교환 횟수", swap_count)
print("det(A)=",det_A)

#Numpy 계산 결과와 비교
det_check = round(np.linalg.det(original_A))
print("Numpy 검산 결과:",det_check)

