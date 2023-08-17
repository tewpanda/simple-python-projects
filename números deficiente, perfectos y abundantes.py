cant_numeros = int(input("Introduzca la cantidad de números enteros positivos que desea comprobar. "))
cant_defi = 0
cant_perf = 0
cant_abun = 0
i = 1

while i <= cant_numeros:
    numero = int(input("Introduzca un numero entero positivo. "))
    sum_numero = 0
    x2num = numero * 2
    k = 1
    while k <= numero:
        if numero % k == 0:
            sum_numero = sum_numero + k
        k += 1
    

    if sum_numero < x2num:
        cant_defi += 1
    elif sum_numero == x2num:
        cant_perf += 1
    elif sum_numero > x2num:
        cant_abun += 1
    i += 1

print("")
print("Abundantes:",cant_abun)
print("Perfectos:",cant_perf)
print("Deficientes:",cant_defi)
    
