print("Este es el ejercicio de practica #3")

n1 =  int(input("\nIngrese el primer numero: "))
n2 =  int(input("Ingrese el segundo numero: "))
n3 =  int(input("Ingrese el ultimo numero: "))

print(f"\nLos numeros ingresados fueron: {n1}, {n2} & {n3}" )

if n1 > n2 :
    if n1 > n3:
        print(f"\nEl numero mayor entre los ingresados fue el: {n1}")
    else:
        print(f"\nEl numero mayor entre los ingresados fue el: {n3}")
else:
    if n2 > n3:
        print(f"\nEl numero mayor entre los ingresados fue el: {n2}")
    else:
        print(f"\nEl numero mayor entre los ingresados fue el: {n3}")

print("\tFin.")
