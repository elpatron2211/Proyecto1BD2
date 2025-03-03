from neo4j import GraphDatabase

# despachos

def create_despacho_a(driver, almacen, camion, documento, codigoConfirmacion, fechaEntrega):
    """
    Crea una relacion de despacho entre un almacen y un camion

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param camion: placa del camion.
    :param documento: documento del despacho.
    :param codigoConfirmacion: codigo de confirmacion del despacho.
    :param fechaEntrega: fecha de entrega del despacho.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})
        MATCH (c:Camión {Placas: $camion})
        CREATE (a)-[r:DESPACHO_A]->(c)
        SET r.documento = $documento
        SET r.codigoConfirmacion = $codigoConfirmacion
        SET r.fechaEntrega = $fechaEntrega


        """,
        almacen=almacen,
        camion=camion,
        documento=documento,   
        codigoConfirmacion=codigoConfirmacion,
        fechaEntrega=fechaEntrega,
        database = 'neo4j'

    )

    return f'Relacion despacho creada entre {almacen} y {camion}: ({documento}, {codigoConfirmacion}, {fechaEntrega})', result

def delete_despacho_a(driver, almacen, camion, documento):
    """
    Elimina una relacion de despacho entre un almacen y un camion, para un documento especifico

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param camion: placa del camion.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:DESPACHO_A {documento: $documento}]->(c:Camión {Placas: $camion})
        DELETE r

        """,
        almacen=almacen,
        camion=camion,
        documento=documento,
        database = 'neo4j'

    )

    return f'Relacion despacho eliminada entre {almacen} y {camion}', result

def get_despacho_a_documento(driver, documento):
    """
    Obtiene las relaciones de despacho en base al documento que se esta cumpliendo

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén)-[r:DESPACHO_A {documento: $documento}]->(c:Camión)
        RETURN a, r, c

        """,
        documento=documento,
        database = 'neo4j'

    )

    return result


def get_despacho_a_almacen(driver, almacen):
    """
    Obtiene todas las relaciones de despacho para un almacen 

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:DESPACHO_A]->(c:Camión)
        RETURN r, c

        """,
        almacen=almacen,
        database = 'neo4j'

    )

    return result

def get_despacho_a_camion(driver, camion):
    """
    Obtiene todas las relaciones de respacho para un camion

    :param driver: driver de la base de datos Neo4j.
    :param camion: placa del camion.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén)-[r:DESPACHO_A]->(c:Camión {Placas: $camion})
        RETURN r, a

        """,
        camion=camion,
        database = 'neo4j'

    )

    return result

def get_despachos_almacen_camion(driver, almacen, camion):
    """
    Obtiene todas las relaciones de despacho entre un almacen y un camion

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param camion: placa del camion.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:DESPACHO_A]->(c:Camión {Placas: $camion})
        RETURN r

        """,
        almacen=almacen,
        camion=camion,
        database = 'neo4j'

    )

    return result

# Distancias

def create_distancia(driver, almacen, tienda, distancia, tiempo_mins, costo):
    """
    Crea una relacion de distancia entre un almacen y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param tienda: nombre de la tienda.
    :param distancia: distancia entre el almacen y la tienda.
    :param tiempo_mins: tiempo en minutos que se tarda en llegar de un lugar a otro.
    :param costo: costo de transporte entre el almacen y la tienda.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})
        MATCH (t:Tienda {Nombre: $tienda})
        CREATE (a)-[r:DISTANCIA]->(t)
        SET r.distancia = $distancia
        SET r.tiempo_mins = $tiempo_mins
        SET r.costo = $costo

        """,
        almacen=almacen,
        tienda=tienda,
        distancia=distancia,
        tiempo_mins=tiempo_mins,
        costo=costo,
        database = 'neo4j'

    )

    return f'Relacion distancia creada entre {almacen} y {tienda}: ({distancia}, {tiempo_mins}, {costo})', result

def delete_distancia(driver, almacen, tienda):
    """
    Elimina una relacion de distancia entre un almacen y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param tienda: nombre de la tienda.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:DISTANCIA]->(t:Tienda {Nombre: $tienda})
        DELETE r

        """,
        almacen=almacen,
        tienda=tienda,
        database = 'neo4j'

    )

    return f'Relacion distancia eliminada entre {almacen} y {tienda}', result

