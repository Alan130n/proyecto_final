import clientes as c
import menu
import pedidos as p
import db

def mostrar_menu():
    print("\n--- Menu Principal ---")
    print("A. Pedidos")
    print("B. Clientes")
    print("C. Menú")
    print("D. Salir")

def seleccionar_opcion():
    while True:
        mostrar_menu()
        opcion = input("selecciona una opcion: ")
        if opcion == 'A':
            gestionar_pedidos()
        elif opcion == 'B':
            gestionar_clientes()
        elif opcion == 'C':
            gestionar_menu()
        elif opcion == 'D':
            print("Saliendo del programa.")
            break
        else:
            print("opción no válida, intente de nuevo")

def gestionar_pedidos():
    pedido_m = p.Pedido()
    cliente_m = c.Cliente()
    menu_m = menu.Menu()
    while True:
        print("\n--- Administación de pedidos ---")
        print("1. Crear pedido")
        print("2. Cancelar pedido")
        print("3. Ver pedidos actuales")
        print("4. Generar recibo")
        print("5. Volver al menú principal")
        opcion = input("seleciona una opción:")
        if opcion == '1':
            try:
                pedido_id = int(input("ID del pedido: "))
                cliente = input("Nombre del cliente: ").strip()
                if not cliente_m.existe_cliente(cliente):
                    raise ValueError("El cliente no existe.")
                producto = input("Nombre del producto: ").strip()
                if not menu_m.existe_producto(producto):
                    raise ValueError("El producto no existe.")
                precio = float(input("Precio:"))
                if not cliente or not producto:
                    raise ValueError("Cliente y producto no pueden estar vacíos.")
                pedido_m.crear_pedido(pedido_id, cliente, producto, precio)
            except ValueError as e:
                print(f"Error: {e}")
        elif opcion == '2':
            try:
                pedido_id = int(input("ID del pedido:"))
                pedido_m.cancelar_pedido(pedido_id)
            except ValueError:
                print("Id de pedido inválido")
        elif opcion == '3':
            pedidos = pedido_m.obtener_pedidos()
            if pedidos:
                for pedido in pedidos:
                    print(pedido)
            else:
                print(pedido)
        elif opcion == '4':
            try:
                pedido_id = int(input("ID del pedido"))
                pedido = pedido_m.obtener_pedido_por_id(pedido_id)
                if pedido:
                    pedido_m.generar_ticket(pedido_id, pedido[1], pedido[2], pedido[3])
                else:
                    print("Pedido no encontrado.")
            except ValueError:
                print("ID de pedido inválido.")
        elif opcion == '5':
            break
        else:
            print("Opción no válida, intenta de nuevo.")

def gestionar_clientes():
    cliente_m = c.Cliente()
    while True:
             print("\n--- Administración de clientes ---")
             print("1. Agregar cliente")
             print("2. Eliminar cliente")
             print("3. Actualizar cliente")
             print("4. Ver lista clientes")
             print("5. Volver al menú principal")
             opcion = input("seleciona una opción:")
             if opcion == '1':
                 clave = input("Clave del cliente:").strip()
                 nombre = input("Nombre: ").strip()
                 direccion = input(" Direccción:").strip()
                 correo = input("Correo Electronico: ").strip()
                 telefono = input("Telefono: ").strip()
                 if clave and nombre and direccion and correo and telefono:
                     cliente_m.agregar_cliente(clave,nombre,direccion,correo,telefono)
                 else:
                     print ("Todos los campos son obligatorios")
             elif opcion == '2':
                 clave = input("Clave del cliente: ").strip()
                 if clave:
                    cliente_m.eliminar_cliente(clave)
                 else: 
                     print("Clave del cliente no puede estar vacía.")
             elif opcion == '3':     
                 clave = input("Clave del cliente: ").strip()
                 if clave:
                     nombre = input("Nuevo Nombre(deja en blanco para no cambiar):").strip()    
                     direccion = input("Nueva direeción (deja en blanco para no cambiar):").strip()
                     correo = input("Nuevo Correo Electrónico(dejaen blanco para no cambiar):").strip()
                     telefono = input("Nuevo Teléfono(deja en blanco para no cambiar):").strip()
                     cliente_m.actualizar_cliente(clave, nombre, direccion, correo, telefono)
                 else:
                     print("Clave del cliente no puede estar vacia.")
             elif opcion == '4':   
                 clientes = cliente_m.obtener_clientes()
                 if clientes:
                    for cliente in clientes: 
                     print(cliente)
                 else:
                    print("No hay clientes")
             elif opcion == '5':
                 break
             else:
                 print ("Opción no válida, intenta de nuevo")           

def gestionar_menu():
    menu_m = menu.Menu() 
    while True:
                print("\n--- Gestion del Menú ---")
                print("1. Agregar producto")
                print("2. Eliminar producto")
                print("3. Actualizar producto")
                print("4. Ver productos del menú principal")
                print("5. Volver al menú principal")
                opcion = input("seleciona una opción:")
                if opcion == '1':
                    clave = input("Clave del producto: ").strip()
                    nombre = input("Nombre: ").strip()    
                    try:
                        precio = float(input("Precio: "))
                        if clave and nombre:
                            menu_m.agregar_producto(clave,nombre,precio)
                        else:
                            print("La clave y nombre son obligatorios.")
                    except ValueError:
                        print("Precio inválido.")
                elif opcion == '2':
                    clave = input("Clave del producto: ").strip()
                    if clave:
                        menu_m.eliminar_producto(clave)
                    else:
                        print("Clave del producto no puede ser vacía.")
                elif opcion == '3':
                    clave = input("Clave del producto:").strip()
                    if clave:
                        nombre = input("Nuevo nombre (deja en blanco para no cambiar):").strip()
                        precio = input("Nuevo precio (deja en blanco para no cambiar):").strip()
                        precio = float(precio) if precio else None
                        menu_m.actualizar_producto(clave,nombre,precio)
                    else:
                        print("Clave del producto no puede estar vacía.")
                elif opcion == '4':
                    productos = menu_m.obtener_productos()
                    if productos:
                        for producto in productos:
                            print(producto)
                    else:
                        print("No hay productos.")  
                elif opcion == '5':
                    break                          
                else:
                    print("Opcion no válida, intenta de nuevo.")

db.crear_tablas()
seleccionar_opcion()


                       