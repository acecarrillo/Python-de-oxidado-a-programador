import sys
import utilidades


try:
    print(f"Calculadora basica \n ejecutando: {sys.argv[1], sys.argv[2], sys.argv[3]}")
    calculos = utilidades.Calculadora()
    num1 = int(sys.argv[1])
    num2 = int(sys.argv[3])
    if sys.argv[2] == "+":
        print(f"Resultado: {calculos.sumar(num1, num2)}")
    elif sys.argv[2] == "-":
        print(f"Resultado: {calculos.restar(num1, num2)}")
    elif sys.argv[2] == "x":
        print(f"Resultado: {calculos.multiplicar(num1, num2)}")
    elif sys.argv[2] == "/":
        print(f"Resultado: {calculos.dividir(num1, num2)}")
        
        
except IndexError:
    print("Debe de usarse 3 valores")
except TypeError:
    print("Valores 1 y 3 deben de ser numericos")