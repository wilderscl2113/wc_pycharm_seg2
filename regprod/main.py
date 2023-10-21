class Producto:
    def __init__(self, id, nombre, descripcion, costo, cantidad, margen_de_venta):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.costo = costo
        self.cantidad = cantidad
        self.margen_de_venta = float(margen_de_venta)
        self.precio_de_venta = self.calcular_precio_de_venta()

    def calcular_precio_de_venta(self):
        if self.costo <= 0 or self.margen_de_venta <= 0:
            return 0
        return self.costo / (1 - self.margen_de_venta)

class Inventario:
    def __init__(self):
        self.productos = {}

    def registrar_producto(self, producto):
        if producto.id not in self.productos:
            self.productos[producto.id] = producto

    def imprimir_listado(self):
        for id, producto in self.productos.items():
            print(f"ID: {producto.id}")
            print(f"Nombre: {producto.nombre}")
            print(f"Descripción: {producto.descripcion}")
            print(f"Costo: ${producto.costo}")
            print(f"Cantidad: {producto.cantidad}")
            print(f"Precio de Venta Unitario: ${producto.precio_de_venta}")
            print(f"Precio de Venta Total: ${producto.precio_de_venta * producto.cantidad }")
            print("---------------")

inventario = Inventario()

while True:
    print("Ingrese los datos de un nuevo producto:")
    id = int(input("ID del producto: "))
    nombre = input("Nombre del producto: ")
    descripcion = input("Descripción del producto: ")
    costo = float(input("Costo del producto: "))
    cantidad = int(input("Cantidad del producto: "))
    margen = float(input("Margen de venta del producto: "))

    producto = Producto(id, nombre, descripcion, costo, cantidad, margen)
    inventario.registrar_producto(producto)

    print("Producto registrado con éxito.")

    continuar = input("¿Desea ingresar otro producto? (Si/No): ").strip().lower()
    if continuar != "si":
        break

inventario.imprimir_listado()
