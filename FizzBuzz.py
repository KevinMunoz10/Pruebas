# Pregunta 1:
# Fundamentos de Programación escribe un programa que imprima los números del 1 al 100.
# Pero para los múltiplos de 3, en lugar de imprimir el número, imprime "Fizz".
# Para los múltiplos de 5, imprime "Buzz".
# Y para los números que son múltiplos tanto de 3 como de 5, imprime "FizzBuzz".

for numeros in range(1, 101):
    print(numeros)

i = int(input("Digite un numero: "))

if i % 5 == i % 3 == 0:
    print("FizzBuzz")
elif i % 5 == 0:
    print("Buzz")
elif i % 3 == 0:
    print("Fizz")
else:
    print("Ni Fizz Ni Buzz " + " El numero ingresado fue: " + str(i))
