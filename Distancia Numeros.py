numeros = input("Ingrese los números separados por espacios: ")
distancia = int(input("Ingrese la distancia: "))

numeros = numeros.split()
for i in range(len(numeros)):
    numeros[i] = int(numeros[i])


contador_pares = 0


for i in range(len(numeros)):
    for j in range(i + 1, len(numeros)):  
        diferencia = numeros[i] - numeros[j]
        if diferencia < 0:
            diferencia = -diferencia
        
        if diferencia == distancia:
            contador_pares += 1

print(contador_pares)