def update_distancia(driver, almacen, tienda, distancia, tiempo_mins, costo):
    """
    
    Actualiza una relacion de distancia entre un almacen y una tienda
    
    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param tienda: nombre de la tienda.
    :param distancia: distancia entre el almacen y la tienda.
    :param tiempo_mins: tiempo en minutos que se tarda en llegar de un lugar a otro.
    :param costo: costo de transporte entre el almacen y la tienda.
    :return: mensaje de exito y resultado de la consulta.

    """

    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:DISTANCIA]->(t:Tienda {Nombre: $tienda})
        SET r.distancia = $distancia
        SET r.tiempo_mins = $tiempo_mins
        SET r.costo = $costo

        """,
        almacen=almacen,
        tienda=tienda,
        distancia=distancia,
        tiempo_mins=tiempo_mins,
        costo=costo,
        database = 'neo4j'

    )

    return f'Relacion distancia actualizada entre {almacen} y {tienda}: ({distancia}, {tiempo_mins}, {costo})', result

def get_distancia(driver, almacen, tienda):
    """
    Obtiene la relacion de distancia entre un almacen y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param tienda: nombre de la tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:DISTANCIA]->(t:Tienda {Nombre: $tienda})
        RETURN r

        """,
        almacen=almacen,
        tienda=tienda,
        database = 'neo4j'

    )

    return result

# completado por

def create_completado_por(driver, documento, camion, comision, ayudante, tiempoDescargaMinutos):
    """
    Crea una relacion de completado por entre un documento y un camion

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param camion: placa del camion.
    :param comision: comision del camion.
    :param ayudante: nombre del ayudante del camion.
    :param tiempoDescargaMinutos: tiempo en minutos que se tarda en descargar la mercancia.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})
        MATCH (c:Camión {Placas: $camion})
        CREATE (d)-[r:COMPLETADO_POR]->(c)
        SET r.comision = $comision
        SET r.ayudante = $ayudante
        SET r.tiempoDescargaMinutos = $tiempoDescargaMinutos

        """,
        documento=documento,
        camion=camion,
        comision=comision,
        ayudante=ayudante,
        tiempoDescargaMinutos=tiempoDescargaMinutos,
        database = 'neo4j'

    )

    return f'Relacion completado por creada entre {documento} y {camion}: ({comision}, {ayudante}, {tiempoDescargaMinutos})', result

def delete_completado_por(driver, documento, camion):
    """
    Elimina una relacion de completado por entre un documento y un camion

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param camion: placa del camion.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:COMPLETADO_POR]->(c:Camión {placa: $camion})
        DELETE r

        """,
        documento=documento,
        camion=camion,
        database = 'neo4j'

    )

    return f'Relacion completado por eliminada entre {documento} y {camion}', result

def get_completado_por_documento(driver, documento):
    """
    Obtiene la relacion de completado por en base al documento que se esta cumpliendo

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:COMPLETADO_POR]->(c:Camión)
        RETURN r, c

        """,
        documento=documento,
        database = 'neo4j'

    )

    return result

def get_completado_por_camion(driver, camion):
    """
    Obtiene la relacion de completado por en base a la placa del camion

    :param driver: driver de la base de datos Neo4j.
    :param camion: placa del camion.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento)-[r:COMPLETADO_POR]->(c:Camión {Placas: $camion})
        RETURN r, d

        """,
        camion=camion,
        database = 'neo4j'

    )

    return result

def get_completado_por_documento_camion(driver, documento, camion):
    """
    Obtiene la relacion de completado por entre un documento y un camion

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param camion: placa del camion.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:COMPLETADO_POR]->(c:Camión {Placas: $camion})
        RETURN r

        """,
        documento=documento,
        camion=camion,
        database = 'neo4j'

    )

    return result

# distribuido por

def create_distribuido_por(driver, empresa, producto, costo, horasTomaPedidos, distribuidoDesde):
    """
    Crea una relacion de distribuido por entre una empresa y un producto

    :param driver: driver de la base de datos Neo4j.
    :param empresa: nombre de la empresa.
    :param producto: nombre del producto.
    :param costo: costo de distribucion del producto.
    :param horasTomaPedidos: horas en las que se toman los pedidos.
    :param distribuidoDesde: fecha en la que se comenzo a distribuir el producto.

    :return: mensaje de exito y resultado de la consulta.

    """
    result = driver.execute_query(

        """
        MATCH (e:Empresa {Nombre: $empresa})
        MATCH (p:Producto {Nombre: $producto})
        CREATE (e)-[r:DISTRIBUIDO_POR]->(p)
        SET r.costo = $costo
        SET r.horasTomaPedidos = $horasTomaPedidos
        SET r.distribuidoDesde = $distribuidoDesde

        """,
        empresa=empresa,
        producto=producto,
        costo=costo,
        horasTomaPedidos=horasTomaPedidos,
        distribuidoDesde=distribuidoDesde,
        database = 'neo4j'

    )

    return f'Relacion distribuido por creada entre {empresa} y {producto}: ({costo}, {horasTomaPedidos}, {distribuidoDesde})', result

def delete_distribuido_por(driver, empresa, producto):
    """
    Elimina una relacion de distribuido por entre una empresa y un producto

    :param driver: driver de la base de datos Neo4j.
    :param empresa: nombre de la empresa.
    :param producto: nombre del producto.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (e:Empresa {Nombre: $empresa})-[r:DISTRIBUIDO_POR]->(p:Producto {Nombre: $producto})
        DELETE r

        """,
        empresa=empresa,
        producto=producto,
        database = 'neo4j'

    )

    return f'Relacion distribuido por eliminada entre {empresa} y {producto}', result

def update_distribuido_por(driver, empresa, producto, costo, horasTomaPedidos, distribuidoDesde):
    """
    Actualiza una relacion de distribuido por entre una empresa y un producto

    :param driver: driver de la base de datos Neo4j.
    :param empresa: nombre de la empresa.
    :param producto: nombre del producto.
    :param costo: costo de distribucion del producto.
    :param horasTomaPedidos: horas en las que se toman los pedidos
    :param distribuidoDesde: fecha en la que se comenzo a distribuir el producto.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (e:Empresa {Nombre: $empresa})-[r:DISTRIBUIDO_POR]->(p:Producto {Nombre: $producto})
        SET r.costo = $costo
        SET r.horasTomaPedidos = $horasTomaPedidos
        SET r.distribuidoDesde = $distribuidoDesde

        """,
        empresa=empresa,
        producto=producto,
        costo=costo,
        horasTomaPedidos=horasTomaPedidos,
        distribuidoDesde=distribuidoDesde,
        database = 'neo4j'

    )

    return f'Relacion distribuido por actualizada entre {empresa} y {producto}: ({costo}, {horasTomaPedidos}, {distribuidoDesde})', result


def get_distribuido_por_empresa(driver, empresa):
    """
    Obtiene la relacion de distribuido por en base al nombre de la empresa

    :param driver: driver de la base de datos Neo4j.
    :param empresa: nombre de la empresa.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (e:Empresa {Nombre: $empresa})-[r:DISTRIBUIDO_POR]->(p:Producto)
        RETURN r, p

        """,
        empresa=empresa,
        database = 'neo4j'

    )

    return result

def get_distribuido_por_producto(driver, producto):
    """
    Obtiene la relacion de distribuido por en base al nombre del producto

    :param driver: driver de la base de datos Neo4j.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (e:Empresa)-[r:DISTRIBUIDO_POR]->(p:Producto {Nombre: $producto})
        RETURN r, e

        """,
        producto=producto,
        database = 'neo4j'

    )

    return result

def get_distribuido_por_empresa_producto(driver, empresa, producto):
    """
    Obtiene la relacion de distribuido por entre una empresa y un producto

    :param driver: driver de la base de datos Neo4j.
    :param empresa: nombre de la empresa.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (e:Empresa {Nombre: $empresa})-[r:DISTRIBUIDO_POR]->(p:Producto {Nombre: $producto})
        RETURN r

        """,
        empresa=empresa,
        producto=producto,
        database = 'neo4j'

    )

    return result


# distribuye a

def create_distribuye_a(driver,fabricante, proveedor, fechaInicioContrato, fechaFinContrato, precioContrato):
    """
    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :param proveedor: nombre del proveedor.
    :param fechaInicioContrato: fecha de inicio del contrato.
    :param fechaFinContrato: fecha de fin del contrato.
    :param precioContrato: precio del contrato.
    :return: mensaje de exito y resultado de la consulta.

    """

    driver.execute_query(
        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})
        MATCH (p:Empresa {Tipo: 'Proveedor', Nombre: $proveedor})
        CREATE (f)-[r:DISTRIBUYE_A]->(p)
        SET r.fechaInicioContrato = $fechaInicioContrato
        SET r.fechaFinContrato = $fechaFinContrato
        SET r.precioContrato = $precioContrato

        """,
        fabricante=fabricante,
        proveedor=proveedor,
        fechaInicioContrato=fechaInicioContrato,
        fechaFinContrato=fechaFinContrato,
        precioContrato=precioContrato,
        database = 'neo4j'

    )

