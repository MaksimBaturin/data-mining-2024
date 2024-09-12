def determinant(matrix):
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Матрица должна быть двухуровневым списком")
    
    N = len(matrix)
    if not all(len(row) == N for row in matrix):
        raise ValueError("Матрица должна быть квадратной")
    if N == 0:
        raise ValueError("Матрица не может быть пустой")
    
    if N == 1:
        return matrix[0][0]
    
    if N == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    
    det = 0
    for col in range(N):
        minor = [row[:col] + row[col+1:] for row in matrix[1:]]
        minor_det = determinant(minor)
        det += ((-1) ** col) * matrix[0][col] * minor_det
    
    return det

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
try:
    det = determinant(matrix)
    print(det)
except ValueError as e:
    print("Ошибка:", e)