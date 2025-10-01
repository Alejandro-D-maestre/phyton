p = input("Escribe cualquier palabra: ").lower()
vocal = "aeiou"
cont = 0
for letra in p:
    if letra in vocal:
        cont += 1
print("la cantidad de vocales en la palabra", p , "es de:", cont)