def formatear_nombres(lista_de_personas):
    """
    Recibe una lista de tuplas (Apellido, Nombre, Inicial_segundo_nombre)
    y devuelve una lista con el formato "Nombre Inicial. Apellido".
    """
    nombres_formateados = []

    for persona in lista_de_personas:

        
        apellido = persona[0]
        nombre = persona[1]
        inicial = persona[2]
        
        cadena_formateada = f"{nombre} {inicial}. {apellido}"
        
       
        nombres_formateados.append(cadena_formateada)

    return nombres_formateados

ejemplo_entrada = [
    ("García", "Ana", "M"),
    ("Pérez", "Juan", "C"),
    ("López", "Marta", "R")
]

resultado = formatear_nombres(ejemplo_entrada)

print(resultado)