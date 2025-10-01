a = float(input("Dime el primer numero: "))
b = float(input("Dime el segundo numero: "))
op = input("Que operacion quieres realizar? +, -, *, / : ")
if op == "+":
    print("El resultado de la suma es:", a + b)
elif op == "-":
    print("El resultado de la resta es:", a - b)
elif op == "*":
    print("El resultado de la multiplicacion es:", a * b)
elif op == "/":
    if b != 0:
        print("El resultado al hacer la division es:", a / b)
    else:
        print("Disculpa, no es posible dividir entre 0")
else:
    print("la operación no es valida")