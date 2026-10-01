A = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

diagonal_sum = sum(A[i][i] for i in range(len(A)))

print(diagonal_sum)