def contar_palabras(cadena):
    # Dividir la cadena en palabras
    palabras = cadena.split()
    # Inicializar un diccionario para almacenar las frecuencias
    frecuencias = {}
    
    # Contar las frecuencias de las palabras
    for palabra in palabras:
        # Eliminar signos de puntuación alrededor de la palabra
        palabra = palabra.strip(".,!?\"'()[]{}")
        # Convertir la palabra a minúsculas para un conteo sin distinción entre mayúsculas y minúsculas
        palabra = palabra.lower()
        if palabra:
            if palabra in frecuencias:
                frecuencias[palabra] += 1
            else:
                frecuencias[palabra] = 1
    
    return frecuencias

def palabra_mas_repetida(diccionario):
    if not diccionario:
        return None, 0
    
    palabra_max = max(diccionario, key=diccionario.get)
    frecuencia_max = diccionario[palabra_max]
    
    return palabra_max, frecuencia_max

# Ejemplo de uso
cadena_ejemplo = "Esta es una prueba. Prueba de frecuencia de palabras. ¿Cuál es la palabra más repetida?"
frecuencias = contar_palabras(cadena_ejemplo)
palabra_max_repetida, frecuencia_max_repetida = palabra_mas_repetida(frecuencias)

print("Frecuencias de palabras:", frecuencias)
print("Palabra más repetida:", palabra_max_repetida)
print("Frecuencia de la palabra más repetida:", frecuencia_max_repetida)
