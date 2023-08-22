def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    
    # Crear un diccionario para almacenar las palabras y sus conteos
    diccionario = {}
    
    # Contar la frecuencia de cada palabra
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1
        
    return diccionario

def palabra_mas_repetida(diccionario):
    # Encontrar la palabra más repetida y su frecuencia
    palabra_max = None
    frecuencia_max = 0
    
    for palabra, frecuencia in diccionario.items():
        if frecuencia > frecuencia_max:
            palabra_max = palabra
            frecuencia_max = frecuencia
    
    return palabra_max, frecuencia_max

# Ejemplo de uso
cadena_ejemplo = "esta es una prueba es para contar palabras en una cadena es"
diccionario_palabras = contar_palabras(cadena_ejemplo)
palabra_repetida, frecuencia_repetida = palabra_mas_repetida(diccionario_palabras)

print("Diccionario de palabras:", diccionario_palabras)
print("Palabra más repetida:", palabra_repetida)
print("Frecuencia de la palabra más repetida:", frecuencia_repetida)
