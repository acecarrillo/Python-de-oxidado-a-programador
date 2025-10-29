import sys
import utilidades

def main():
    """
    Función principal de nuestra calculadora.
    La ponemos dentro de una función para mantener el código limpio.
    """
    
    # 1. El "Guardia" (checa len() primero)
    #    Necesitamos 4: [script.py, num1, op, num2]
    if len(sys.argv) != 4:
        print("Error: Uso incorrecto.")
        print("Ejemplo: python 20-main-y-calculadora.py 10 + 5")
        sys.exit(1) # Cierra el script con un código de error

    # 2. Asignamos los argumentos a variables claras
    script_name = sys.argv[0]
    val1 = sys.argv[1]
    op = sys.argv[2]
    val2 = sys.argv[3]

    # 3. El bloque TRY...EXCEPT robusto
    try:
        # Convertimos a int() DENTRO del try
        num1 = int(val1)
        num2 = int(val2)
        
        calc = utilidades.Calculadora()
        
        if op == "+":
            resultado = calc.sumar(num1, num2)
        elif op == "-":
            resultado = calc.restar(num1, num2)
        elif op == "x":
            resultado = calc.multiplicar(num1, num2)
        elif op == "/":
            resultado = calc.dividir(num1, num2)
        else:
            print(f"Error: Operador '{op}' no reconocido.")
            sys.exit(1)
            
        print(f"Resultado: {resultado}")

    # 4. Múltiples 'excepts' para cada error posible
    except ValueError:
        print(f"Error: '{val1}' o '{val2}' no son números válidos.")
    except ZeroDivisionError:
        print("Error: ¡No se puede dividir entre cero!")
    except Exception as e:
        # Un 'except' genérico para cualquier otro
        print(f"Ocurrió un error inesperado: {e}")

# --- LA MAGIA ---
# Esto le dice a Python: "Si ejecuté este archivo directamente..."
if __name__ == "__main__":
    main() # "...entonces, corre la función principal."