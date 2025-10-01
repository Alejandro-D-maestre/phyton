n = int(input("Digite un numero: "))
es_primo = True
for i in range(2, n):
    if n % i == 0:
        es_primo = False
        break
    
if es_primo:
        print(f"{n} es primo")
else:
        print(f"{n} no es primo")