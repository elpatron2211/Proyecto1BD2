from neo4j import GraphDatabase


#Empresa

def createEmpresa(driver, tipo, nombre, pais, telefono, email):
    """
    :param driver: Neo4j driver
    :param tipo: str
    :param nombre: str
    :param pais: str
    :param telefono: str
    :param email: str

    :return: str, neo4j result


    """
    result = driver.execute_query(
        """
        MERGE (e:Empresa {Tipo: $tipo, Nombre: $nombre, Pais: $pais, Telefono: $telefono, Email: $email})
        RETURN e
        """, tipo=tipo, nombre=nombre, pais=pais, telefono=telefono, email=email, database='neo4j'
    )
    return f"Empresa creada: ({tipo}, {nombre}, {pais}, {telefono}, {email})", result

def readEmpresa(driver, nombre):
    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (e:Empresa {Nombre: $nombre})
        RETURN e
        """, nombre=nombre, database='neo4j'
    )
    return result

def updateEmpresa(driver, tipo, nombre, pais, telefono, email):
    """
    :param driver: Neo4j driver
    :param nombre: str
    :param telefono: str
    :param email: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (e:Empresa {Nombre: $nombre})
        SET e.Telefono = $telefono, 
            e.Email = $email,
            e.Pais = $pais,
            e.Tipo = $tipo
        RETURN e
        """, tipo=tipo, pais=pais, nombre=nombre, telefono=telefono, email=email, database='neo4j'
    )
    return f"Empresa actualizada: ({nombre}, {tipo}, {pais}, {telefono}, {email})", result

def deleteEmpresa(driver, nombre):
    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (e:Empresa {Nombre: $nombre})
        DETACH DELETE e
        """, nombre=nombre, database='neo4j'
    )
    return f"Empresa eliminada: {nombre}", result

#Producto

def createProducto(driver, nombre, precio, codigo, tipo, marca):
    """
    :param driver: Neo4j driver
    :param nombre: str
    :param precio: str
    :param codigo: str
    :param tipo: str
    :param marca: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MERGE (p:Producto {Nombre: $nombre, Precio: $precio, Codigo: $codigo, Tipo: $tipo, Marca: $marca})
        RETURN p
        """, nombre=nombre, precio=precio, codigo=codigo, tipo=tipo, marca=marca, database='neo4j'
    )
    return f"Producto creado: ({nombre}, {precio}, {codigo}, {tipo}, {marca})", result

def readProducto(driver, nombre):
    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (p:Producto {Nombre: $nombre})
        RETURN p
        """, nombre=nombre, database='neo4j'
    )
    return result

def updateProducto(driver, nombre, precio, codigo, tipo, marca):
    """
    :param driver: Neo4j driver
    :param nombre: str
    :param precio: str
    :param codigo: str
    :param tipo: str
    :param marca: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (p:Producto {Nombre: $nombre})
        SET p.Precio = $precio, 
            p.Codigo = $codigo,
            p.Tipo = $tipo,
            p.Marca = $marca
        RETURN p
        """, nombre=nombre, precio=precio, codigo=codigo, tipo=tipo, marca=marca, database='neo4j'
    )
    return f"Producto actualizado: ({nombre}, {precio}, {codigo}, {tipo}, {marca})", result

def deleteProducto(driver, nombre):
    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (p:Producto {Nombre: $nombre})
        DETACH DELETE p
        """, nombre=nombre, database='neo4j'
    )
    return f"Producto eliminado: {nombre}",

#Documentos

def createDocumento(driver, tipoDocumento, fechaEmision, numero, estado, total):
    """
    :param driver: Neo4j driver
    :param tipoDocumento: str
    :param fechaEmision: str
    :param numero: str
    :param estado: str
    :param total: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MERGE (d:Documento {TipoDocumento: $tipoDocumento, FechaEmisión: $fechaEmision, Numero: $numero, Estado: $estado, Total: $total})
        RETURN d
        """, tipoDocumento=tipoDocumento, fechaEmision=fechaEmision, numero=numero, estado=estado, total=total, database='neo4j'
    )
    return f"Documento creado: ({tipoDocumento}, {fechaEmision}, {numero}, {estado}, {total})", result

def readDocumento(driver, numero):
    """
    :param driver: Neo4j driver
    :param numero: str

    :return: neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (d:Documento {Numero: $numero})
        RETURN d
        """, numero=numero, database='neo4j'
    )
    return result

def updateDocumento(driver, tipoDocumento, fechaEmision, numero, estado, total):

    """
    :param driver: Neo4j driver
    :param tipoDocumento: str
    :param fechaEmision: str
    :param numero: str
    :param estado: str
    :param total: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (d:Documento {Numero: $numero})
        SET d.TipoDocumento = $tipoDocumento, 
            d.FechaEmisión = $fechaEmision,
            d.Estado = $estado,
            d.Total = $total
        RETURN d
        """, tipoDocumento=tipoDocumento, fechaEmision=fechaEmision, numero=numero, estado=estado, total=total, database='neo4j'
    )
    return f"Documento actualizado: ({tipoDocumento}, {fechaEmision}, {numero}, {estado}, {total})", result

def deleteDocumento(driver, numero):
    """
    :param driver: Neo4j driver
    :param numero: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (d:Documento {Numero: $numero})
        DETACH DELETE d
        """, numero=numero, database='neo4j'
    )
    return f"Documento eliminado: {numero}",


# Almacenes

