filas = input("Ingrese el numero de filas: ")
columnas = input("Ingrese el numero de columnas: ")

total = int(filas) * int(columnas)

arrayNumeros = [];

for i in range(0, total):
    if i == 0:
        num = input("\nIngrese el numero: ")
        arrayNumeros.append(int(num))
    else:
        num = input("\tIngrese el siguiente numero: ")
        arrayNumeros.append(int(num))
    
for i in range(0, int(filas)):
    for j in range(0, int(columnas)):
        print(arrayNumeros[i * int(columnas) + j], end=" ")
    print("\n")