def delete_distribuye_a(driver, fabricante, proveedor):
    """
    Elimina una relacion de distribuye a entre un fabricante y un proveedor

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :param proveedor: nombre del proveedor.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})-[r:DISTRIBUYE_A]->(p:Empresa {Tipo: 'Proveedor', Nombre: $proveedor})
        DELETE r

        """,
        fabricante=fabricante,
        proveedor=proveedor,
        database = 'neo4j'

    )

    return f'Relacion distribuye a eliminada entre {fabricante} y {proveedor}', result

def update_distribuye_a(driver, fabricante, proveedor, fechaInicioContrato, fechaFinContrato, precioContrato):
    """
    Actualiza una relacion de distribuye a entre un fabricante y un proveedor

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :param proveedor: nombre del proveedor.
    :param fechaInicioContrato: fecha de inicio del contrato.
    :param fechaFinContrato: fecha de fin del contrato.
    :param precioContrato: precio del contrato.
    :return: mensaje de exito y resultado de la consulta.
    
    """

    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})-[r:DISTRIBUYE_A]->(p:Empresa {Tipo: 'Proveedor', Nombre: $proveedor})
        SET r.fechaInicioContrato = $fechaInicioContrato
        SET r.fechaFinContrato = $fechaFinContrato
        SET r.precioContrato = $precioContrato

        """,
        fabricante=fabricante,
        proveedor=proveedor,
        fechaInicioContrato=fechaInicioContrato,
        fechaFinContrato=fechaFinContrato,
        precioContrato=precioContrato,
        database = 'neo4j'

    )

    return f'Relacion distribuye a actualizada entre {fabricante} y {proveedor}: ({fechaInicioContrato}, {fechaFinContrato}, {precioContrato})', result

def get_distribuye_a_fabricante(driver, fabricante):
    """
    Obtiene la relacion de distribuye a en base al nombre del fabricante

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})-[r:DISTRIBUYE_A]->(p:Empresa {Tipo: 'Proveedor'})
        RETURN r, p

        """,
        fabricante=fabricante,
        database = 'neo4j'

    )

    return result

def get_distribuye_a_proveedor(driver, proveedor):
    """
    Obtiene la relacion de distribuye a en base al nombre del proveedor

    :param driver: driver de la base de datos Neo4j.
    :param proveedor: nombre del proveedor.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante'})-[r:DISTRIBUYE_A]->(p:Empresa {Tipo: 'Proveedor', Nombre: $proveedor})
        RETURN r, f

        """,
        proveedor=proveedor,
        database = 'neo4j'

    )

    return result

def get_distribuye_a_fabricante_proveedor(driver, fabricante, proveedor):
    """
    Obtiene la relacion de distribuye a entre un fabricante y un proveedor

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :param proveedor: nombre del proveedor.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})-[r:DISTRIBUYE_A]->(p:Empresa {Tipo: 'Proveedor', Nombre: $proveedor})
        RETURN r

        """,
        fabricante=fabricante,
        proveedor=proveedor,
        database = 'neo4j'

    )

    return result


# entregado_en


def create_entregado_en(driver, camion, tienda, documento, integridadProductos, tiempoDescargaMinutos):
    """
    Crea una relacion de entregado en entre un camion y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param camion: placa del camion.
    :param tienda: nombre de la tienda.
    :param documento: documento del despacho.
    :param integridadProductos: integridad de los productos al ser entregados.
    :param tiempoDescargaMinutos: tiempo en minutos que se tarda en descargar la mercancia.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (c:Camión {Placas: $camion})
        MATCH (t:Tienda {Nombre: $tienda})
        CREATE (c)-[r:ENTREGADO_EN]->(t)
        SET r.documento = $documento
        SET r.integridadProductos = $integridadProductos
        SET r.tiempoDescargaMinutos = $tiempoDescargaMinutos

        """,
        camion=camion,
        tienda=tienda,
        documento=documento,
        integridadProductos=integridadProductos,
        tiempoDescargaMinutos=tiempoDescargaMinutos,
        database = 'neo4j'

    )

    return f'Relacion entregado en creada entre {camion} y {tienda}: ({documento}, {integridadProductos}, {tiempoDescargaMinutos})', result

def delete_entregado_en(driver, camion, tienda, documento):

    """
    Elimina una relacion de entregado en entre un camion y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param camion: placa del camion.
    :param tienda: nombre de la tienda.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (c:Camión {Placas: $camion})-[r:ENTREGADO_EN {documento: $documento}]->(t:Tienda {Nombre: $tienda})
        DELETE r

        """,
        camion=camion,
        tienda=tienda,
        documento=documento,
        database = 'neo4j'

    )

    return f'Relacion entregado en eliminada entre {camion} y {tienda}', result

def get_entregado_en_camion(driver, camion):
    """
    Obtiene la relacion de entregado en en base a la placa del camion

    :param driver: driver de la base de datos Neo4j.
    :param camion: placa del camion.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (c:Camión {Placas: $camion})-[r:ENTREGADO_EN]->(t:Tienda)
        RETURN r, t

        """,
        camion=camion,
        database = 'neo4j'

    )

    return result

def get_entregado_en_tienda(driver, tienda):
    """
    Obtiene la relacion de entregado en en base al nombre de la tienda

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (c:Camión)-[r:ENTREGADO_EN]->(t:Tienda {Nombre: $tienda})
        RETURN r, c

        """,
        tienda=tienda,
        database = 'neo4j'

    )

    return result

def get_entregado_en_camion_tienda(driver, camion, tienda):
    """
    Obtiene la relacion de entregado en entre un camion y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param camion: placa del camion.
    :param tienda: nombre de la tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (c:Camión {Placas: $camion})-[r:ENTREGADO_EN]->(t:Tienda {Nombre: $tienda})
        RETURN r

        """,
        camion=camion,
        tienda=tienda,
        database = 'neo4j'

    )

    return result

# fabricado_por

def create_fabricado_por(driver, fabricante, producto, materiales, costo, fechaInicio):

    """
    Crea una relacion de fabricado por entre un fabricante y un producto

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :param producto: nombre del producto.
    :param materiales: materiales necesarios para fabricar el producto.
    :param costo: costo de fabricacion del producto.
    :param fechaInicio: fecha de inicio de la fabricacion del producto.

    :return: mensaje de exito y resultado de la consulta.
    
    """
    
    driver.execute_query(
        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})
        MATCH (p:Producto {Nombre: $producto})
        CREATE (f)-[r:FABRICADO_POR]->(p)
        SET r.materiales = $materiales
        SET r.costo = $costo
        SET r.fechaInicio = $fechaInicio

        """,
        fabricante=fabricante,
        producto=producto,
        materiales=materiales,
        costo=costo,
        fechaInicio=fechaInicio,
        database = 'neo4j'

    )
    return f'Relacion fabricado por creada entre {fabricante} y {producto}: ({materiales}, {costo}, {fechaInicio})', result

