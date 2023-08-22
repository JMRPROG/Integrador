def get_int():
    while True:
        try:
            valor = int(input("Ingrese un valor entero: "))
            return valor
        except ValueError:
            print("Entrada inválida. Intente nuevamente.")

entero = get_int()
print(f"Valor entero ingresado: {entero}")
5