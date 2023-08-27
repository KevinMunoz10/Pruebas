# Fibonacci en este caso se define fibonacci y se le el valor de n
# Se usa una funcion if la cual dira que si n es igual a 0 o n es igual a 1 returnara n
# Si esto no se cumple returnara a fibonacci tomara el valor de n y le restara 1 y a este valor le sumara fibonacci de n - 2
# Pediremos al usuario que digite un numero para la serie
# Para pedirlo por consola se usara el input, la variable n almacenara un dato de tipo int que digitara el usuario
# El print nos mostrara por consola el texto que necesitemos
# Usaremos la funcion for con el fin de mostrar la serie
# N in un rango de 0, n esto quiere decir que n estara en un rango de 0 a n, n en este caso sera el valor dado por el usuario
# Finalmente haremos un print de fibonacci mostrando hasta n


def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n = int(input("digita un numero"))
print("La serie es")

for n in range(0, n):
    print(fibonacci(n))
