productos = [
    {'nombre': 'Laptop', 'precio': 15000},
    {'nombre': 'Teclado', 'precio': 2000},
    {'nombre': 'Mouse', 'precio': 800},
    {'nombre': 'Monitor', 'precio': 5000}
]

productos_caros_primero = sorted(productos, key = lambda productos : productos['precio'], reverse=True)
print(productos_caros_primero)