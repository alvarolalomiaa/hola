#a)
def sumar_matrices(A, B):
    
    if len(A) != len(B) or len(A[0]) != len(B[0]):
       return "Error, deben de ser dos matrices de la misma dimensión"

    filas, columnas = len(A), len(A[0])
    C = []
    for i in range(filas):
        fila_actual = []
        for j in range(columnas):
            fila_actual.append(0)
        C.append(fila_actual)

    
    for i in range(filas):
        for j in range(columnas):
            C[i][j] = A[i][j] + B[i][j]
            
    return C

matriz1= (
    [0, 2, 3],
    [5, 6, 9],
    [4, 8, 1],
    )

matriz2= (
    [0, 0, 2],
    [5, 9, 6], 
    [4, 10, 8],
    )

print(sumar_matrices(matriz1, matriz2))
