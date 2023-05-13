numMatrices = int(input("Numero de matrices a sumar: "))
while numMatrices < 2:
    numMatrices = int(input("El numero minimo es de 2: "))

filas = int(input("\nDigite el numero de filas de las matrices: "))
columnas = int(input("Digite la cantidad de columnas de las matrices: "))

matrices = []
for i in range(numMatrices):
    matriz = []
    
    if i == 0:
        print("\nIngrese los elementos de la primera matriz")
    else:
        print(f"Ingrese los elementos de la matriz {i + 1}")
    
    for j in range(filas):
        fila = []
        for k in range(columnas):
            elemento = int(input(f"Ingrese el elemento en la fila {j + 1} y columna {k + 1}: "))
            fila.append(elemento)
        matriz.append(fila)
    matrices.append(matriz)

suma = [[0] * columnas for _ in range(filas)]
for i in range(numMatrices):
    for j in range(filas):
        for k in range(columnas):
            suma[j][k] += matrices[i][j][k]

print("\nMatrices a sumar:")
for i in range(numMatrices):
    print(f"Matriz {i + 1}:")
    for fila in matrices[i]:
        print(fila)
    if i < numMatrices - 1:
        print("+")
    else:
        print("=")
    
print("Matriz resultante:")
for fila in suma:
    print(fila)
