
cadena = input("Introduce una cadena: ")

# Solución 1
for i in cadena[::-1]:
    print(i, end="")

# Solución 2
print("\n", cadena[::-1])

# Solución 3
for i in range(len(cadena)-1, -1, -1):
    print(cadena[i], end="")

