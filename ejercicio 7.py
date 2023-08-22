class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    # Getters
    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_dni(self):
        return self.__dni

    # Setters
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_edad(self, edad):
        if edad >= 0:
            self.__edad = edad
        else:
            print("La edad no puede ser negativa.")

    def set_dni(self, dni):
        if len(dni) == 9:
            self.__dni = dni
        else:
            print("El DNI debe tener 9 caracteres.")

    def mostrar(self):
        print("Nombre:", self.__nombre)
        print("Edad:", self.__edad)
        print("DNI:", self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18

# Ejemplo de uso
persona1 = Persona()
persona1.set_nombre("Juan")
persona1.set_edad(12)
persona1.set_dni("23626927")

persona1.mostrar()
if persona1.es_mayor_de_edad():
    print("Es mayor de edad.")
else:
    print("No es mayor de edad.")
