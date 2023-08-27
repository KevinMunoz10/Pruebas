def encontrar_numero_mas_grande(lista_numeros):
    maximo = float("-inf")  # Valor inicial muy pequeño

    for numero in lista_numeros:
        if numero > maximo:
            maximo = numero

    return maximo


entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
numeros = [int(numero) for numero in entrada_usuario.split()]

resultado = encontrar_numero_mas_grande(numeros)
print("El número más grande es:", resultado)
