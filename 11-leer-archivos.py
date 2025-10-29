try:
    with open("leccion.txt","r") as archivo: 
        contenido_completo = archivo.read()
        print("Contenido del archivo:\n")
        print(contenido_completo)
except FileNotFoundError:
    print("Archivo no encontrado")