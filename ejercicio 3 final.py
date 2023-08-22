def contar_palabras(cadena):
    
    palabras = cadena.split()
    
    
    frecuencia_palabras = {}
    
    
    for palabra in palabras:
        if palabra in frecuencia_palabras:
            frecuencia_palabras[palabra] += 1
        else:
            frecuencia_palabras[palabra] = 1
    
    return frecuencia_palabras


cadena_input = input("Ingrese una cadena de caracteres: ")


diccionario_frecuencias = contar_palabras(cadena_input)


for palabra, frecuencia in diccionario_frecuencias.items():
    print(f'Palabra: {palabra}, Frecuencia: {frecuencia}')
