def empaquetar_manual(lista):
    resultado_empaquetado = []
    
    valor_actual = lista[0]
    contador = 1
    
    for i in range(1, len(lista)):
        
       
        if lista[i] == valor_actual:
            contador += 1
        else:
            
            resultado_empaquetado.append((valor_actual, contador))
            
            
            valor_actual = lista[i]
            contador = 1
            
    resultado_empaquetado.append((valor_actual, contador))
    return resultado_empaquetado


lista_ejemplo = [1, 1, 1, 3, 5, 1, 1, 3, 3]

empaquetado = empaquetar_manual(lista_ejemplo)

print("Lista Original: ", lista_ejemplo )
print(f"Resultado Obtenido (Manual): ", empaquetado)
