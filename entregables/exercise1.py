from py2flowchart import pyfile2flowchart

def main():
    name = input("Ingrese su nombre: ")

    print(f"====== Vamos a determinar su tiempo de vacaciones {name} ======")

    departamento = input("Ingrese el departamento al que pertenece: ")
    anios = int(input("Ingrese la cantidad de años que lleva en la empresa: "))

    if (departamento == "Clave 1" or departamento == "clave 1"):
        
        if anios == 1:
            vacaciones = 6
        elif anios >= 2 and anios <= 6:
            vacaciones = 14
        elif anios >= 7:
            vacaciones = 20
        else:
            print("No tiene derecho a vacaciones aun.")
            vacaciones = 0
        
    elif (departamento == "Clave 2" or departamento == "clave 2"):
        
        if anios == 1:
            vacaciones = 7
        elif anios >= 2 and anios <= 6:
            vacaciones = 15
        elif anios >= 7:
            vacaciones = 22
        else:
            print("No tiene derecho a vacaciones aun.")
            vacaciones = 0

    elif (departamento == "Clave 3" or departamento == "clave 3"):
        
        if anios == 1:
            vacaciones = 10
        elif anios >= 2 and anios <= 6:
            vacaciones = 20
        elif anios >= 7:
            vacaciones = 30
        else:
            print("No tiene derecho a vacaciones aun.")
            vacaciones = 0

    else: 
        print("No hay ningun departamento con esa clave.")

    print(f"\n\nHola {name}, según el formulario usted pertenece al departamento con {departamento} y lleva {anios} años en la empresa.")
    if(vacaciones != 0):
        print(f"\tPor lo tanto, usted tiene derecho a {vacaciones} días de vacaciones.");

    print("Gracias por su tiempo.")


if __name__ == "__main__":
    # Ejecutar el programa
    main()

    # Diagrama de flujo
    pyfile2flowchart("./entregables/exercise1.py", "./entregables/exercise1.html")
