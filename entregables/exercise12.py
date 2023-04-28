listaNumeros = [1, 2, 3, 4, 5]

print("Lista de números: ", listaNumeros)

listaEliminados = []

listaEliminados.append(listaNumeros.pop(0))
listaEliminados.append(listaNumeros[-1])
listaNumeros.remove(listaNumeros[-1])

print("Lista de numeros restanes: ", listaNumeros)
print("Lista de numeros eliminados: ", listaEliminados)
