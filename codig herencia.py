
# Clase base: contiene los atributos y métodos comunes.
class Consola:
    def __init__(self, nombre, marca, precio, stock):
        self.nombre = nombre
        self.marca = marca
        self.precio = precio
        self.stock = stock

    def mostrar_info(self):
        return (f"{self.nombre} ({self.marca}) - "
                f"${self.precio:,.2f} MXN | "
                f"Disponibles: {self.stock}")

    def vender(self, cantidad):
        if cantidad <= 0 or cantidad > self.stock:
            print("Cantidad no válida o stock insuficiente.")
            return False

        self.stock -= cantidad
        print(f"Venta realizada: {cantidad} x {self.nombre}")
        return True


# Subclase que hereda de Consola.
class PlayStation(Consola):
    def __init__(self, nombre, precio, stock):
        # super() llama al constructor de la clase base.
        super().__init__(nombre, "Sony", precio, stock)

    # Método exclusivo de PlayStation.
    def juegos_exclusivos(self):
        print("PlayStation cuenta con juegos exclusivos.")


# Subclase Xbox.
class Xbox(Consola):
    def __init__(self, nombre, precio, stock):
        super().__init__(nombre, "Microsoft", precio, stock)

    # Método exclusivo de Xbox.
    def mostrar_gamepass(self):
        print("Xbox ofrece el servicio Game Pass.")


# Subclase Nintendo.
class Nintendo(Consola):
    def __init__(self, nombre, precio, stock):
        super().__init__(nombre, "Nintendo", precio, stock)

    # Sobrescritura de un método heredado.
    def mostrar_info(self):
        return super().mostrar_info() + " | Modo portátil"

    # Método exclusivo de Nintendo.
    def modo_portatil(self):
        print("Nintendo Switch permite jugar en modo portátil.")


# Programa principal: instanciación de las subclases.
def main():
    ps5 = PlayStation("PlayStation 5", 11999, 5)
    xbox = Xbox("Xbox Series X", 10999, 4)
    switch = Nintendo("Nintendo Switch", 6499, 7)

    # Prueba de los métodos heredados.
    print(ps5.mostrar_info())
    print(xbox.mostrar_info())
    print(switch.mostrar_info())

    # Prueba de los métodos exclusivos.
    ps5.juegos_exclusivos()
    xbox.mostrar_gamepass()
    switch.modo_portatil()

    # Prueba de venta y actualización del inventario.
    switch.vender(2)
    print(switch.mostrar_info())


if __name__ == "__main__":
    main()
