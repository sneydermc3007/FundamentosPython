lista = ["A", "B", "b", "c", "E", "E", "f"]

letterDelete = input("Ingrese la letra que desea eliminar: ")

for i in lista[:]:
    print(i)
    if i == letterDelete.lower() or i == letterDelete.upper():
        print("Elemento: ", i)
        lista.remove(i)

print("\n Lista limpia: ", lista)