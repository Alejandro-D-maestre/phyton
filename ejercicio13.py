n = int(input("Digite un número: "))
print(f"Números pares desde 1 hasta {n}:")
for i in range(1, n + 1):
    if i % 2 == 0:  
        print(i)