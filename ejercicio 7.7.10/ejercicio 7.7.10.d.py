def a_triangular_superior(M):
    
    M_mod = [row[:] for row in M] 
    filas, cols = len(M_mod), len(M_mod[0])
    
    
    TOLERANCIA = 1e-9 

    for k in range(min(filas, cols)): 
        
        
        max_val, fila_max = 0, k
        for i in range(k, filas):
            if abs(M_mod[i][k]) > max_val:
                max_val = abs(M_mod[i][k])
                fila_max = i
        
        
        if fila_max != k:
            M_mod[k], M_mod[fila_max] = M_mod[fila_max], M_mod[k]
        
        pivote = M_mod[k][k]

        
        if abs(pivote) < TOLERANCIA:
            continue 

        
        for i in range(k + 1, filas):
            
            factor = M_mod[i][k] / pivote
            
            
            for j in range(k, cols):
                M_mod[i][j] -= factor * M_mod[k][j]

    return M_mod

