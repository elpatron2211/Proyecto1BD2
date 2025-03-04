from crud import *
from relaciones import *
from neo4j import GraphDatabase
from tsp_optimization import TSP

# Información de conexión
NEO4J_URI = "neo4j+s://33397770.databases.neo4j.io"
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
            print(result)

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
def gestionar_relaciones():
    while True:
        print("\n--- Gestionar Relaciones ---")
        print("1. Crear Relación de Despacho")
        print("2. Eliminar Relación de Despacho")
        print("3. Obtener Relación de Despacho por Documento")
        print("4. Obtener Relación de Despacho por Almacén")
        print("5. Obtener Relación de Despacho por Camión")
        print("6. Obtener Relación de Distancia")
        print("7. Obtener Relación de Completado por Documento")
        print("8. Obtener Relación de Completado por Camión")
        print("9. Obtener Relación de Distribuido por Empresa")
        print("10. Obtener Relación de Distribuido por Producto")
        print("11. Obtener Relación de Distribuye a Fabricante")
        print("12. Obtener Relación de Distribuye a Proveedor")
        print("13. Obtener Relación de Entregado en Camión")
        print("14. Obtener Relación de Entregado en Tienda")
        print("15. Obtener Relación de Fabricado por Fabricante")
        print("16. Obtener Relación de Fabricado por Producto")
        print("17. Obtener Relación de Inventario Almacén por Almacén")
        print("18. Obtener Relación de Inventario Almacén por Producto")
        print("19. Obtener Relación de Inventario Tienda por Tienda")
        print("20. Obtener Relación de Inventario Tienda por Producto")
        print("21. Obtener Relación de Ordenado a Almacén por Documento")
        print("22. Obtener Relación de Ordenado a Almacén por Almacén")
        print("23. Obtener Relación de Ordenado a Empresa por Documento")
        print("24. Obtener Relación de Ordenado a Empresa por Empresa")
        print("25. Obtener Relación de Ordenes por Documento")
        print("26. Obtener Relación de Ordenes por Almacén")
        print("27. Obtener Relación de Productos Ordenados por Documento")
        print("28. Obtener Relación de Productos Ordenados por Producto")
        print("29. Obtener Relación de Solicitud por Documento")
        print("30. Obtener Relación de Solicitud por Tienda")
        print("31. Obtener Relación de Distancia Tienda por Tienda")
        print("32. Volver al menú principal")
        
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
            almacen = input("Nombre del almacén: ")
            tienda = input("Nombre de la tienda: ")
            result = get_distancia(driver, almacen, tienda)
            print(result)

        elif opcion == "7":
            documento = input("Documento: ")
            result = get_completado_por_documento(driver, documento)
            print(result)

        elif opcion == "8":
            camion = input("Placas del camión: ")
            result = get_completado_por_camion(driver, camion)
            print(result)

        elif opcion == "9":
            empresa = input("Nombre de la empresa: ")
            result = get_distribuido_por_empresa(driver, empresa)
            print(result)

        elif opcion == "10":
            producto = input("Nombre del producto: ")
            result = get_distribuido_por_producto(driver, producto)
            print(result)

        elif opcion == "11":
            fabricante = input("Nombre del fabricante: ")
            result = get_distribuye_a_fabricante(driver, fabricante)
            print(result)

        elif opcion == "12":
            proveedor = input("Nombre del proveedor: ")
            result = get_distribuye_a_proveedor(driver, proveedor)
            print(result)

        elif opcion == "13":
            camion = input("Placas del camión: ")
            result = get_entregado_en_camion(driver, camion)
            print(result)

        elif opcion == "14":
            tienda = input("Nombre de la tienda: ")
            result = get_entregado_en_tienda(driver, tienda)
            print(result)

        elif opcion == "15":
            fabricante = input("Nombre del fabricante: ")
            result = get_fabricado_por_fabricante(driver, fabricante)
            print(result)

        elif opcion == "16":
            producto = input("Nombre del producto: ")
            result = get_fabricado_por_producto(driver, producto)
            print(result)

        elif opcion == "17":
            almacen = input("Nombre del almacén: ")
            result = get_inventario_almacen_almacen(driver, almacen)
            print(result)

        elif opcion == "18":
            producto = input("Nombre del producto: ")
            result = get_inventario_almacen_producto(driver, producto)
            print(result)

        elif opcion == "19":
            tienda = input("Nombre de la tienda: ")
            result = get_inventario_tienda_tienda(driver, tienda)
            print(result)

        elif opcion == "20":
            producto = input("Nombre del producto: ")
            result = get_inventario_tienda_producto(driver, producto)
            print(result)

        elif opcion == "21":
            documento = input("Documento: ")
            result = get_ordenado_a_almacen_documento(driver, documento)
            print(result)

        elif opcion == "22":
            almacen = input("Nombre del almacén: ")
            result = get_ordenado_a_almacen_almacen(driver, almacen)
            print(result)

        elif opcion == "23":
            documento = input("Documento: ")
            result = get_ordenado_a_empresa_documento(driver, documento)
            print(result)

        elif opcion == "24":
            empresa = input("Nombre de la empresa: ")
            result = get_ordenado_a_empresa_empresa(driver, empresa)
            print(result)

        elif opcion == "25":
            documento = input("Documento: ")
            result = get_ordenes_documento(driver, documento)
            print(result)

        elif opcion == "26":
            almacen = input("Nombre del almacén: ")
            result = get_ordenes_almacen(driver, almacen)
            print(result)

        elif opcion == "27":
            documento = input("Documento: ")
            result = get_productos_ordenados_documento(driver, documento)
            print(result)

        elif opcion == "28":
            producto = input("Nombre del producto: ")
            result = get_productos_ordenados_producto(driver, producto)
            print(result)

        elif opcion == "29":
            documento = input("Documento: ")
            result = get_solicitud_documento(driver, documento)
            print(result)

        elif opcion == "30":
            tienda = input("Nombre de la tienda: ")
            result = get_solicitud_tienda(driver, tienda)
            print(result)

        elif opcion == "31":
            tienda = input("Nombre de la tienda: ")
            result = get_distancia_tienda_tienda(driver, tienda)
            print(result)

        elif opcion == "32":
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