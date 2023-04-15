
frase = input("Ingrese una frase: ")
chart = input("Ingrese un caracter: ")

print(f"\nEsta es la frase ingresada: {frase} y este el caracter {chart}")

vocales = ['a', 'e', 'i', 'o', 'u']

array = list(frase)

for i in frase:
    
    if( vocales.__contains__(i) ):
        print(i)
        # array.remove(i)
        frase = frase.replace(i, '', 1)
        
    if(i == chart):
        break
        
        
print(frase)
        
        
# arrayFrase = list(frase)
# print(arrayFrase,"\n")

# for i in vocales:
#     if (frase.__contains__(i)):
#         arrayFrase.remove(i)
        
# prueba = ''.join(map(str, arrayFrase))
# print("\nCadena sin vocales: ", prueba)
