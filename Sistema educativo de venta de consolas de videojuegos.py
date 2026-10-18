"""Sistema educativo de venta de consolas de videojuegos usando POO."""

class Consola:
    """Representa una consola disponible en el inventario."""

    def __init__(self, nombre, marca, precio, stock):
        """Inicializa los atributos de una consola y valida sus valores."""
        if precio <= 0 or stock < 0:
            raise ValueError("El precio debe ser positivo y el stock no negativo")
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        """Devuelve una descripción del producto."""
        return f"{self.nombre} ({self.marca}) - ${self.precio:,.2f} MXN | Disponibles: {self.stock}"

    def vender(self, cantidad):
        """Descuenta unidades del inventario si hay existencias."""
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor que cero")
        if cantidad > self.stock:
            return False
        self.stock -= cantidad
        return True


class TiendaConsolas:
    """Administra el catálogo y registra el importe acumulado de ventas."""

    def __init__(self, nombre):
        """Crea una tienda con catálogo vacío y ventas en cero."""
        self.nombre = nombre
        self.catalogo = []
        self.total_ventas = 0.0

    def agregar_consola(self, consola):
        """Agrega un objeto Consola al catálogo."""
        self.catalogo.append(consola)

    def mostrar_catalogo(self):
        """Muestra las consolas numeradas y sus existencias."""
        print(f"\n=== {self.nombre}: catálogo ===")
        for indice, consola in enumerate(self.catalogo, start=1):
            print(f"{indice}. {consola.mostrar_info()}")

    def realizar_venta(self, indice, cantidad):
        """Procesa la venta de una consola y muestra el ticket."""
        if indice < 1 or indice > len(self.catalogo):
            print("Producto no válido.")
            return False
        consola = self.catalogo[indice - 1]
        if not consola.vender(cantidad):
            print("No hay existencias suficientes.")
            return False
        subtotal = consola.precio * cantidad
        self.total_ventas += subtotal
        print(f"Venta exitosa: {cantidad} x {consola.nombre} = ${subtotal:,.2f} MXN")
        return True


def main():
    """Instancia objetos y permite probar sus métodos mediante un menú."""
    tienda = TiendaConsolas("GameZone")
    tienda.agregar_consola(Consola("PlayStation 5", "Sony", 11999, 5))
    tienda.agregar_consola(Consola("Xbox Series X", "Microsoft", 10999, 4))
    tienda.agregar_consola(Consola("Nintendo Switch", "Nintendo", 6499, 7))

    # Bucle principal de la aplicación: se repite hasta elegir salir.
    while True:
        print("\n1. Ver catálogo  2. Comprar consola  3. Ver ventas  4. Salir")
        opcion = input("Selecciona una opción: ").strip()
        if opcion == "1":
            tienda.mostrar_catalogo()
        elif opcion == "2":
            tienda.mostrar_catalogo()
            try:
                indice = int(input("Número de consola: "))
                cantidad = int(input("Cantidad: "))
                tienda.realizar_venta(indice, cantidad)
            except ValueError:
                print("Ingresa números enteros válidos.")
        elif opcion == "3":
            print(f"Ventas acumuladas: ${tienda.total_ventas:,.2f} MXN")
        elif opcion == "4":
            print("Gracias por visitar GameZone.")
            break
        else:
            print("Opción no válida.")


if __name__ == "__main__":
    main()
    