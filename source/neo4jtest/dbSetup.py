from py2neo import Graph, authenticate
graph = Graph()
authenticate('localhost:7474', 'neo4j', 'nathan3j')

graph.delete_all()

people = [{'name':'Paul', 'surname':'Cresswell'},{'name': 'James', 'surname':'Allingham', 'age':21, 'occupation':'Student'}, {'name':'Julian', 'surname':'Zeegers', 'age':21, 'occupation':'Data Scientist'}, {'name':'Joseph', 'surname':'Gage', 'age':22}, {'name':'Nathan', 'surname':'Haag'}, {'name':'Sasha', 'surname':'Naidoo', 'age':'22'}]

# for each person add a node to the graph
for person in people:
	query = "CREATE (person:Person {params}) RETURN person"
	graph.cypher.execute(query, params=person)

# add some relationships
for person_a, rel, person_b, rel_params in [("James", "FRIENDS_WITH", "Julian", {"since":2013}), ("Julian", "FRIENDS_WITH", "Nathan", {"since":2009}), ("Joseph", "FRIENDS_WITH", "Nathan", {"since":2005}), ("James", "FRIENDS_WITH", "Paul", {"since":2013}), ("Paul", "FRIENDS_WITH", "James", {"since":2013}), ("Paul", "FRIENDS_WITH", "Julian", {"since":2013}), ("Julian", "FRIENDS_WITH", "James", {"since":2013}), ("Joseph", "FRIENDS_WITH", "James", {"since":2013}), ("Sasha", "IN_RELATIONSHIP_WITH", "James", {"since":2015,"type":"dating"}), ("Sasha", "FRIENDS_WITH", "James", {"since":2014}), ("Sasha", "FRIENDS_WITH", "Paul", {"since":2014,"level":"annoying"})]:
	query = "MATCH (a {name:{A}}), (b {name:{B}}) CREATE (a)-[:"+rel+ "{params}]->(b)"
	graph.cypher.execute(query, {"A": person_a, "B": person_b, "relationship": rel, "params": rel_params})