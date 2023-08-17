print("Ingrese un numero entero positivo y le diré si es múltiplo de 15, 5 o 3.")
numero=int(input("Ingrese un numero. "))

if numero % 15 == 0:
    print("El número es múltiplo de 15")
elif numero % 5 == 0:
    print("El número es múltiplo de 5")
elif numero % 3 == 0:
    print("El número es múltiplo de 3")
else:
    print("El número no es múltiplo de ninguno de los números analizados.")
