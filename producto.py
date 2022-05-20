class Producto():
    def __init__(self, nombre: str, precio: int, stock: int = 0):
        self.__nombre = nombre
        self.__precio = precio
        self.__stock = stock

    def validar_stock(self, stock):
        if stock < 0:
            stock = 0
        return

    @property
    def nombre(self):
        return self.__nombre

    @property
    def precio(self):
        return self.__precio

    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, nuevo_stock: int):
        self.__stock = self.validar_stock(nuevo_stock)

    def __eq__(self, other):
        return self.__nombre.lower() == other.nombre.lower()

    def __iadd__(self, other):
        if self == other:
            self.__stock += other.stock
        return self

    def __isub__(self, other):
        if self == other:
            self.__stock -= other.stock
        return self
