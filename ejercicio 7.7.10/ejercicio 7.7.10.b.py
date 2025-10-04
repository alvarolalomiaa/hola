def multiplicar_matrices(A, B):
    filas_A, column_A = len(A), len(A[0])
    filas_B, column_B = len(B), len(B[0])

    if column_A != filas_B:
        return "Error, las columnas de A deben coincidir con filas de B"

    F=[[0] * column_B for _ in range(filas_A)] 
    
    for i in range(filas_A):
        for j in range(column_B):
           
            suma_producto = 0
            for k in range(column_A):
                suma_producto += A[i][k] * B[k][j]
            F[i][j] = suma_producto
            
    return F

matriz1= (
    [1, 0, 3],
    [9, 2, 4],
    [7, 5, 2],
    )

matriz2= (
    [3, 2, 1],
    [6, 9, 5], 
    [4, 10, 7],
    )

print(multiplicar_matrices(matriz1, matriz2))