def createAlmacen(driver, nombre, direccion, telefono, ciudad, tipoAlmacen):
    """
    :param driver: Neo4j driver
    :param nombre: str
    :param direccion: str
    :param telefono: str
    :param ciudad: str
    :param tipoAlmacen: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MERGE (a:Almacén {Nombre: $nombre, Direccion: $direccion, Telefono: $telefono, Ciudad: $ciudad, TipoAlmacen: $tipoAlmacen})
        RETURN a
        """, nombre=nombre, direccion=direccion, telefono=telefono, ciudad=ciudad, tipoAlmacen=tipoAlmacen, database='neo4j'
    )
    return f"Almacén creado: ({nombre}, {direccion}, {telefono}, {ciudad}, {tipoAlmacen})", result

def readAlmacen(driver, nombre):
    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (a:Almacén {Nombre: $nombre})
        RETURN a
        """, nombre=nombre, database='neo4j'
    )
 
    return result

def updateAlmacen(driver, nombre, direccion, telefono, ciudad, tipoAlmacen):
    """
    :param driver: Neo4j driver
    :param nombre: str
    :param direccion: str
    :param telefono: str
    :param ciudad: str
    :param tipoAlmacen: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (a:Almacén {Nombre: $nombre})
        SET a.Direccion = $direccion, 
            a.Telefono = $telefono,
            a.Ciudad = $ciudad,
            a.TipoAlmacen = $tipoAlmacen
        RETURN a
        """, nombre=nombre, direccion=direccion, telefono=telefono, ciudad=ciudad, tipoAlmacen=tipoAlmacen, database='neo4j'
    )
    return f"Almacen actualizado: ({nombre}, {direccion}, {telefono}, {ciudad}, {tipoAlmacen})", result

def deleteAlmacen(driver, nombre):
    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (a:Almacén {Nombre: $nombre})
        DETACH DELETE a
        """, nombre=nombre, database='neo4j'
    )
    return f"Almacen eliminado: {nombre}",

# Tiendas

def createTienda(driver, nombre, direccion, telefono, ciudad, asesor):
    """
    :param driver: Neo4j driver
    :param nombre: str
    :param direccion: str
    :param telefono: str
    :param ciudad: str
    :param asesor: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MERGE (t:Tienda {Nombre: $nombre, Direccion: $direccion, Telefono: $telefono, Ciudad: $ciudad, Asesor: $asesor})
        RETURN t
        """, nombre=nombre, direccion=direccion, telefono=telefono, ciudad=ciudad, asesor=asesor, database='neo4j'
    )
    return f"Tienda creada: ({nombre}, {direccion}, {telefono}, {ciudad}, {asesor})", result

def readTienda(driver, nombre):
    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (t:Tienda {Nombre: $nombre})
        RETURN t
        """, nombre=nombre, database='neo4j'
    )
    return result

def updateTienda(driver, nombre, direccion, telefono, ciudad, asesor):

    """
    :param driver: Neo4j driver
    :param nombre: str
    :param direccion: str
    :param telefono: str
    :param ciudad: str
    :param asesor: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (t:Tienda {Nombre: $nombre})
        SET t.Direccion = $direccion, 
            t.Telefono = $telefono,
            t.Ciudad = $ciudad,
            t.Asesor = $asesor
        RETURN t
        """, nombre=nombre, direccion=direccion, telefono=telefono, ciudad=ciudad, asesor=asesor, database='neo4j'
    )
    return f"Tienda actualizada: ({nombre}, {direccion}, {telefono}, {ciudad}, {asesor})", result

def deleteTienda(driver, nombre):

    """
    :param driver: Neo4j driver
    :param nombre: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (t:Tienda {Nombre: $nombre})
        DETACH DELETE t
        """, nombre=nombre, database='neo4j'
    )
    return f"Tienda eliminada: {nombre}",

# Camiones

def createCamion(driver, placas, marca, modelo, capacidad, piloto):
    """
    :param driver: Neo4j driver
    :param placas: str
    :param marca: str
    :param modelo: str
    :param capacidad: str
    :param piloto: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MERGE (c:Camión {Placas: $placas, Marca: $marca, Modelo: $modelo, Capacidad: $capacidad, Piloto: $piloto})
        RETURN c
        """, placas=placas, marca=marca, modelo=modelo, capacidad=capacidad, piloto=piloto, database='neo4j'
    )
    return f"Camión creado: ({placas}, {marca}, {modelo}, {capacidad}, {piloto})", result

def readCamion(driver, placas):
    """
    :param driver: Neo4j driver
    :param placas: str

    :return: neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (c:Camión {Placas: $placas})
        RETURN c
        """, placas=placas, database='neo4j'
    )
    return result

def updateCamion(driver, placas, marca, modelo, capacidad, piloto):
    """
    :param driver: Neo4j driver
    :param placas: str
    :param marca: str
    :param modelo: str
    :param capacidad: str
    :param piloto: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (c:Camión {Placas: $placas})
        SET c.Marca = $marca, 
            c.Modelo = $modelo,
            c.Capacidad = $capacidad,
            c.Piloto = $piloto
        RETURN c
        """, placas=placas, marca=marca, modelo=modelo, capacidad=capacidad, piloto=piloto, database='neo4j'
    )
    return f"Camion actualizado: ({placas}, {marca}, {modelo}, {capacidad}, {piloto})", result

def deleteCamion(driver, placas):
    """
    :param driver: Neo4j driver
    :param placas: str

    :return: str, neo4j result
    """
    result = driver.execute_query(
        """
        MATCH (c:Camión {Placas: $placas})
        DETACH DELETE c
        """, placas=placas, database='neo4j'
    )
    return f"Camion eliminado: {placas}",






