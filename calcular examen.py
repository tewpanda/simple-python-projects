cant_notas = int(input("Introduzca la cantidad de notas del estudiante. "))
sum_notas = 0
pro_notas = 0

i = 0 #Variable para determinar la cantidad de vecez que se repite el bucle

while i < cant_notas:
    nota = float(input("Introduzca una nota. "))
    sum_notas = sum_notas + nota
    
    i +=1

pro_notas = sum_notas / cant_notas

if pro_notas >= 4:
    print("El estudiante ha aprobado.")
elif 4 > pro_notas >= 3.3:
    print("El estudiante debe rendir el examen.")
else:
    print("El estudiante ha reprobado.")