def delete_fabricado_por(driver, fabricante, producto):
    """
    Elimina una relacion de fabricado por entre un fabricante y un producto

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :param producto: nombre del producto.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})-[r:FABRICADO_POR]->(p:Producto {Nombre: $producto})
        DELETE r

        """,
        fabricante=fabricante,
        producto=producto,
        database = 'neo4j'

    )

    return f'Relacion fabricado por eliminada entre {fabricante} y {producto}', result

def update_fabricado_por(driver, fabricante, producto, materiales, costo, fechaInicio):
    """
    Actualiza una relacion de fabricado por entre un fabricante y un producto

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :param producto: nombre del producto.
    :param materiales: materiales necesarios para fabricar el producto.
    :param costo: costo de fabricacion del producto.
    :param fechaInicio: fecha de inicio de la fabricacion del producto.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})-[r:FABRICADO_POR]->(p:Producto {Nombre: $producto})
        SET r.materiales = $materiales
        SET r.costo = $costo
        SET r.fechaInicio = $fechaInicio

        """,
        fabricante=fabricante,
        producto=producto,
        materiales=materiales,
        costo=costo,
        fechaInicio=fechaInicio,
        database = 'neo4j'

    )

    return f'Relacion fabricado por actualizada entre {fabricante} y {producto}: ({materiales}, {costo}, {fechaInicio})', result

def get_fabricado_por_fabricante(driver, fabricante):
    """
    Obtiene la relacion de fabricado por en base al nombre del fabricante

    :param driver: driver de la base de datos Neo4j.
    :param fabricante: nombre del fabricante.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante', Nombre: $fabricante})-[r:FABRICADO_POR]->(p:Producto)
        RETURN r, p

        """,
        fabricante=fabricante,
        database = 'neo4j'

    )

    return result

def get_fabricado_por_producto(driver, producto):
    """
    Obtiene la relacion de fabricado por en base al nombre del producto

    :param driver: driver de la base de datos Neo4j.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (f:Empresa {Tipo: 'Fabricante'})-[r:FABRICADO_POR]->(p:Producto {Nombre: $producto})
        RETURN r, f

        """,
        producto=producto,
        database = 'neo4j'

    )

    return result

# inventario_almacen

def create_inventario_almacen(driver, almacen, producto, cantidad,shelfTimePromedioDias,bloque):
    """
    Crea una relacion de inventario almacen entre un almacen y un producto

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param producto: nombre del producto.
    :param cantidad: cantidad de productos en el almacen.
    :param shelfTimePromedioDias: tiempo promedio de permanencia de un producto en el almacen.
    :param bloque: bloque en el que se encuentra el producto en el almacen.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})
        MATCH (p:Producto {Nombre: $producto})
        CREATE (a)-[r:INVENTARIO_ALMACEN]->(p)
        SET r.cantidad = $cantidad
        SET r.shelfTimePromedioDias = $shelfTimePromedioDias
        SET r.bloque = $bloque

        """,
        almacen=almacen,
        producto=producto,
        cantidad=cantidad,
        shelfTimePromedioDias=shelfTimePromedioDias,
        bloque=bloque,
        database = 'neo4j'

    )

    return f'Relacion inventario almacen creada entre {almacen} y {producto}: ({cantidad}, {shelfTimePromedioDias}, {bloque})', result

def delete_inventario_almacen(driver, almacen, producto):
    """
    Elimina una relacion de inventario almacen entre un almacen y un producto

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param producto: nombre del producto.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:INVENTARIO_ALMACEN]->(p:Producto {Nombre: $producto})
        DELETE r

        """,
        almacen=almacen,
        producto=producto,
        database = 'neo4j'

    )

    return f'Relacion inventario almacen eliminada entre {almacen} y {producto}', result

def update_inventario_almacen(driver, almacen, producto, cantidad, shelfTimePromedioDias, bloque):
    """
    Actualiza una relacion de inventario almacen entre un almacen y un producto

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param producto: nombre del producto.
    :param cantidad: cantidad de productos en el almacen.
    :param shelfTimePromedioDias: tiempo promedio de permanencia de un producto en el almacen.
    :param bloque: bloque en el que se encuentra el producto en el almacen.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:INVENTARIO_ALMACEN]->(p:Producto {Nombre: $producto})
        SET r.cantidad = $cantidad
        SET r.shelfTimePromedioDias = $shelfTimePromedioDias
        SET r.bloque = $bloque

        """,
        almacen=almacen,
        producto=producto,
        cantidad=cantidad,
        shelfTimePromedioDias=shelfTimePromedioDias,
        bloque=bloque,
        database = 'neo4j'

    )

    return f'Relacion inventario almacen actualizada entre {almacen} y {producto}: ({cantidad}, {shelfTimePromedioDias}, {bloque})', result

def get_inventario_almacen_almacen(driver, almacen):
    """
    Obtiene la relacion de inventario almacen en base al nombre del almacen

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:INVENTARIO_ALMACEN]->(p:Producto)
        RETURN r, p

        """,
        almacen=almacen,
        database = 'neo4j'

    )

    return result

