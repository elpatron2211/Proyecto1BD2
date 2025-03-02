from neo4j import GraphDatabase

# despachos

def crear_relacion_despacho(driver, almacen, camion, documento, codigoConfirmacion, fechaEntrega):
    result = driver.execute_query(

        """
        MATCH (a:Almacen {nombre: $almacen})
        MATCH (c:Camion {placa: $camion})
        CREATE (a)-[r:DESPACHO]->(c)
        SET r.documento = $documento
        SET r.codigoConfirmacion = $codigoConfirmacion
        SET r.fechaEntrega = $fechaEntrega
        

        """
    )