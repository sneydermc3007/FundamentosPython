
frase = input("Ingrese una frase: ")
chart = input("Ingrese un caracter: ")

print(f"\nEsta es la frase ingresada: {frase} y este el caracter {chart}")

vocales = ['a', 'e', 'i', 'o', 'u']

arrayFrase = list(frase)
print(arrayFrase,"\n")

for i in vocales:
    if (frase.__contains__(i)):
        arrayFrase.remove(i)
        
    if(frase.__contains__(chart)):
        break

prueba = ''.join(map(str, arrayFrase))
print("\nCadena sin vocales: ", prueba)