def get_inventario_almacen_producto(driver, producto):
    """
    Obtiene la relacion de inventario almacen en base al nombre del producto

    :param driver: driver de la base de datos Neo4j.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén)-[r:INVENTARIO_ALMACEN]->(p:Producto {Nombre: $producto})
        RETURN a, r

        """,
        producto=producto,
        database = 'neo4j'

    )

    return result

def get_inventario_almacen_almacen_producto(driver, almacen, producto):
    """
    Obtiene la relacion de inventario almacen entre un almacen y un producto

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (a:Almacén {Nombre: $almacen})-[r:INVENTARIO_ALMACEN]->(p:Producto {Nombre: $producto})
        RETURN r

        """,
        almacen=almacen,
        producto=producto,
        database = 'neo4j'

    )

    return result

# inventario_tienda

def create_inventario_tienda(driver, tienda, producto, cantidad, shelfTimePromedioDias, pasillo):
    """
    
    Crea una relacion de inventario tienda entre una tienda y un producto

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :param producto: nombre del producto.
    :param cantidad: cantidad de productos en la tienda.
    :param shelfTimePromedioDias: tiempo promedio de permanencia de un producto en la tienda.
    :param pasillo: pasillo en el que se encuentra el producto en la tienda.
    
    """

    result = driver.execute_query(
        """
        MATCH (t:Tienda {Nombre: $tienda})
        MATCH (p:Producto {Nombre: $producto})
        CREATE (t)-[r:INVENTARIO_TIENDA]->(p)
        SET r.cantidad = $cantidad
        SET r.shelfTimePromedioDias = $shelfTimePromedioDias
        SET r.pasillo = $pasillo

        """,
        tienda=tienda,
        producto=producto,
        cantidad=cantidad,
        shelfTimePromedioDias=shelfTimePromedioDias,
        pasillo=pasillo,
        database = 'neo4j'

    )

    return f'Relacion inventario tienda creada entre {tienda} y {producto}: ({cantidad}, {shelfTimePromedioDias}, {pasillo})', result

def delete_inventario_tienda(driver, tienda, producto):
    """
    Elimina una relacion de inventario tienda entre una tienda y un producto

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :param producto: nombre del producto.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (t:Tienda {Nombre: $tienda})-[r:INVENTARIO_TIENDA]->(p:Producto {Nombre: $producto})
        DELETE r

        """,
        tienda=tienda,
        producto=producto,
        database = 'neo4j'

    )

    return f'Relacion inventario tienda eliminada entre {tienda} y {producto}', result

def update_inventario_tienda(driver, tienda, producto, cantidad, shelfTimePromedioDias, pasillo):
    """
    Actualiza una relacion de inventario tienda entre una tienda y un producto

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :param producto: nombre del producto.
    :param cantidad: cantidad de productos en la tienda.
    :param shelfTimePromedioDias: tiempo promedio de permanencia de un producto en la tienda.
    :param pasillo: pasillo en el que se encuentra el producto en la tienda.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (t:Tienda {Nombre: $tienda})-[r:INVENTARIO_TIENDA]->(p:Producto {Nombre: $producto})
        SET r.cantidad = $cantidad
        SET r.shelfTimePromedioDias = $shelfTimePromedioDias
        SET r.pasillo = $pasillo

        """,
        tienda=tienda,
        producto=producto,
        cantidad=cantidad,
        shelfTimePromedioDias=shelfTimePromedioDias,
        pasillo=pasillo,
        database = 'neo4j'

    )

    return f'Relacion inventario tienda actualizada entre {tienda} y {producto}: ({cantidad}, {shelfTimePromedioDias}, {pasillo})', result


def get_inventario_tienda_tienda(driver, tienda):
    """
    Obtiene la relacion de inventario tienda en base al nombre de la tienda

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (t:Tienda {Nombre: $tienda})-[r:INVENTARIO_TIENDA]->(p:Producto)
        RETURN r, p

        """,
        tienda=tienda,
        database = 'neo4j'

    )

    return result

def get_inventario_tienda_producto(driver, producto):
    """
    Obtiene la relacion de inventario tienda en base al nombre del producto

    :param driver: driver de la base de datos Neo4j.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (t:Tienda)-[r:INVENTARIO_TIENDA]->(p:Producto {Nombre: $producto})
        RETURN t, r

        """,
        producto=producto,
        database = 'neo4j'

    )

    return result

def get_inventario_tienda_tienda_producto(driver, tienda, producto):
    """
    Obtiene la relacion de inventario tienda entre una tienda y un producto

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (t:Tienda {Nombre: $tienda})-[r:INVENTARIO_TIENDA]->(p:Producto {Nombre: $producto})
        RETURN r

        """,
        tienda=tienda,
        producto=producto,
        database = 'neo4j'

    )

    return result

# ordenado_a_almacen 

def create_ordenado_a_almacen(driver, documento, almacen, administrador, numeroConfirmacion, prioridad):
    """
    Crea una relacion de ordenado a almacen entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :param administrador: nombre del administrador del almacen.
    :param numeroConfirmacion: numero de confirmacion del despacho.
    :param prioridad: prioridad del despacho.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})
        MATCH (a:Almacén {Nombre: $almacen})
        CREATE (d)-[r:ORDENADO_A_ALMACEN]->(a)
        SET r.administrador = $administrador
        SET r.numeroConfirmacion = $numeroConfirmacion
        SET r.prioridad = $prioridad

        """,
        documento=documento,
        almacen=almacen,
        administrador=administrador,
        numeroConfirmacion=numeroConfirmacion,
        prioridad=prioridad,
        database = 'neo4j'

    )

    return f'Relacion ordenado a almacen creada entre {documento} y {almacen}: ({administrador}, {numeroConfirmacion}, {prioridad})', result

def delete_ordenado_a_almacen(driver, documento, almacen):
    """
    Elimina una relacion de ordenado a almacen entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_ALMACEN]->(a:Almacén {Nombre: $almacen})
        DELETE r

        """,
        documento=documento,
        almacen=almacen,
        database = 'neo4j'

    )

    return f'Relacion ordenado a almacen eliminada entre {documento} y {almacen}', result

