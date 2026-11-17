import numpy as np
#선형시스템 A X = b
#2x1 + x2 = 3
#2x1 + x2 = 1
#2X1 - 2x2 = -1


A = np.array([
    [2, 1],
    [2,-1],
    [1,-2]
],dtype=float)

b = np.array([3,1,-1],dtype = float)

# 방정식 3개 미지수 2개 최소제곱법 사용

solution, residuals, rank, singular_values = np.linalg.lstsq(
    A, b, rcond=None
)

x1, x2 = solution

print(f"x1 = {x1:6f}")
print(f"x2 = {x2:6f}")

#모든 방정식을 정확히 만족하는지 확인

print("A @ solution =",A @ solution)
print("b =",b)

if np.allclose(A @ solution, b):
    print("공통해가 존재합니다.")
    print(f"공통해: ({x1:0f}, {x2:0f})")
else:
    print("세 방정식을 동시에 만족하는 정확한 공통해가 없습니다.")