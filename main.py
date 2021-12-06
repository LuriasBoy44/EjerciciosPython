from FibonacciSerial import Fibonacci

ingreso=input("Ingrese valor numérico para ejecutar a secuencia: ")

if ingreso.isnumeric():
    secuencia= Fibonacci() 
    secuencia.ejecutaSecuencia(int(ingreso))
else:
    print("Por favor ingrese valor numérico")