def update_ordenado_a_almacen(driver, documento, almacen, administrador, numeroConfirmacion, prioridad):
    """
    Actualiza una relacion de ordenado a almacen entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :param administrador: nombre del administrador del almacen.
    :param numeroConfirmacion: numero de confirmacion del despacho.
    :param prioridad: prioridad del despacho.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_ALMACEN]->(a:Almacén {Nombre: $almacen})
        SET r.administrador = $administrador
        SET r.numeroConfirmacion = $numeroConfirmacion
        SET r.prioridad = $prioridad

        """,
        documento=documento,
        almacen=almacen,
        administrador=administrador,
        numeroConfirmacion=numeroConfirmacion,
        prioridad=prioridad,
        database = 'neo4j'

    )

    return f'Relacion ordenado a almacen actualizada entre {documento} y {almacen}: ({administrador}, {numeroConfirmacion}, {prioridad})', result

def get_ordenado_a_almacen_documento(driver, documento):
    """
    Obtiene la relacion de ordenado a almacen en base al documento del despacho

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_ALMACEN]->(a:Almacén)
        RETURN r, a

        """,
        documento=documento,
        database = 'neo4j'

    )

    return result

def get_ordenado_a_almacen_almacen(driver, almacen):
    """
    Obtiene la relacion de ordenado a almacen en base al nombre del almacen

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento)-[r:ORDENADO_A_ALMACEN]->(a:Almacén {Nombre: $almacen})
        RETURN r, d

        """,
        almacen=almacen,
        database = 'neo4j'

    )

    return result

def get_ordenado_a_almacen_documento_almacen(driver, documento, almacen):
    """
    Obtiene la relacion de ordenado a almacen entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_ALMACEN]->(a:Almacén {Nombre: $almacen})
        RETURN r

        """,
        documento=documento,
        almacen=almacen,
        database = 'neo4j'

    )

    return result

#ordemado_a_empresa

def create_ordenado_a_empresa(driver, documento, empresa, corresponsal, numeroConfirmacion,prioridad):
    """
    Crea una relacion de ordenado a empresa entre un documento y una empresa

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param empresa: nombre de la empresa.
    :param corresponsal: nombre del corresponsal de la empresa.
    :param numeroConfirmacion: numero de confirmacion del despacho.
    :param prioridad: prioridad del despacho.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})
        MATCH (e:Empresa {Nombre: $empresa})
        CREATE (d)-[r:ORDENADO_A_EMPRESA]->(e)
        SET r.corresponsal = $corresponsal
        SET r.numeroConfirmacion = $numeroConfirmacion
        SET r.prioridad = $prioridad

        """,
        documento=documento,
        empresa=empresa,
        corresponsal=corresponsal,
        numeroConfirmacion=numeroConfirmacion,
        prioridad=prioridad,
        database = 'neo4j'

    )

    return f'Relacion ordenado a empresa creada entre {documento} y {empresa}: ({corresponsal}, {numeroConfirmacion}, {prioridad})', result

def delete_ordenado_a_empresa(driver, documento, empresa):
    """
    Elimina una relacion de ordenado a empresa entre un documento y una empresa

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param empresa: nombre de la empresa.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_EMPRESA]->(e:Empresa {Nombre: $empresa})
        DELETE r

        """,
        documento=documento,
        empresa=empresa,
        database = 'neo4j'

    )

    return f'Relacion ordenado a empresa eliminada entre {documento} y {empresa}', result

def update_ordenado_a_empresa(driver, documento, empresa, corresponsal, numeroConfirmacion, prioridad):
    """
    Actualiza una relacion de ordenado a empresa entre un documento y una empresa

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param empresa: nombre de la empresa.
    :param corresponsal: nombre del corresponsal de la empresa.
    :param numeroConfirmacion: numero de confirmacion del despacho.
    :param prioridad: prioridad del despacho.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_EMPRESA]->(e:Empresa {Nombre: $empresa})
        SET r.corresponsal = $corresponsal
        SET r.numeroConfirmacion = $numeroConfirmacion
        SET r.prioridad = $prioridad

        """,
        documento=documento,
        empresa=empresa,
        corresponsal=corresponsal,
        numeroConfirmacion=numeroConfirmacion,
        prioridad=prioridad,
        database = 'neo4j'

    )

    return f'Relacion ordenado a empresa actualizada entre {documento} y {empresa}: ({corresponsal}, {numeroConfirmacion}, {prioridad})', result

def get_ordenado_a_empresa_documento(driver, documento):
    """
    Obtiene la relacion de ordenado a empresa en base al documento del despacho

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_EMPRESA]->(e:Empresa)
        RETURN r, e

        """,
        documento=documento,
        database = 'neo4j'

    )

    return result

def get_ordenado_a_empresa_empresa(driver, empresa):
    """
    Obtiene la relacion de ordenado a empresa en base al nombre de la empresa

    :param driver: driver de la base de datos Neo4j.
    :param empresa: nombre de la empresa.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento)-[r:ORDENADO_A_EMPRESA]->(e:Empresa {Nombre: $empresa})
        RETURN r, d

        """,
        empresa=empresa,
        database = 'neo4j'

    )

    return result

def get_ordenado_a_empresa_documento_empresa(driver, documento, empresa):
    """
    Obtiene la relacion de ordenado a empresa entre un documento y una empresa

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param empresa: nombre de la empresa.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENADO_A_EMPRESA]->(e:Empresa {Nombre: $empresa})
        RETURN r

        """,
        documento=documento,
        empresa=empresa,
        database = 'neo4j'

    )

    return result

# ordenes

def create_ordenes(driver, documento, almacen, hechaPor, hora, responsable):
    """
    Crea una relacion de ordenes entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :param hechaPor: nombre de la persona que hizo la orden.
    :param hora: hora en la que se hizo la orden.
    :param responsable: nombre de la persona responsable de la orden.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})
        MATCH (a:Almacén {Nombre: $almacen})
        CREATE (d)-[r:ORDENES]->(a)
        SET r.hechaPor = $hechaPor
        SET r.hora = $hora
        SET r.responsable = $responsable

        """,
        documento=documento,
        almacen=almacen,
        hechaPor=hechaPor,
        hora=hora,
        responsable=responsable,
        database = 'neo4j'

    )

    return f'Relacion ordenes creada entre {documento} y {almacen}: ({hechaPor}, {hora}, {responsable})', result

def delete_ordenes(driver, documento, almacen):
    """
    Elimina una relacion de ordenes entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENES]->(a:Almacén {Nombre: $almacen})
        DELETE r

        """,
        documento=documento,
        almacen=almacen,
        database = 'neo4j'

    )

    return f'Relacion ordenes eliminada entre {documento} y {almacen}', result

