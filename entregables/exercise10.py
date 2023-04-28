size = int(input("Ingrese el tamaño de la lista: "))

lista = []
for i in range(size):
    lista.append(int(input("Ingrese un número: ")))

print("\nLista creada: ", lista)

# Opcion 1
suma = 0
for i in lista:
    suma += i

print("\tSuma de los elementos de la lista Opción A: ", suma)

# Opcion 2
print("\tSuma de los elementos de la lista Opción B: ", sum(lista))