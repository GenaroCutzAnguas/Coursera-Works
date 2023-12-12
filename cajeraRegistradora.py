class Producto:
    def __init__(self, codigo, nombre, precio):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio

class CajaRegistradora:
    def __init__(self):
        self.productos = []
        self.total = 0
        self.descuento = 0

    def agregar_producto(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        if producto:
            subtotal = producto.precio * cantidad
            self.total += subtotal
            print(f"{cantidad} {producto.nombre}(s) agregado(s) al carrito.")
        else:
            print("Producto no encontrado.")

    def buscar_producto(self, codigo):
        for producto in self.productos:
            if producto.codigo == codigo:
                return producto
        return None

    def calcular_total_cambio(self, pago):
        if self.total == 0:
            print("El carrito está vacío.")
        else:
            if pago >= self.total:
                cambio = pago - self.total
                print(f"Total: {self.total}")
                print(f"Cambio: {cambio}")
            else:
                print("El pago no es suficiente.")

    def aplicar_descuento(self, porcentaje):
        self.descuento = self.total * (porcentaje / 100)
        self.total -= self.descuento
        print(f"Descuento aplicado: {self.descuento}")
        print(f"Total con descuento: {self.total}")

    def finalizar_compra(self):
        print(f"Total a pagar: {self.total}")
        print("Gracias por su compra.")

import unittest

class TestCajaRegistradora(unittest.TestCase):
    def setUp(self):
        self.caja = CajaRegistradora()
        self.caja.productos.append(Producto("001", "Producto 1", 10))
        self.caja.productos.append(Producto("002", "Producto 2", 20))

    def test_agregar_producto_existente(self):
        self.caja.agregar_producto("001", 2)
        self.assertEqual(self.caja.total, 20)

    def test_agregar_producto_no_existente(self):
        self.caja.agregar_producto("003", 1)
        self.assertEqual(self.caja.total, 0)

    def test_calcular_total_cambio_suficiente(self):
        self.caja.agregar_producto("001", 2)
        self.caja.calcular_total_cambio(50)
        self.assertEqual(self.caja.total, 20)
        self.assertEqual(self.caja.descuento, 0)

    def test_calcular_total_cambio_insuficiente(self):
        self.caja.agregar_producto("001", 2)
        self.caja.calcular_total_cambio(10)
        self.assertEqual(self.caja.total, 20)
        self.assertEqual(self.caja.descuento, 0)

    def test_aplicar_descuento(self):
        self.caja.agregar_producto("001", 2)
        self.caja.aplicar_descuento(10)
        self.assertEqual(self.caja.total, 18)
        self.assertEqual(self.caja.descuento, 2)

    def test_finalizar_compra(self):
        self.caja.agregar_producto("001", 2)
        self.caja.finalizar_compra()
        self.assertEqual(self.caja.total, 20)

if __name__ == '__main__':
    unittest.main()