def update_ordenes(driver, documento, almacen, hechaPor, hora, responsable):
    """
    Actualiza una relacion de ordenes entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :param hechaPor: nombre de la persona que hizo la orden.
    :param hora: hora en la que se hizo la orden.
    :param responsable: nombre de la persona responsable de la orden.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENES]->(a:Almacén {Nombre: $almacen})
        SET r.hechaPor = $hechaPor
        SET r.hora = $hora
        SET r.responsable = $responsable

        """,
        documento=documento,
        almacen=almacen,
        hechaPor=hechaPor,
        hora=hora,
        responsable=responsable,
        database = 'neo4j'

    )

    return f'Relacion ordenes actualizada entre {documento} y {almacen}: ({hechaPor}, {hora}, {responsable})', result

def get_ordenes_documento(driver, documento):
    """
    Obtiene la relacion de ordenes en base al documento del despacho

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENES]->(a:Almacén)
        RETURN r, a

        """,
        documento=documento,
        database = 'neo4j'

    )

    return result

def get_ordenes_almacen(driver, almacen):
    """
    Obtiene la relacion de ordenes en base al nombre del almacen

    :param driver: driver de la base de datos Neo4j.
    :param almacen: nombre del almacen.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento)-[r:ORDENES]->(a:Almacén {Nombre: $almacen})
        RETURN r, d

        """,
        almacen=almacen,
        database = 'neo4j'

    )

    return result

def get_ordenes_documento_almacen(driver, documento, almacen):
    """
    Obtiene la relacion de ordenes entre un documento y un almacen

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param almacen: nombre del almacen.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:ORDENES]->(a:Almacén {Nombre: $almacen})
        RETURN r

        """,
        documento=documento,
        almacen=almacen,
        database = 'neo4j'

    )

    return result

# productos_ordenados

def create_productos_ordenados(driver, documento, producto, cantidad,colores,Premium):
    """
    
    Crea una relacion de productos ordenados entre un documento y un producto
    
    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param producto: nombre del producto.
    :param cantidad: cantidad de productos ordenados.
    :param colores: colores del producto.
    :param Premium: si el producto es premium o no.

    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})
        MATCH (p:Producto {Nombre: $producto})
        CREATE (d)-[r:PRODUCTOS_ORDENADOS]->(p)
        SET r.cantidad = $cantidad
        SET r.colores = $colores
        SET r.Premium = $Premium

        """,
        documento=documento,
        producto=producto,
        cantidad=cantidad,
        colores=colores,
        Premium=Premium,
        database = 'neo4j'

    )

    return f'Relacion productos ordenados creada entre {documento} y {producto}: ({cantidad}, {colores}, {Premium})', result

def delete_productos_ordenados(driver, documento, producto):
    """
    Elimina una relacion de productos ordenados entre un documento y un producto

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param producto: nombre del producto.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:PRODUCTOS_ORDENADOS]->(p:Producto {Nombre: $producto})
        DELETE r

        """,
        documento=documento,
        producto=producto,
        database = 'neo4j'

    )

    return f'Relacion productos ordenados eliminada entre {documento} y {producto}', result

def update_productos_ordenados(driver, documento, producto, cantidad, colores, Premium):
    """
    Actualiza una relacion de productos ordenados entre un documento y un producto

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param producto: nombre del producto.
    :param cantidad: cantidad de productos ordenados.
    :param colores: colores del producto.
    :param Premium: si el producto es premium o no.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:PRODUCTOS_ORDENADOS]->(p:Producto {Nombre: $producto})
        SET r.cantidad = $cantidad
        SET r.colores = $colores
        SET r.Premium = $Premium

        """,
        documento=documento,
        producto=producto,
        cantidad=cantidad,
        colores=colores,
        Premium=Premium,
        database = 'neo4j'

    )

    return f'Relacion productos ordenados actualizada entre {documento} y {producto}: ({cantidad}, {colores}, {Premium})', result

def get_productos_ordenados_documento(driver, documento):
    """
    Obtiene la relacion de productos ordenados en base al documento del despacho

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:PRODUCTOS_ORDENADOS]->(p:Producto)
        RETURN r, p

        """,
        documento=documento,
        database = 'neo4j'

    )

    return result

def get_productos_ordenados_producto(driver, producto):
    """
    Obtiene la relacion de productos ordenados en base al nombre del producto

    :param driver: driver de la base de datos Neo4j.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento)-[r:PRODUCTOS_ORDENADOS]->(p:Producto {Nombre: $producto})
        RETURN d, r

        """,
        producto=producto,
        database = 'neo4j'

    )

    return result

def get_productos_ordenados_documento_producto(driver, documento, producto):
    """
    Obtiene la relacion de productos ordenados entre un documento y un producto

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento del despacho.
    :param producto: nombre del producto.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:PRODUCTOS_ORDENADOS]->(p:Producto {Nombre: $producto})
        RETURN r

        """,
        documento=documento,
        producto=producto,
        database = 'neo4j'

    )

    return result

# solicitud

def create_solicitud(driver, documento, tienda, firmadaPor,modalidad,metodoPago):
    """
    Crea una relacion de solicitud entre un documento y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento de la solicitud.
    :param tienda: nombre de la tienda.
    :param firmadaPor: nombre de la persona que firmo la solicitud.
    :param modalidad: modalidad de la solicitud.
    :param metodoPago: metodo de pago de la solicitud.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})
        MATCH (t:Tienda {Nombre: $tienda})
        CREATE (d)-[r:SOLICITUD]->(t)
        SET r.firmadaPor = $firmadaPor
        SET r.modalidad = $modalidad
        SET r.metodoPago = $metodoPago

        """,
        documento=documento,
        tienda=tienda,
        firmadaPor=firmadaPor,
        modalidad=modalidad,
        metodoPago=metodoPago,
        database = 'neo4j'

    )

    return f'Relacion solicitud creada entre {documento} y {tienda}: ({firmadaPor}, {modalidad}, {metodoPago})', result

def delete_solicitud(driver, documento, tienda):
    """
    Elimina una relacion de solicitud entre un documento y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento de la solicitud.
    :param tienda: nombre de la tienda.
    :return: mensaje de exito y resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:SOLICITUD]->(t:Tienda {Nombre: $tienda})
        DELETE r

        """,
        documento=documento,
        tienda=tienda,
        database = 'neo4j'

    )

    return f'Relacion solicitud eliminada entre {documento} y {tienda}', result

