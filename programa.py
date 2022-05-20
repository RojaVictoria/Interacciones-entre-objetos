from tienda import Restaurante, Farmacia, Supermercado

opcion_tienda = int(input("\nIngrese el tipo de tienda que desea administrar: \n"
                          "1. Restaurante\n"
                          "2. Farmacia\n"
                          "3. Supermercado\n"
                          "> "))

if opcion_tienda == 4:
    print("Hasta pronto")
    exit()
elif opcion_tienda == 1:
    nombre = input("\nIngrese el nombre de la tienda: \n")
    delivery = int(input("\nIngrese el costo de delivery: \n"))
    tienda_uno = Restaurante(nombre, delivery)

elif opcion_tienda == 2:
    nombre = input("\nIngrese el nombre de la tienda: \n")
    delivery = int(input("\nIngrese el costo de delivery: \n"))
    tienda_uno = Farmacia(nombre, delivery)

elif opcion_tienda == 3:
    nombre = input("\nIngrese el nombre de la tienda: \n")
    delivery = int(input("\nIngrese el costo de delivery: \n"))
    tienda_uno = Supermercado(nombre, delivery)

opcion_producto = int(input("\n¿Quiere ingresar un producto? \n"
                            "1. Sí\n"
                            "2. No\n"
                            "> "))

while opcion_producto == 1:
    nombre = input("\nIngrese nombre del producto: \n")
    precio = int(input("\nIngrese precio del producto: \n"))
    stock = int(input("\nIngrese stock del producto:\n"))
    tienda_uno.ingresar_producto(nombre, precio, stock)

    opcion_producto = int(input("\n¿Quiere ingresar otro producto? \n"
                                "1. Sí\n"
                                "2. No\n"
                                "> "))
    if opcion_producto == 2:
        print("Ha finalizado el ingreso de productos")
        break

operacion = 0
while operacion == 0:

    opcion_operacion = int(input("\nIndique la operación que desea realizar: \n"
                                 "1. Listar los productos\n"
                                 "2. Realizar venta\n"
                                 "3. Salir del programa\n"
                                 "> "))

    if opcion_operacion == 1:
        print( f"\n***** DATOS DE INGRESO *****\n{tienda_uno.tipo} {tienda_uno.nombre}\nLista de productos:")
        tienda_uno.listar_productos()

        pregunta_volver = int(input("¿Desea volver al Menú? 1. Si 2. No (Salir) \n > "))
        if pregunta_volver == 1:
            operacion = 0
        else:
            print("Hasta pronto")
            exit()

    elif opcion_operacion == 2:
        while opcion_operacion == 2:
            nombre = input("\nIngrese nombre del producto: \n")
            cantidad = int(input("\nIngrese la cantidad a vender: \n"))
            tienda_uno.realizar_venta(nombre, cantidad)

            opcion_operacion = int(input("¿Quiere finalizar la venta? 1. Si 2. No \n > "))
            if opcion_producto == 1:
                print("Ha finalizado la operación")
                break
    else:
        print("Hasta pronto")
        exit()
