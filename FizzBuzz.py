n = int(input("Ingrese cualquier numero positivo: "))

a = []
for i in range(1,n+1):
    if i % 15 == 0:
        a.append("FizzBuzz")
    elif i % 3 == 0:
        a.append("Fizz")
    elif i % 5 == 0:
        a.append("Buzz")
    else:
        a.append(str(i))
print(a)