def update_solicitud(driver, documento, tienda, firmadaPor, modalidad, metodoPago):
    """
    Actualiza una relacion de solicitud entre un documento y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento de la solicitud.
    :param tienda: nombre de la tienda.
    :param firmadaPor: nombre de la persona que firmo la solicitud.
    :param modalidad: modalidad de la solicitud.
    :param metodoPago: metodo de pago de la solicitud.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:SOLICITUD]->(t:Tienda {Nombre: $tienda})
        SET r.firmadaPor = $firmadaPor
        SET r.modalidad = $modalidad
        SET r.metodoPago = $metodoPago

        """,
        documento=documento,
        tienda=tienda,
        firmadaPor=firmadaPor,
        modalidad=modalidad,
        metodoPago=metodoPago,
        database = 'neo4j'

    )

    return f'Relacion solicitud actualizada entre {documento} y {tienda}: ({firmadaPor}, {modalidad}, {metodoPago})', result

def get_solicitud_documento(driver, documento):
    """
    Obtiene la relacion de solicitud en base al documento de la solicitud

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento de la solicitud.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:SOLICITUD]->(t:Tienda)
        RETURN r, t

        """,
        documento=documento,
        database = 'neo4j'

    )

    return result


def get_solicitud_tienda(driver, tienda):
    """
    Obtiene la relacion de solicitud en base al nombre de la tienda

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento)-[r:SOLICITUD]->(t:Tienda {Nombre: $tienda})
        RETURN r, d

        """,
        tienda=tienda,
        database = 'neo4j'

    )

    return result

def get_solicitud_documento_tienda(driver, documento, tienda):

    """
    Obtiene la relacion de solicitud entre un documento y una tienda

    :param driver: driver de la base de datos Neo4j.
    :param documento: documento de la solicitud.
    :param tienda: nombre de la tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (d:Documento {Numero: $documento})-[r:SOLICITUD]->(t:Tienda {Nombre: $tienda})
        RETURN r

        """,
        documento=documento,
        tienda=tienda,
        database = 'neo4j'

    )

    return result

# Distanica_tienda

def create_distancia_tienda(driver, tienda1, tienda2,distancia,tiempo_mins,costo):

    """
    Crea una relacion de distancia entre dos tiendas

    :param driver: driver de la base de datos Neo4j.
    :param tienda1: nombre de la primera tienda.
    :param tienda2: nombre de la segunda tienda.
    :param distancia: distancia entre las tiendas.
    :param tiempo_mins: tiempo en minutos entre las tiendas.
    :param costo: costo de transporte entre las tiendas.

    :return: mensaje de exito y resultado de la consulta.
    
    
    """

    result = driver.execute_query(

        """
        MATCH (t1:Tienda {Nombre: $tienda1})
        MATCH (t2:Tienda {Nombre: $tienda2})
        CREATE (t1)-[r:DISTANCIA_TIENDA]->(t2)
        SET r.distancia = $distancia
        SET r.tiempo_mins = $tiempo_mins
        SET r.costo = $costo

        """,
        tienda1=tienda1,
        tienda2=tienda2,
        distancia=distancia,
        tiempo_mins=tiempo_mins,
        costo=costo,
        database = 'neo4j'

    )

    return f'Relacion distancia creada entre {tienda1} y {tienda2}: ({distancia}, {tiempo_mins}, {costo})', result


def delete_distancia_tienda(driver, tienda1, tienda2):
    
    """
    Elimina una relacion de distancia entre dos tiendas

    :param driver: driver de la base de datos Neo4j.
    :param tienda1: nombre de la primera tienda.
    :param tienda2: nombre de la segunda tienda.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (t1:Tienda {Nombre: $tienda1})-[r:DISTANCIA_TIENDA]->(t2:Tienda {Nombre: $tienda2})
        DELETE r

        """,
        tienda1=tienda1,
        tienda2=tienda2,
        database = 'neo4j'

    )

    return f'Relacion distancia eliminada entre {tienda1} y {tienda2}', result

def update_distancia_tienda(driver, tienda1, tienda2, distancia, tiempo_mins, costo):

    """
    Actualiza una relacion de distancia entre dos tiendas

    :param driver: driver de la base de datos Neo4j.
    :param tienda1: nombre de la primera tienda.
    :param tienda2: nombre de la segunda tienda.
    :param distancia: distancia entre las tiendas.
    :param tiempo_mins: tiempo en minutos entre las tiendas.
    :param costo: costo de transporte entre las tiendas.
    :return: mensaje de exito y resultado de la consulta.
    """

    result = driver.execute_query(

        """
        MATCH (t1:Tienda {Nombre: $tienda1})-[r:DISTANCIA_TIENDA]->(t2:Tienda {Nombre: $tienda2})
        SET r.distancia = $distancia
        SET r.tiempo_mins = $tiempo_mins
        SET r.costo = $costo

        """,
        tienda1=tienda1,
        tienda2=tienda2,
        distancia=distancia,
        tiempo_mins=tiempo_mins,
        costo=costo,
        database = 'neo4j'

    )

    return f'Relacion distancia actualizada entre {tienda1} y {tienda2}: ({distancia}, {tiempo_mins}, {costo})', result

def get_distancia_tienda_tienda(driver, tienda):
    """
    Obtiene la relacion de distancia en base al nombre de la tienda

    :param driver: driver de la base de datos Neo4j.
    :param tienda: nombre de la tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (t1:Tienda {Nombre: $tienda})-[r:DISTANCIA_TIENDA]->(t2:Tienda)
        RETURN r, t2

        """,
        tienda=tienda,
        database = 'neo4j'

    )

    return result

def get_distancia_tienda_tienda_tienda(driver, tienda1, tienda2):
    """
    Obtiene la relacion de distancia entre dos tiendas

    :param driver: driver de la base de datos Neo4j.
    :param tienda1: nombre de la primera tienda.
    :param tienda2: nombre de la segunda tienda.
    :return:resultado de la consulta.
    """
    result = driver.execute_query(

        """
        MATCH (t1:Tienda {Nombre: $tienda1})-[r:DISTANCIA_TIENDA]->(t2:Tienda {Nombre: $tienda2})
        RETURN r

        """,
        tienda1=tienda1,
        tienda2=tienda2,
        database = 'neo4j'

    )

    return result






