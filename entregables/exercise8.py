# tabla de multiplicar 

num = int(input("Ingrese un numero: "))
print(f"\nEsta es la tabla de multiplicar del {num}")

for i in range (11):
    print("\n", num, " * ", i, " = ", num*i)
    