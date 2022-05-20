from abc import ABC, abstractmethod
from producto import Producto


class Tienda(ABC):
    def __init__(self, nombre: str, delivery: int):
        self.__nombre = nombre
        self.__delivery = delivery
        self.__productos = []

    @abstractmethod
    def ingresar_producto(self, nombre: str, precio: int, stock: int):
        pass

    @abstractmethod
    def listar_productos(self):
        pass

    @abstractmethod
    def realizar_venta(self, nombre: str, cantidad: int):
        pass

    @property
    def nombre(self):
        return self.__nombre

    @property
    def delivery(self):
        return self.__delivery

    @property
    def productos(self):
        return self.__productos


class Restaurante(Tienda):
    tipo = "Restaurante"

    def ingresar_producto(self, nombre: str, precio: int, stock: int = 0) -> None:
        p = Producto(nombre, precio, 0)
        if p in self.productos:
            pass
        else:
            self.productos.append(p)

    def listar_productos(self):
        for index, item in enumerate(self.productos, 1):
            print(f"{index}. Nombre: {item.nombre.capitalize()} // Precio: ${item.precio}")

    def realizar_venta(self, nombre: str, cantidad: int):
        pass


class Farmacia(Tienda):
    tipo = "Farmacia"

    def ingresar_producto(self, nombre: str, precio: int, stock: int) -> None:
        p = Producto(nombre, precio, stock)
        if p in self.productos:
            indice = self.productos.index(p)
            self.productos[indice] += p
        else:
            self.productos.append(p)

    def listar_productos(self):
        for index, item in enumerate(self.productos, 1):
            if item.precio > 15000:
                print(f"{index}. Nombre: {item.nombre.capitalize()} // Precio: ${item.precio}. 'Envío gratis al "
                      f"solicitar este producto'")
            else:
                print(f"{index}. Nombre: {item.nombre.capitalize()} // Precio: ${item.precio}")

    def realizar_venta(self, nombre: str, cantidad: int):
        if cantidad <= 3:
            venta = Producto(nombre, 5000, cantidad)
            if venta in self.productos:
                indice = self.productos.index(venta)
                if cantidad > self.productos[indice].stock:
                    self.productos[indice].stock = 0
                else:
                    self.productos[indice] -= venta
            else:
                pass
        else:
            pass


class Supermercado(Tienda):
    tipo = "Supermercado"

    def ingresar_producto(self, nombre: str, precio: int, stock: int) -> None:
        p = Producto(nombre, precio, stock)
        if p in self.productos:
            indice = self.productos.index(p)
            self.productos[indice] += p
        else:
            self.productos.append(p)

    def listar_productos(self):
        for index, item in enumerate(self.productos, 1):
            if item.stock < 10:
                print(f"{index}. Nombre: {item.nombre.capitalize()} // Precio: ${item.precio} // Stock: {item.stock}. "
                      f"'Pocos productos disponibles'")
            else:
                print(f"{index}. Nombre: {item.nombre.capitalize()} // Precio: ${item.precio} // Stock: {item.stock}")

    def realizar_venta(self, nombre: str, cantidad: int):
        venta = Producto(nombre, 5000, cantidad)
        if venta in self.productos:
            indice = self.productos.index(venta)
            if cantidad > self.productos[indice].stock:
                self.productos[indice].stock = 0
            else:
                self.productos[indice] -= venta
        else:
            pass
