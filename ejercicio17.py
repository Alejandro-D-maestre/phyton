num = int(input("piensa en un numero: "))
primo = True
if num <= 1:
    primo = False
else:
    for i in range(2, num):
        if num % i == 0:
            primo = False
            break
print(f"El numero:" , num , "si es primo" if primo else "no es primo")
