num = [1, 10, 8, 16, 12, 4, 7, 11, 6, 9]
may = num[0]
for n in num:
    if n > may:
        may = n
print("El numero mayor de la lista", num , "es:", may)