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
    pass


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
    pass

def gestionar_distancia_tienda():
    pass

def gestionar_distribuido_por():
    pass

def gestionar_distribuye_a():
    pass

def gestionar_entregado_en():
    pass

def gestionar_fabricado_por():
    pass

def gestionar_inventario_almacen():
    pass

def gestionar_inventario_tienda():
    pass

def gestionar_ordenado_a_almacen():
    pass

def gestionar_ordenado_a_empresa():
    pass

def gestionar_ordenes():
    pass

def gestionar_productos_ordenados():
    pass

def gestionar_solicitud():
    pass





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