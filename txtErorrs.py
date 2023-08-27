# Pregunta 6:
# Manejo de Errores
# Escribe una función que lea un archivo de texto y maneje posibles errores de lectura del archivo.

try:
    archive = open("ConsultasBD.txt", "r")
    print(archive.read())
    print("Este fue el archivo encontrado: " + str(archive))
except FileNotFoundError:
    print("El archivo no existe")
except IOError as e:
    print("Error de lectura del archivo", e)
except Exception as e:
    print("Error Inesperado", e)
