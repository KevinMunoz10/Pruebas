class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad


mi_Persona = Persona("Kevin", 21)
print("La primera persona creada es: ")
print(mi_Persona.nombre)
print(mi_Persona.edad)

segunda_persona = Persona("Saray", 14)
print("La segunda persona creada es: ")
print(segunda_persona.nombre)
print(segunda_persona.edad)
