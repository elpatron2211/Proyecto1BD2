from neo4j import GraphDatabase
from crud import *

from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

def crear_matriz_distancias(almacen, dist_almacen_tienda, dist_tienda_tienda):
    """Crea una matriz de distancias que incluye almacén-tienda y tienda-tienda."""
    ubicaciones = [almacen] + list(set([t[0] for t in dist_tienda_tienda] + [t[1] for t in dist_tienda_tienda]))
    indice_mapa = {loc: i for i, loc in enumerate(ubicaciones)}
    
    tamaño = len(ubicaciones)
    matriz_distancias = [[float('inf')] * tamaño for _ in range(tamaño)]
    
    # Distancias almacén-tienda (simétricas)
    for al, tienda, dist in dist_almacen_tienda:
        i, j = indice_mapa[al], indice_mapa[tienda]
        matriz_distancias[i][j] = matriz_distancias[j][i] = dist

    # Distancias tienda-tienda (asimétricas)
    for t1, t2, dist in dist_tienda_tienda:
        i, j = indice_mapa[t1], indice_mapa[t2]
        matriz_distancias[i][j] = dist

    return matriz_distancias, indice_mapa

def resolver_tsp(matriz_distancias):
    """Resuelve el problema del viajante usando OR-Tools."""
    gerente = pywrapcp.RoutingIndexManager(len(matriz_distancias), 1, 0)  # Un solo vehículo, comienza en 0
    modelo = pywrapcp.RoutingModel(gerente)

    def distancia_callback(desde_idx, hasta_idx):
        return matriz_distancias[gerente.IndexToNode(desde_idx)][gerente.IndexToNode(hasta_idx)]
    
    indice_transito = modelo.RegisterTransitCallback(distancia_callback)
    modelo.SetArcCostEvaluatorOfAllVehicles(indice_transito)

    parametros_busqueda = pywrapcp.DefaultRoutingSearchParameters()
    parametros_busqueda.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

    solucion = modelo.SolveWithParameters(parametros_busqueda)
    
    if solucion:
        indice = modelo.Start(0)
        ruta = []
        distancia_total = 0
        while not modelo.IsEnd(indice):
            ruta.append(gerente.IndexToNode(indice))
            siguiente_indice = solucion.Value(modelo.NextVar(indice))
            distancia_total += matriz_distancias[gerente.IndexToNode(indice)][gerente.IndexToNode(siguiente_indice)]
            indice = siguiente_indice
        ruta.append(gerente.IndexToNode(indice))
        return ruta, distancia_total
    return None, None


def TSP(driver):
    print("Bienvenido")
    valor_a_optimizar = input("¿Qué desea optimizar? (distancia, tiempo, costo): ")
    if valor_a_optimizar == "tiempo":
        valor_a_optimizar = "tiempo_mins"

    notValid = True
    while notValid:
        almacen = input("Ingrese el almacén de donde partirá el camión: ")
        try:
            almacen = int(almacen)
            almacen = "Almacen "+str(almacen)
        except:
            pass
        print(almacen)
        al = readAlmacen(driver, almacen)
        # Revisar si TipoAlmacen es "Almacen Despacho"

        if dict(al[0][0]["a"])['TipoAlmacen'] != "Almacen Despacho":
            print("El almacén ingresado no es un almacén de despacho.")
            continue
        notValid = False
        

    tiendas_en_ruta = []
    while True:
        tienda = int(input("Ingrese la siguiente tienda en la ruta: "))
        tiendas_en_ruta.append("Tienda "+str(tienda))
        if input("¿Desea ingresar otra tienda? (s/n): ").lower() == "n":
            break

    #print("Almacén:", almacen)
    print("Procediendo a calcular ruta óptima...")

    query_almacen = f"""
        MATCH (a:Almacén)-[r:DISTANCIA]->(t: Tienda)
        WHERE a.Nombre = "{almacen}" AND t.Nombre IN {tiendas_en_ruta}
        RETURN r.{valor_a_optimizar} AS Valor, t.Nombre AS Destino
    """
    result = driver.execute_query(query_almacen)

    # Convert to list of lists
    relacion_almacen_tienda = [[almacen, record[1], record[0]] for record in result[0]]

    relacion_tienda_tienda = []
    for i in range(len(tiendas_en_ruta)):
        for j in range(len(tiendas_en_ruta)):
                if i != j:
                        query_tienda = f"""
                        MATCH (t1)-[r:DISTANCIA_TIENDA]->(t2)
                        WHERE t1.Nombre = "{tiendas_en_ruta[i]}" AND t2.Nombre = "{tiendas_en_ruta[j]}"
                        RETURN r.{valor_a_optimizar} AS Valor, t1.Nombre AS Origen, t2.Nombre AS Destino
                        """
                        result = driver.execute_query(query_tienda)
                        #print(result[0][0])
                        relacion_tienda_tienda.append([result[0][0][1], result[0][0][2], result[0][0][0]])

    #print(relacion_almacen_tienda)
    #print(almacen, tiendas_en_ruta)
    #print(relacion_tienda_tienda)
    matriz_distancias, indice_mapa = crear_matriz_distancias(almacen, relacion_almacen_tienda, relacion_tienda_tienda)

    #print(matriz_distancias)
    #print(indice_mapa)
    ruta_optima, valor_total = resolver_tsp(matriz_distancias)

# Imprimir resultado
    if ruta_optima:
        ubicaciones = list(indice_mapa.keys())
        print("Ruta óptima:", " -> ".join(ubicaciones[i] for i in ruta_optima))
        if valor_a_optimizar == "tiempo_mins":
            valor_a_optimizar = "tiempo"
        print(f"{valor_a_optimizar} total: {valor_total}")
    else:
        print("No se encontró una solución.")