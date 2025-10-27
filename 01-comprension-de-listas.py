# MÉTODO TRADICIONAL
pares = []
for numero in range(11):  # range(11) para que incluya el 10
    if numero % 2 == 0:   # El % (módulo) nos da el residuo de una división
        pares.append(numero)

print(f"Tradicional: {pares}")

#MÉTODO MODERNO
# [ lo_que_metes for elemento in iterable if condición ]
pares_moderno = [numero for numero in range(11) if numero % 2 == 0]
print(f"Moderno:  {pares_moderno}")