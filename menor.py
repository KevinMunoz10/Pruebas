def encontrar_numero_mas_pequeñó(lista_numeros):
    minimo = float("inf")  # Valor inicial muy grande

    for numero in lista_numeros:
        if numero < minimo:
            minimo = numero

    return minimo


entrada_usuario = input("Ingresa una lista de números separados por espacios: ")
numeros = [int(numero) for numero in entrada_usuario.split()]

resultado = encontrar_numero_mas_pequeñó(numeros)
print("El número más pequeño es:", resultado)
