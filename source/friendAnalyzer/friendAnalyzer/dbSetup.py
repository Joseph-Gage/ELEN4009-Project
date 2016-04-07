# coding: utf-8
# dbQuery.py
# Author: James Allingham
# Date: 29 March 2016

# Import appropriate py2neo modules
from py2neo import Graph, authenticate
# create a Graph object to represent the db
graph = Graph()
# connect the the db at the given location using the following user name and password
authenticate('localhost:7474', 'neo4j', 'nathan3j')

# remove any old data in the graph
graph.delete_all()

# create a list of people to be added to the database. py2neo has the ability to cast dictionaries to Neo4j nodes.
people = [{"name":"Paul", "surname":"Cresswell", "img_url":"/static/images/paul.jpg"},{"name": "James", "surname":"Allingham", "age":21, "occupation":"Student", "img_url":"/static/images/james.jpg"}, {"name":"Julian", "surname":"Zeegers", "age":21, "occupation":"Data Scientist","img_url":"/static/images/julz.jpg"}, {"name":"Joseph", "surname":"Gage", "age":22, "img_url":"/static/images/joe.jpg"} , {"name":"Nathan", "surname":"Haag", "img_url":"/static/images/nathan.jpg"}, {"name":"Sasha", "surname":"Naidoo", "age":"22", "img_url":"/static/images/sasha.jpg"}]

# for each person add a node to the graph
for person in people:
	# create a query that will add the person to the graph.
	# {params} is a parameter
	query = "CREATE (person:Person {params}) RETURN person"
	# execure the query using the person as the parameter
	graph.cypher.execute(query, params=person)

# add some relationships
for person_a, rel, person_b, rel_params in [("Julian", "FRIENDS_WITH", "Nathan", {"since":2009}), ("Joseph", "FRIENDS_WITH", "Nathan", {"since":2005}), ("Paul", "FRIENDS_WITH", "James", {"since":2013}), ("Paul", "FRIENDS_WITH", "Julian", {"since":2013}), ("Julian", "FRIENDS_WITH", "James", {"since":2013}), ("Joseph", "FRIENDS_WITH", "James", {"since":2013}), ("Sasha", "IN_RELATIONSHIP_WITH", "James", {"since":2015,"level":"dating"}), ("Sasha", "FRIENDS_WITH", "James", {"since":2014}), ("Sasha", "FRIENDS_WITH", "Paul", {"since":2014,"level":"annoying"})]:
	# create a query that will add the relationship to the graph.
	# {A}, {B}, <<relationship>> and {params} are parameters
	query = "MATCH (a {name:{A}}), (b {name:{B}}) CREATE (a)-[:«relationship»{params}]->(b)"
	# execure the query using the peoples names for {A} and {B}, the type of <<relationship>> for relationship and the information about the relationship as {params}
	graph.cypher.execute(query, {"A": person_a, "B": person_b, "relationship": rel, "params": rel_params})