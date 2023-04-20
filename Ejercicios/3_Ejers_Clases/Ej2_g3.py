def division():
    while True:
        try:
            n1 = int(input("Ingresa el primer numero:\n>>> "))
            n2 = int(input("Ingresa el segundo numero:\n>>> "))

            print(n1/n2)

        except ZeroDivisionError:
            print("No se puede dividir por cero")
        finally:
            print("Proceso Ejecutado")


division()