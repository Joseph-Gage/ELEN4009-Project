from py2neo import Graph, Path, authenticate
graph = Graph()
authenticate("localhost:7474", "neo4j", "nathan3j")
tx = graph.cypher.begin()
names = ["Alice", "Bob", "Carol"]
for name in names:
    tx.append("CREATE (person:Person {name:{name}}) RETURN person", name=name)
test = [result.one for result in tx.commit()]
alice = test[0]
bob = test[1]
carol = test[2]

friends = Path(alice, "KNOWS", bob, "KNOWS", carol)
graph.create(friends)
print(alice["name"]) 
print(friends)

for name in names:
	print(graph.cypher.execute("MATCH (a) WHERE a.name={x} RETURN a", {"x":name}))
