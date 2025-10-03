def generar_multiplos_de_2(limite):
    multiplos = []
    for num in range(limite + 1):
        if num % 2 == 0:
            multiplos.append(num)
    return multiplos

# Generar múltiplos de 2 hasta el número 20
print(generar_multiplos_de_2(20))
# Salida: [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
