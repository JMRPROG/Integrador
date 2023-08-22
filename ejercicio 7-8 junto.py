class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def get_titular(self):
        return self.titular

    def set_cantidad(self, cantidad):
        if cantidad >= 0:
            self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad

    def mostrar(self):
        return f"Titular: {self.titular}\nCantidad: {self.cantidad}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad


class CuentaJoven(Cuenta):
    def __init__(self, titular, cantidad=0.0, bonificacion=0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def set_bonificacion(self, bonificacion):
        self.bonificacion = bonificacion

    def get_bonificacion(self):
        return self.bonificacion

    def es_titular_valido(self):
        return self.titular.get_edad() > 18 and self.titular.get_edad() < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven\nTitular: {self.titular}\nCantidad: {self.cantidad}\nBonificación: {self.bonificacion}%"


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def get_edad(self):
        return self.edad

    def __str__(self):
        return f"{self.nombre}, {self.edad} años"


# Ejemplo de uso
persona1 = Persona("Juan", 45)
cuenta_joven = CuentaJoven(persona1, 1000, 5)

print(cuenta_joven.mostrar())
print("¿Es titular válido?", cuenta_joven.es_titular_valido())

cuenta_joven.ingresar(500)
cuenta_joven.retirar(200)
print(cuenta_joven.mostrar())
