frase = input("Ingrese una frase: ")
print("\tEsta es la frase ingresada: " + frase)

palabra = input("\nIngrese la palabra a eliminar: ")

# Manera 1
print("\tEsta es la frase sin la palabra: " + frase.replace(palabra, ""))

# Manera 2
lista = frase.split()
lista.remove(palabra)

print("\tEsta es la frase sin la palabra: " + " ".join(lista))