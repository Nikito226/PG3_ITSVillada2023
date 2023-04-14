while True:
    try:
        num1=int(input("Cual es el primer numero :"))
        num2=int(input("cual es el segundo numero :"))
        print ("La suma es :" + str (num1+num2))
    except ValueError:
        print ("El valor ingresado no es un numero")
    finally:
        print("Realize otra operacion")
        
            