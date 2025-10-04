#c)
def a_triangular_superior(M):
    M_mod = [row[:] for row in M] 
    filas, cols = len(M_mod), len(M_mod[0])

    for k in range(min(filas, cols)): 
        pivote = M_mod[k][k]
        
        
        if pivote == 0:
            continue 

        
        for i in range(k + 1, filas):
            factor = M_mod[i][k] / pivote
            
            
            for j in range(k, cols):
                M_mod[i][j] -= factor * M_mod[k][j]

    return M_mod
