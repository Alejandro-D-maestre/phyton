a = int(input("Digite el primer numero "))
b = int(input("Digite el segundo numero "))
c = int(input("Digite el tercero numero "))
if a > b and  a > c:
    print (f"{a} Es el mayor")
elif b > a and b > c:
    print(f"{b} Es el mayor")
elif c > a and c > b:
    print(f"{c} Es el mayor")
else:
    print("Hay numeros iguales")