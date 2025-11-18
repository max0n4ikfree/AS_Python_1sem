if __name__ == "__main__":
    pass
def SwapCol(A, K1, K2):
    """
    Меняет местами столбцы K1 и K2 в матрице A
    A - матрица M×N (список списков)
    K1, K2 - номера столбцов (индексы с 0)
    """
    for i in range(len(A)):
        A[i][K1], A[i][K2] = A[i][K2], A[i][K1]


matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("До:")
for row in matrix:
    print(row)

SwapCol(matrix, 1, 3)  

print("\nПосле:")
for row in matrix:
    print(row)
