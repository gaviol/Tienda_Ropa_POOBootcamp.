# Clase Producto: Representa un producto general
class Producto:
    def __init__(self, nombre, precio, cantidad=0):
        self._nombre = nombre  # Atributo encapsulado
        self._precio = precio  # Atributo encapsulado
        self._cantidad = cantidad  # Atributo encapsulado

    @property
    def nombre(self):
        return self._nombre

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    @cantidad.setter
    def cantidad(self, cantidad):
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._cantidad = cantidad

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio:.2f}, Cantidad disponible: {self.cantidad}"


# Clase Ropa: Hereda de Producto y añade características específicas de la ropa
class Ropa(Producto):
    def __init__(self, nombre, precio, talla, cantidad=0):
        super().__init__(nombre, precio, cantidad)
        self._talla = talla  # Atributo encapsulado

    @property
    def talla(self):
        return self._talla

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Talla: {self.talla}"


# Clases derivadas de Ropa
class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, cantidad=0):
        super().__init__(nombre, precio, talla, cantidad)
        self._tipo_tela = tipo_tela  # Atributo encapsulado

    @property
    def tipo_tela(self):
        return self._tipo_tela

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo de tela: {self.tipo_tela}"


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_pantalon, cantidad=0):
        super().__init__(nombre, precio, talla, cantidad)
        self._tipo_pantalon = tipo_pantalon  # Atributo encapsulado

    @property
    def tipo_pantalon(self):
        return self._tipo_pantalon

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo de pantalón: {self.tipo_pantalon}"


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_zapato, cantidad=0):
        super().__init__(nombre, precio, talla, cantidad)
        self._tipo_zapato = tipo_zapato  # Atributo encapsulado

    @property
    def tipo_zapato(self):
        return self._tipo_zapato

    def mostrar_info(self):
        return f"{super().mostrar_info()}, Tipo de zapato: {self.tipo_zapato}"


# Clase Tienda: Maneja los productos disponibles y las compras
class Tienda:
    def __init__(self):
        self._productos = []  # Atributo encapsulado

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_catalogo(self):
        print("Catálogo de productos:")
        for idx, producto in enumerate(self._productos, start=1):
            print(f"{idx}. {producto.mostrar_info()}")

    def procesar_compra(self, carrito):
        if not carrito._productos:
            print("El carrito está vacío.")
            return
        print("Procesando compra...")
        print(carrito.mostrar_resumen())
        carrito._productos.clear()  # Limpiar el carrito después de la compra


# Clase Carrito: Almacena productos seleccionados
class Carrito:
    def __init__(self):
        self._productos = []  # Atributo encapsulado

    def agregar_producto(self, producto, cantidad):
        if producto.cantidad >= cantidad:  # Verificar si hay suficiente cantidad
            self._productos.append((producto, cantidad))  # Almacenar el producto junto con la cantidad
            producto.cantidad -= cantidad  # Reducir la cantidad disponible del producto
        else:
            print(f"No hay suficiente cantidad de {producto.nombre}. Solo hay {producto.cantidad} disponible.")

    def calcular_total(self):
        return sum(producto.precio * cantidad for producto, cantidad in self._productos)

    def mostrar_resumen(self):
        resumen = []
        for producto, cantidad in self._productos:
            resumen.append(f"{producto.mostrar_info()}, Cantidad: {cantidad}")
        total = self.calcular_total()
        return "\n".join(resumen) + f"\nTotal a pagar: ${total:.2f}"


# Función principal para la interacción con el usuario
def main():
    # Crear productos con cantidades iniciales
    camisa1 = Camisa("Camisa Casual", 25.00, "M", "Algodón", cantidad=10)
    pantalon1 = Pantalon("Pantalón Deportivo", 30.00, "L", "Chino", cantidad=5)
    zapato1 = Zapato("Zapato de Cuero", 50.00, "42", "Formal", cantidad=8)

    # Crear la tienda y agregar productos
    tienda = Tienda()
    tienda.agregar_producto(camisa1)
    tienda.agregar_producto(pantalon1)
    tienda.agregar_producto(zapato1)

    # Crear carrito
    carrito = Carrito()

    while True:
        tienda.mostrar_catalogo()
        seleccion = input("Seleccione el número del producto a agregar al carrito (o 'q' para salir y procesar la compra): ")

        if seleccion.lower() == 'q':
            break

        try:
            indice = int(seleccion) - 1
            if 0 <= indice < len(tienda._productos):
                cantidad = int(input("Ingrese la cantidad a agregar: "))
                if cantidad > 0:
                    producto_seleccionado = tienda._productos[indice]
                    carrito.agregar_producto(producto_seleccionado, cantidad)
                    print(f"{cantidad} unidad(es) de {producto_seleccionado.nombre} ha(n) sido agregado(s) al carrito.\n")
                else:
                    print("La cantidad debe ser mayor a 0.")
            else:
                print("Selección inválida. Por favor, intente de nuevo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")

    # Procesar la compra
    tienda.procesar_compra(carrito)


# Ejecución del programa
if __name__ == "__main__":
    main()
