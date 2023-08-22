def count_word_frequency(text):
    words = text.split()
    word_freq = {}
    
    for word in words:
        word = word.lower()  # Convertimos la palabra a minúsculas para considerar mayúsculas y minúsculas iguales
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

def most_common_word(word_freq_dict):
    most_common = None
    max_frequency = 0
    
    for word, frequency in word_freq_dict.items():
        if frequency > max_frequency:
            most_common = word
            max_frequency = frequency
    
    return (most_common, max_frequency)

def get_int():
    try:
        user_input = input("Ingrese un valor entero: ")
        int_value = int(user_input)
        return int_value
    except ValueError:
        print("Valor no válido. Intente nuevamente.")
        return get_int()  # Llamada recursiva si el valor no es válido

# Ejemplo de uso
if __name__ == "__main__":
    text = "Esta es una prueba de texto. Una prueba de texto, nada más que una prueba."
    word_freq_dict = count_word_frequency(text)
    print("Diccionario de frecuencias:", word_freq_dict)
    
    most_common, frequency = most_common_word(word_freq_dict)
    print("Palabra más repetida:", most_common)
    print("Frecuencia:", frequency)
    
    int_value = get_int()
    print("Valor entero ingresado:", int_value)
