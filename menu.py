from crud import *
from relaciones import *
from neo4j import GraphDatabase
from tsp_optimization import TSP

# Información de conexión
NEO4J_URI = "neo4j+ssc://33397770.databases.neo4j.io"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "wnHpVYT3KweYDd5zzThQ2sVQO_XKtI7jDVuKvfTsETY"



# Inicializar el driver de Neo4j
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))
def test_connection(driver):
    with driver.session() as session:
        result = session.run("RETURN 'Connection successful' AS message")
        print(result.single()["message"])


test_connection(driver)
def print_menu():
    print("\n--- Menú Principal ---")
    print("1. Gestionar Empresas")
    print("2. Gestionar Productos")
    print("3. Gestionar Documentos")
    print("4. Gestionar Almacenes")
    print("5. Gestionar Tiendas")
    print("6. Gestionar Camiones")
    print("7. Gestionar Relaciones")
    print("8. Calcular ruta óptima")
    print("9. Salir")

def gestionar_empresas():
    while True:
        print("\n--- Gestionar Empresas ---")
        print("1. Crear Empresa")
        print("2. Leer Empresa")
        print("3. Actualizar Empresa")
        print("4. Eliminar Empresa")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de empresa: ")
            nombre = input("Nombre de la empresa: ")
            pais = input("País: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            result = createEmpresa(driver, tipo, nombre, pais, telefono, email)
            print(result)

        elif opcion == "2":
            nombre = input("Nombre de la empresa: ")
            result = readEmpresa(driver, nombre)
            print(result)

        elif opcion == "3":
            tipo = input("Tipo de empresa: ")
            nombre = input("Nombre de la empresa: ")
            pais = input("País: ")
            telefono = input("Teléfono: ")
            email = input("Email: ")
            result = updateEmpresa(driver, tipo, nombre, pais, telefono, email)
            print(result)

        elif opcion == "4":
            nombre = input("Nombre de la empresa: ")
            result = deleteEmpresa(driver, nombre)
            print(result)

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_productos():
    while True:
        print("\n--- Gestionar Productos ---")
        print("1. Crear Producto")
        print("2. Leer Producto")
        print("3. Actualizar Producto")
        print("4. Eliminar Producto")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del producto: ")
            precio = input("Precio: ")
            codigo = input("Código: ")
            tipo = input("Tipo: ")
            marca = input("Marca: ")
            result = createProducto(driver, nombre, precio, codigo, tipo, marca)
            print(result)

        elif opcion == "2":
            nombre = input("Nombre del producto: ")
            result = readProducto(driver, nombre)
            print(result)

        elif opcion == "3":
            nombre = input("Nombre del producto: ")
            precio = input("Precio: ")
            codigo = input("Código: ")
            tipo = input("Tipo: ")
            marca = input("Marca: ")
            result = updateProducto(driver, nombre, precio, codigo, tipo, marca)
            print(result)

        elif opcion == "4":
            nombre = input("Nombre del producto: ")
            result = deleteProducto(driver, nombre)
            print(result)

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_documentos():
    while True:
        print("\n--- Gestionar Documentos ---")
        print("1. Crear Documento")
        print("2. Leer Documento")
        print("3. Actualizar Documento")
        print("4. Eliminar Documento")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            tipoDocumento = input("Tipo de documento: ")
            fechaEmision = input("Fecha de emisión: ")
            numero = input("Número: ")
            estado = input("Estado: ")
            total = input("Total: ")
            result = createDocumento(driver, tipoDocumento, fechaEmision, numero, estado, total)
            print(result)

        elif opcion == "2":
            numero = input("Número del documento: ")
            result = readDocumento(driver, numero)
            print(result)

        elif opcion == "3":
            tipoDocumento = input("Tipo de documento: ")
            fechaEmision = input("Fecha de emisión: ")
            numero = input("Número: ")
            estado = input("Estado: ")
            total = input("Total: ")
            result = updateDocumento(driver, tipoDocumento, fechaEmision, numero, estado, total)
            print(result)

        elif opcion == "4":
            numero = input("Número del documento: ")
            result = deleteDocumento(driver, numero)
            print(result)

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_almacenes():
    while True:
        print("\n--- Gestionar Almacenes ---")
        print("1. Crear Almacén")
        print("2. Leer Almacén")
        print("3. Actualizar Almacén")
        print("4. Eliminar Almacén")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre del almacén: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            ciudad = input("Ciudad: ")
            tipoAlmacen = input("Tipo de almacén: ")
            result = createAlmacen(driver, nombre, direccion, telefono, ciudad, tipoAlmacen)
            print(result)

        elif opcion == "2":
            nombre = input("Nombre del almacén: ")
            result = readAlmacen(driver, nombre)
            #print(result)

        elif opcion == "3":
            nombre = input("Nombre del almacén: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            ciudad = input("Ciudad: ")
            tipoAlmacen = input("Tipo de almacén: ")
            result = updateAlmacen(driver, nombre, direccion, telefono, ciudad, tipoAlmacen)
            print(result)

        elif opcion == "4":
            nombre = input("Nombre del almacén: ")
            result = deleteAlmacen(driver, nombre)
            print(result)

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_tiendas():
    while True:
        print("\n--- Gestionar Tiendas ---")
        print("1. Crear Tienda")
        print("2. Leer Tienda")
        print("3. Actualizar Tienda")
        print("4. Eliminar Tienda")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Nombre de la tienda: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            ciudad = input("Ciudad: ")
            asesor = input("Asesor: ")
            result = createTienda(driver, nombre, direccion, telefono, ciudad, asesor)
            print(result)

        elif opcion == "2":
            nombre = input("Nombre de la tienda: ")
            result = readTienda(driver, nombre)
            print(result)

        elif opcion == "3":
            nombre = input("Nombre de la tienda: ")
            direccion = input("Dirección: ")
            telefono = input("Teléfono: ")
            ciudad = input("Ciudad: ")
            asesor = input("Asesor: ")
            result = updateTienda(driver, nombre, direccion, telefono, ciudad, asesor)
            print(result)

        elif opcion == "4":
            nombre = input("Nombre de la tienda: ")
            result = deleteTienda(driver, nombre)
            print(result)

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_camiones():
    while True:
        print("\n--- Gestionar Camiones ---")
        print("1. Crear Camión")
        print("2. Leer Camión")
        print("3. Actualizar Camión")
        print("4. Eliminar Camión")
        print("5. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            placas = input("Placas: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            capacidad = input("Capacidad: ")
            piloto = input("Piloto: ")
            result = createCamion(driver, placas, marca, modelo, capacidad, piloto)
            print(result)

        elif opcion == "2":
            placas = input("Placas: ")
            result = readCamion(driver, placas)
            print(result)

        elif opcion == "3":
            placas = input("Placas: ")
            marca = input("Marca: ")
            modelo = input("Modelo: ")
            capacidad = input("Capacidad: ")
            piloto = input("Piloto: ")
            result = updateCamion(driver, placas, marca, modelo, capacidad, piloto)
            print(result)

        elif opcion == "4":
            placas = input("Placas: ")
            result = deleteCamion(driver, placas)
            print(result)

        elif opcion == "5":
            break

        else:
            print("Opción no válida. Intente de nuevo.")
"""
def gestionar_relaciones():
    while True:
        print("\n--- Gestionar Relaciones ---")
        print("1. Crear Relación de Despacho")
        print("2. Eliminar Relación de Despacho")
        print("3. Obtener Relación de Despacho por Documento")
        print("4. Obtener Relación de Despacho por Almacén")
        print("5. Obtener Relación de Despacho por Camión")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            almacen = input("Nombre del almacén: ")
            camion = input("Placas del camión: ")
            documento = input("Documento: ")
            codigoConfirmacion = input("Código de confirmación: ")
            fechaEntrega = input("Fecha de entrega: ")
            result = create_despacho_a(driver, almacen, camion, documento, codigoConfirmacion, fechaEntrega)
            print(result)

        elif opcion == "2":
            almacen = input("Nombre del almacén: ")
            camion = input("Placas del camión: ")
            documento = input("Documento: ")
            result = delete_despacho_a(driver, almacen, camion, documento)
            print(result)

        elif opcion == "3":
            documento = input("Documento: ")
            result = get_despacho_a_documento(driver, documento)
            print(result)

        elif opcion == "4":
            almacen = input("Nombre del almacén: ")
            result = get_despacho_a_almacen(driver, almacen)
            print(result)

        elif opcion == "5":
            camion = input("Placas del camión: ")
            result = get_despacho_a_camion(driver, camion)
            print(result)

        elif opcion == "6":
            break

        else:
            print("Opción no válida. Intente de nuevo.")
"""

def gestionar_despachos():
    
    """
    Gestiona las operaciones relacionadas con despachos, como crear, eliminar, obtener y actualizar despachos.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        print("\n--- Gestión de Despachos ---")
        print("1. Crear despacho")
        print("2. Eliminar despacho")
        print("3. Obtener despacho por documento")
        print("4. Obtener despachos por almacén")
        print("5. Obtener despachos por camión")
        print("6. Obtener despachos entre almacén y camión")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear despacho
            almacen = input("Ingrese el nombre del almacén: ")
            camion = input("Ingrese la placa del camión: ")
            documento = input("Ingrese el número de documento: ")
            codigoConfirmacion = input("Ingrese el código de confirmación: ")
            fechaEntrega = input("Ingrese la fecha de entrega (YYYY-MM-DD): ")
            
            mensaje, resultado = create_despacho_a(driver, almacen, camion, documento, codigoConfirmacion, fechaEntrega)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar despacho
            almacen = input("Ingrese el nombre del almacén: ")
            camion = input("Ingrese la placa del camión: ")
            documento = input("Ingrese el número de documento: ")
            
            mensaje, resultado = delete_despacho_a(driver, almacen, camion, documento)
            print(mensaje)
        
        elif opcion == "3":
            # Obtener despacho por documento
            documento = input("Ingrese el número de documento: ")
            
            resultado = get_despacho_a_documento(driver, documento)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "4":
            # Obtener despachos por almacén
            almacen = input("Ingrese el nombre del almacén: ")
            
            resultado = get_despacho_a_almacen(driver, almacen)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Obtener despachos por camión
            camion = input("Ingrese la placa del camión: ")
            
            resultado = get_despacho_a_camion(driver, camion)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "6":
            # Obtener despachos entre almacén y camión
            almacen = input("Ingrese el nombre del almacén: ")
            camion = input("Ingrese la placa del camión: ")
            
            resultado = get_despachos_almacen_camion(driver, almacen, camion)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "7":
            # Salir
            print("Saliendo de la gestión de despachos...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")


def gestionar_completado_por():
    while True:
        print("\n--- Gestionar Completados ---")
        print("1. Crear Completado")
        print("2. Leer Completado por Camion")
        print("3. Leer Completado por Documento")
        print("4. Leer Completado por Camón y Documento")
        print("5. Eliminar Completado")
        print("6. Volver al menú principal")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            documento = input("Documento: ")
            camion = input("Camión: ")
            comision = input("Comision: ")
            ayudante = input("Ayudante: ")
            tiempoDescargaMinutos = input("Tiempo de descarga (minutos): ")
            result = create_completado_por(driver, documento, camion, comision, ayudante, tiempoDescargaMinutos)
            print(result)

        elif opcion == "2":
            documento = input("Camión: ")
            result = get_completado_por_camion(driver, documento)
            print(result)

        elif opcion == "3":
            documento = input("Documento: ")
            fecha = input("Fecha: ")
            result = get_completado_por_documento(driver, documento, fecha)
            print(result)

        elif opcion == "4":
            documento = input("Documento: ")
            camion = input("Camión: ")
            result = get_completado_por_documento_camion(driver, documento, camion)
            print(result)

        elif opcion == "5":
            documento = input("Documento: ")
            camion = input("Camión: ")
            result = delete_completado_por(driver, documento, camion)
            print(result)

        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_distancia_almacen():
    
    """
    Gestiona las operaciones relacionadas con las distancias entre almacenes y tiendas,
    como crear, eliminar, actualizar y obtener distancias.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        
        print("\n--- Gestión de Distancias entre Almacén y Tienda ---")
        print("1. Crear distancia entre almacén y tienda")
        print("2. Eliminar distancia entre almacén y tienda")
        print("3. Actualizar distancia entre almacén y tienda")
        print("4. Obtener distancia entre almacén y tienda")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear distancia entre almacén y tienda
            almacen = input("Ingrese el nombre del almacén: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            distancia = input("Ingrese la distancia (en km): ")
            tiempo_mins = input("Ingrese el tiempo en minutos: ")
            costo = input("Ingrese el costo de transporte: ")
            
            mensaje, resultado = create_distancia(driver, almacen, tienda, distancia, tiempo_mins, costo)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar distancia entre almacén y tienda
            almacen = input("Ingrese el nombre del almacén: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            
            mensaje, resultado = delete_distancia(driver, almacen, tienda)
            print(mensaje)
        
        elif opcion == "3":
            # Actualizar distancia entre almacén y tienda
            almacen = input("Ingrese el nombre del almacén: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            distancia = input("Ingrese la nueva distancia (en km): ")
            tiempo_mins = input("Ingrese el nuevo tiempo en minutos: ")
            costo = input("Ingrese el nuevo costo de transporte: ")
            
            mensaje, resultado = update_distancia(driver, almacen, tienda, distancia, tiempo_mins, costo)
            print(mensaje)
        
        elif opcion == "4":
            # Obtener distancia entre almacén y tienda
            almacen = input("Ingrese el nombre del almacén: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            
            resultado = get_distancia(driver, almacen, tienda)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Salir
            print("Saliendo de la gestión de distancias entre almacén y tienda...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
def gestionar_distancia_tienda():
    """
    Gestiona las operaciones relacionadas con las distancias entre tiendas,
    como crear, eliminar, actualizar y obtener distancias.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        print("\n--- Gestión de Distancias entre Tiendas ---")
        print("1. Crear distancia entre dos tiendas")
        print("2. Eliminar distancia entre dos tiendas")
        print("3. Actualizar distancia entre dos tiendas")
        print("4. Obtener distancias desde una tienda")
        print("5. Obtener distancia entre dos tiendas específicas")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear distancia entre dos tiendas
            tienda1 = input("Ingrese el nombre de la primera tienda: ")
            tienda2 = input("Ingrese el nombre de la segunda tienda: ")
            distancia = input("Ingrese la distancia (en km): ")
            tiempo_mins = input("Ingrese el tiempo en minutos: ")
            costo = input("Ingrese el costo de transporte: ")
            
            mensaje, resultado = create_distancia_tienda(driver, tienda1, tienda2, distancia, tiempo_mins, costo)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar distancia entre dos tiendas
            tienda1 = input("Ingrese el nombre de la primera tienda: ")
            tienda2 = input("Ingrese el nombre de la segunda tienda: ")
            
            mensaje, resultado = delete_distancia_tienda(driver, tienda1, tienda2)
            print(mensaje)
        
        elif opcion == "3":
            # Actualizar distancia entre dos tiendas
            tienda1 = input("Ingrese el nombre de la primera tienda: ")
            tienda2 = input("Ingrese el nombre de la segunda tienda: ")
            distancia = input("Ingrese la nueva distancia (en km): ")
            tiempo_mins = input("Ingrese el nuevo tiempo en minutos: ")
            costo = input("Ingrese el nuevo costo de transporte: ")
            
            mensaje, resultado = update_distancia_tienda(driver, tienda1, tienda2, distancia, tiempo_mins, costo)
            print(mensaje)
        
        elif opcion == "4":
            # Obtener distancias desde una tienda
            tienda1 = input("Ingrese el nombre de la tienda: ")
            
            resultado = get_distancia_tienda_tienda(driver, tienda1)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Obtener distancia entre dos tiendas específicas
            tienda1 = input("Ingrese el nombre de la primera tienda: ")
            tienda2 = input("Ingrese el nombre de la segunda tienda: ")
            
            resultado = get_distancia_tienda_tienda_tienda(driver, tienda1, tienda2)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "6":
            # Salir
            print("Saliendo de la gestión de distancias entre tiendas...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")
def gestionar_distribuido_por():
    """
    Gestiona las operaciones relacionadas con la relación 'distribuido por' entre empresas y productos,
    como crear, eliminar, actualizar y obtener relaciones.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        print("\n--- Gestión de Relaciones 'Distribuido Por' ---")
        print("1. Crear relación 'distribuido por'")
        print("2. Eliminar relación 'distribuido por'")
        print("3. Actualizar relación 'distribuido por'")
        print("4. Obtener relaciones 'distribuido por' por producto")
        print("5. Obtener relaciones 'distribuido por' por empresa")
        print("6. Obtener relación 'distribuido por' entre empresa y producto")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear relación 'distribuido por'
            empresa = input("Ingrese el nombre de la empresa: ")
            producto = input("Ingrese el nombre del producto: ")
            costo = input("Ingrese el costo de distribución: ")
            horasTomaPedidos = input("Ingrese las horas en las que se toman los pedidos: ")
            distribuidoDesde = input("Ingrese la fecha desde la que se distribuye (YYYY-MM-DD): ")
            
            mensaje, resultado = create_distribuido_por(driver, empresa, producto, costo, horasTomaPedidos, distribuidoDesde)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar relación 'distribuido por'
            empresa = input("Ingrese el nombre de la empresa: ")
            producto = input("Ingrese el nombre del producto: ")
            
            mensaje, resultado = delete_distribuido_por(driver, empresa, producto)
            print(mensaje)
        
        elif opcion == "3":
            # Actualizar relación 'distribuido por'
            empresa = input("Ingrese el nombre de la empresa: ")
            producto = input("Ingrese el nombre del producto: ")
            costo = input("Ingrese el nuevo costo de distribución: ")
            horasTomaPedidos = input("Ingrese las nuevas horas en las que se toman los pedidos: ")
            distribuidoDesde = input("Ingrese la nueva fecha desde la que se distribuye (YYYY-MM-DD): ")
            
            mensaje, resultado = update_distribuido_por(driver, empresa, producto, costo, horasTomaPedidos, distribuidoDesde)
            print(mensaje)
        
        elif opcion == "4":
            # Obtener relaciones 'distribuido por' por producto
            producto = input("Ingrese el nombre del producto: ")
            
            resultado = get_distribuido_por_producto(driver, producto)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Obtener relaciones 'distribuido por' por empresa
            empresa = input("Ingrese el nombre de la empresa: ")
            
            resultado = get_distribuido_por_empresa(driver, empresa)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "6":
            # Obtener relación 'distribuido por' entre empresa y producto
            empresa = input("Ingrese el nombre de la empresa: ")
            producto = input("Ingrese el nombre del producto: ")
            
            resultado = get_distribuido_por_empresa_producto(driver, empresa, producto)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "7":
            # Salir
            print("Saliendo de la gestión de relaciones 'distribuido por'...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_distribuye_a():
    """
    Gestiona las operaciones relacionadas con la relación 'distribuye a' entre fabricantes y proveedores,
    como crear, eliminar, actualizar y obtener relaciones.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        print("\n--- Gestión de Relaciones 'Distribuye A' ---")
        print("1. Crear relación 'distribuye a'")
        print("2. Eliminar relación 'distribuye a'")
        print("3. Actualizar relación 'distribuye a'")
        print("4. Obtener relaciones 'distribuye a' por proveedor")
        print("5. Obtener relaciones 'distribuye a' por fabricante")
        print("6. Obtener relación 'distribuye a' entre fabricante y proveedor")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear relación 'distribuye a'
            fabricante = input("Ingrese el nombre del fabricante: ")
            proveedor = input("Ingrese el nombre del proveedor: ")
            fechaInicioContrato = input("Ingrese la fecha de inicio del contrato (YYYY-MM-DD): ")
            fechaFinContrato = input("Ingrese la fecha de fin del contrato (YYYY-MM-DD): ")
            precioContrato = input("Ingrese el precio del contrato: ")
            
            mensaje, resultado = create_distribuye_a(driver, fabricante, proveedor, fechaInicioContrato, fechaFinContrato, precioContrato)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar relación 'distribuye a'
            fabricante = input("Ingrese el nombre del fabricante: ")
            proveedor = input("Ingrese el nombre del proveedor: ")
            
            mensaje, resultado = delete_distribuye_a(driver, fabricante, proveedor)
            print(mensaje)
        
        elif opcion == "3":
            # Actualizar relación 'distribuye a'
            fabricante = input("Ingrese el nombre del fabricante: ")
            proveedor = input("Ingrese el nombre del proveedor: ")
            fechaInicioContrato = input("Ingrese la nueva fecha de inicio del contrato (YYYY-MM-DD): ")
            fechaFinContrato = input("Ingrese la nueva fecha de fin del contrato (YYYY-MM-DD): ")
            precioContrato = input("Ingrese el nuevo precio del contrato: ")
            
            mensaje, resultado = update_distribuye_a(driver, fabricante, proveedor, fechaInicioContrato, fechaFinContrato, precioContrato)
            print(mensaje)
        
        elif opcion == "4":
            # Obtener relaciones 'distribuye a' por proveedor
            proveedor = input("Ingrese el nombre del proveedor: ")
            
            resultado = get_distribuye_a_proveedor(driver, proveedor)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Obtener relaciones 'distribuye a' por fabricante
            fabricante = input("Ingrese el nombre del fabricante: ")
            
            resultado = get_distribuye_a_fabricante(driver, fabricante)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "6":
            # Obtener relación 'distribuye a' entre fabricante y proveedor
            fabricante = input("Ingrese el nombre del fabricante: ")
            proveedor = input("Ingrese el nombre del proveedor: ")
            
            resultado = get_distribuye_a_fabricante_proveedor(driver, fabricante, proveedor)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "7":
            # Salir
            print("Saliendo de la gestión de relaciones 'distribuye a'...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_entregado_en():
    """
    Gestiona las operaciones relacionadas con la relación 'entregado en' entre camiones y tiendas,
    como crear, eliminar, actualizar y obtener relaciones.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        print("\n--- Gestión de Relaciones 'Entregado En' ---")
        print("1. Crear relación 'entregado en'")
        print("2. Eliminar relación 'entregado en'")
        print("3. Obtener relaciones 'entregado en' por camión")
        print("4. Obtener relaciones 'entregado en' por tienda")
        print("5. Obtener relación 'entregado en' entre camión y tienda")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear relación 'entregado en'
            camion = input("Ingrese las placas del camión: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            documento = input("Ingrese el número de documento: ")
            integridadProductos = input("Ingrese la integridad de los productos (True/False): ")
            tiempoDescargaMinutos = input("Ingrese el tiempo de descarga en minutos: ")
            
            mensaje, resultado = create_entregado_en(driver, camion, tienda, documento, integridadProductos, tiempoDescargaMinutos)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar relación 'entregado en'
            camion = input("Ingrese las placas del camión: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            documento = input("Ingrese el número de documento: ")
            
            mensaje, resultado = delete_entregado_en(driver, camion, tienda, documento)
            print(mensaje)
        
        elif opcion == "3":
            # Obtener relaciones 'entregado en' por camión
            camion = input("Ingrese las placas del camión: ")
            
            resultado = get_entregado_en_camion(driver, camion)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "4":
            # Obtener relaciones 'entregado en' por tienda
            tienda = input("Ingrese el nombre de la tienda: ")
            
            resultado = get_entregado_en_tienda(driver, tienda)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Obtener relación 'entregado en' entre camión y tienda
            camion = input("Ingrese las placas del camión: ")
            tienda = input("Ingrese el nombre de la tienda: ")
            
            resultado = get_entregado_en_camion_tienda(driver, camion, tienda)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "6":
            # Salir
            print("Saliendo de la gestión de relaciones 'entregado en'...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_fabricado_por(driver):
    """
    Gestiona las operaciones relacionadas con la relación 'fabricado por' entre fabricantes y productos,
    como crear, eliminar, actualizar y obtener relaciones.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        print("\n--- Gestión de Relaciones 'Fabricado Por' ---")
        print("1. Crear relación 'fabricado por'")
        print("2. Eliminar relación 'fabricado por'")
        print("3. Actualizar relación 'fabricado por'")
        print("4. Obtener relaciones 'fabricado por' por fabricante")
        print("5. Obtener relaciones 'fabricado por' por producto")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear relación 'fabricado por'
            fabricante = input("Ingrese el nombre del fabricante: ")
            producto = input("Ingrese el nombre del producto: ")
            materiales = input("Ingrese los materiales necesarios: ")
            costo = input("Ingrese el costo de fabricación: ")
            fechaInicio = input("Ingrese la fecha de inicio de fabricación (YYYY-MM-DD): ")
            
            mensaje, resultado = create_fabricado_por(driver, fabricante, producto, materiales, costo, fechaInicio)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar relación 'fabricado por'
            fabricante = input("Ingrese el nombre del fabricante: ")
            producto = input("Ingrese el nombre del producto: ")
            
            mensaje, resultado = delete_fabricado_por(driver, fabricante, producto)
            print(mensaje)
        
        elif opcion == "3":
            # Actualizar relación 'fabricado por'
            fabricante = input("Ingrese el nombre del fabricante: ")
            producto = input("Ingrese el nombre del producto: ")
            materiales = input("Ingrese los nuevos materiales necesarios: ")
            costo = input("Ingrese el nuevo costo de fabricación: ")
            fechaInicio = input("Ingrese la nueva fecha de inicio de fabricación (YYYY-MM-DD): ")
            
            mensaje, resultado = update_fabricado_por(driver, fabricante, producto, materiales, costo, fechaInicio)
            print(mensaje)
        
        elif opcion == "4":
            # Obtener relaciones 'fabricado por' por fabricante
            fabricante = input("Ingrese el nombre del fabricante: ")
            
            resultado = get_fabricado_por_fabricante(driver, fabricante)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Obtener relaciones 'fabricado por' por producto
            producto = input("Ingrese el nombre del producto: ")
            
            resultado = get_fabricado_por_producto(driver, producto)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "6":
            # Salir
            print("Saliendo de la gestión")

def gestionar_inventario_almacen():
    """
    Gestiona las operaciones relacionadas con el inventario en los almacenes,
    como crear, eliminar, actualizar y obtener relaciones.
    
    :param driver: driver de la base de datos Neo4j.
    """
    while True:
        print("\n--- Gestión de Inventario en Almacenes ---")
        print("1. Crear relación de inventario en almacén")
        print("2. Eliminar relación de inventario en almacén")
        print("3. Actualizar relación de inventario en almacén")
        print("4. Obtener inventario por almacén")
        print("5. Obtener inventario por producto")
        print("6. Obtener inventario específico en un almacén")
        print("7. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            # Crear relación de inventario en almacén
            almacen = input("Ingrese el nombre del almacén: ")
            producto = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la cantidad de productos: ")
            shelfTimePromedioDias = input("Ingrese el tiempo promedio de permanencia en días: ")
            bloque = input("Ingrese el bloque donde se almacena el producto: ")
            
            mensaje, resultado = create_inventario_almacen(driver, almacen, producto, cantidad, shelfTimePromedioDias, bloque)
            print(mensaje)
        
        elif opcion == "2":
            # Eliminar relación de inventario en almacén
            almacen = input("Ingrese el nombre del almacén: ")
            producto = input("Ingrese el nombre del producto: ")
            
            mensaje, resultado = delete_inventario_almacen(driver, almacen, producto)
            print(mensaje)
        
        elif opcion == "3":
            # Actualizar relación de inventario en almacén
            almacen = input("Ingrese el nombre del almacén: ")
            producto = input("Ingrese el nombre del producto: ")
            cantidad = input("Ingrese la nueva cantidad de productos: ")
            shelfTimePromedioDias = input("Ingrese el nuevo tiempo promedio de permanencia en días: ")
            bloque = input("Ingrese el nuevo bloque donde se almacena el producto: ")
            
            mensaje, resultado = update_inventario_almacen(driver, almacen, producto, cantidad, shelfTimePromedioDias, bloque)
            print(mensaje)
        
        elif opcion == "4":
            # Obtener inventario por almacén
            almacen = input("Ingrese el nombre del almacén: ")
            
            resultado = get_inventario_almacen_almacen(driver, almacen)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "5":
            # Obtener inventario por producto
            producto = input("Ingrese el nombre del producto: ")
            
            resultado = get_inventario_almacen_producto(driver, producto)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "6":
            # Obtener inventario específico en un almacén
            almacen = input("Ingrese el nombre del almacén: ")
            producto = input("Ingrese el nombre del producto: ")
            
            resultado = get_inventario_almacen_almacen_producto(driver, almacen, producto)
            print("Resultado de la consulta:", resultado)
        
        elif opcion == "7":
            # Salir
            print("Saliendo de la gestión de inventario en almacenes...")
            break
        
        else:
            print("Opción no válida. Intente de nuevo.")

def gestionar_inventario_tienda():
    tienda=input("Ingresa el nombre de la tienda: ")
    result=get_inventario_tienda_tienda(driver,tienda)
    print(result)

def gestionar_ordenado_a_almacen():
    almacen=input("Ingresa el nombre del almacen: ")
    result=get_ordenado_a_almacen_almacen(driver,almacen)
    print(result)

def gestionar_ordenado_a_empresa():
    empresa=input("Ingresa el nombre de la empresa: ")
    result=get_ordenado_a_empresa_empresa(driver,empresa)
    print(result)

def gestionar_ordenes():
    orden=input("Ingresa el numero de la orden: ")
    result=get_ordenes_documento(driver,orden)
    print(result)

def gestionar_productos_ordenados():
    producto=input("Ingresa el nombre del producto: ")
    result=get_productos_ordenados_producto(driver,producto)
    print(result)

def gestionar_solicitud():
    solicitud=input("Ingresa el numero de la solicitud: ")
    result=get_solicitud_documento(driver,solicitud)
    print(result)





def gestionar_relaciones():
    while True:
        print("\n--- Gestionar Relaciones ---")

        print("1. Despachos")
        print("2. Distancias Almacenes a Tiendas")
        print("3. Distancia Tienda a Tienda")
        print("4. Completado Por")
        print("5. Distribuido Por")
        print("6. Distribuye A")
        print("7. Entregado En")
        print("8. Fabricado Por")
        print("9. Inventario Almacén")
        print("10. Inventario Tienda")
        print("11. Ordenado A Almacen")
        print("12. Ordenado A Empresa")
        print("13. Ordenes")
        print("14. Productos Ordenados")
        print("15. Solicitud")
        print("16. Volver al menú principal")
        
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_despachos()
        elif opcion == "2":
            gestionar_distancia_almacen()
        elif opcion == "3":
            gestionar_distancia_tienda()
        elif opcion == "4":
            gestionar_completado_por()
        elif opcion == "5":
            gestionar_distribuido_por()
        elif opcion == "6":
            gestionar_distribuye_a()
        elif opcion == "7":
            gestionar_entregado_en()
        elif opcion == "8":
            gestionar_fabricado_por()
        elif opcion == "9":
            gestionar_inventario_almacen()
        elif opcion == "10":
            gestionar_inventario_tienda()
        elif opcion == "11":
            gestionar_ordenado_a_almacen()
        elif opcion == "12":
            gestionar_ordenado_a_empresa()
        elif opcion == "13":
            gestionar_ordenes()
        elif opcion == "14":
            gestionar_productos_ordenados()
        elif opcion == "15":
            gestionar_solicitud()
        elif opcion == "16":
            break
        else:
            print("Opción no válida. Intente de nuevo.")


def main():
    while True:
        print_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            gestionar_empresas()
        elif opcion == "2":
            gestionar_productos()
        elif opcion == "3":
            gestionar_documentos()
        elif opcion == "4":
            gestionar_almacenes()
        elif opcion == "5":
            gestionar_tiendas()
        elif opcion == "6":
            gestionar_camiones()
        elif opcion == "7":
            gestionar_relaciones()
        elif opcion == "8":
            TSP(driver)
        elif opcion == "9":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    main()