#from graphdatascience import GraphDataScience
from neo4j import GraphDatabase

NEO4J_URI='neo4j+s://33397770.databases.neo4j.io'
NEO4J_USERNAME='neo4j'
NEO4J_PASSWORD='wnHpVYT3KweYDd5zzThQ2sVQO_XKtI7jDVuKvfTsETY'
AURA_INSTANCEID=33397770
AURA_INSTANCENAME='Instance01'

#gds = GraphDataScience(NEO4J_URI,auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

#print(gds.server_version())
#assert gds.server_version()
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))


def first_query(tx):
    tx.run("CALL gds.aura.context.store();")


def generate_graph(tx):
    query = """
    MATCH (a: Almacén)-[r:DISTANCIA]->(t: Tienda)
    RETURN gds.graph.project(
    'Conexiones',
    a,
    t,
    { relationshipProperties: r { .tiempo_mins} }
    )
    """
    tx.run(query)
def dijkstra(tx, start, end):
    query = """
    CALL gds.alpha.shortestPath.dijkstra.stream({
      nodeProjection: 'Person',
      relationshipProjection: {
        KNOWS: {
          type: 'KNOWS',
          properties: 'weight',
          orientation: 'UNDIRECTED'
        }
      },
      startNode: $start,
      endNode: $end,
      relationshipWeightProperty: 'weight'
    })
    YIELD nodeId, cost
    RETURN gds.util.asNode(nodeId).name AS name, cost
    """
    return tx.run(query, start=start, end=end)

with driver.session() as session:
    session.execute_write(first_query)
    session.execute_write(generate_graph)

driver.close()
