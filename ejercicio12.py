import statistics
a = int(input("Digite el primer numero "))
b = int(input("Digite el segundo numero "))
c = int(input("Digite el tercero numero "))
d = int(input("Digite el cuarto numero "))
e = int(input("Digite el quinto numero "))
n = [a, b, c, d, e]
promedio = statistics.mean(n)
print(f"El promedio es:{promedio}")
