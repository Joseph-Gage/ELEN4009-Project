# coding: utf-8
from py2neo import Graph, authenticate
graph = Graph()
authenticate('localhost:7474', 'neo4j', 'nathan3j')

graph.delete_all()

people = [{'name':'Paul', 'surname':'Cresswell', "img_url":"{% static 'images/paul.jpg' %}"},{'name': 'James', 'surname':'Allingham', 'age':21, 'occupation':'Student', "img_url":"{% static 'images/james.jpg' %}"}, {'name':'Julian', 'surname':'Zeegers', 'age':21, 'occupation':'Data Scientist',"img_url":"{% static 'images/jules.jpg' %}"}, {'name':'Joseph', 'surname':'Gage', 'age':22, "img_url":"{% static 'images/joe.jpg' %}"}, {'name':'Nathan', 'surname':'Haag', "img_url":"{% static 'images/nathan.jpg' %}"}, {'name':'Sasha', 'surname':'Naidoo', 'age':'22', "img_url":"{% static 'images/sasha.jpg' %}"}]

# for each person add a node to the graph
for person in people:
	query = "CREATE (person:Person {params}) RETURN person"
	graph.cypher.execute(query, params=person)

# add some relationships
for person_a, rel, person_b, rel_params in [("Julian", "FRIENDS_WITH", "Nathan", {"since":2009}), ("Joseph", "FRIENDS_WITH", "Nathan", {"since":2005}), ("Paul", "FRIENDS_WITH", "James", {"since":2013}), ("Paul", "FRIENDS_WITH", "Julian", {"since":2013}), ("Julian", "FRIENDS_WITH", "James", {"since":2013}), ("Joseph", "FRIENDS_WITH", "James", {"since":2013}), ("Sasha", "IN_RELATIONSHIP_WITH", "James", {"since":2015,"level":"dating"}), ("Sasha", "FRIENDS_WITH", "James", {"since":2014}), ("Sasha", "FRIENDS_WITH", "Paul", {"since":2014,"level":"annoying"})]:
	query = "MATCH (a {name:{A}}), (b {name:{B}}) CREATE (a)-[:«relationship»{params}]->(b)"
	graph.cypher.execute(query, {"A": person_a, "B": person_b, "relationship": rel, "params": rel_params})