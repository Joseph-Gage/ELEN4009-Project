# dbQuery.py
# Author: James Allingham
# Date: 29 March 2016

# Import appropriate py2neo modules
from py2neo import Graph, authenticate
# Import json module
import json

# function to get find a person in the Graph db by their name and surname
# inputs: name and surname - strings representing the name and surname of the person to find
# returns: a json object containing the node of the person if they are in the bd, otherwise containing nothing
def getPerson(name, surname):
	# create a Graph object to represent the db
	graph = Graph()
	# connect the the db at the given location using the following user name and password
	authenticate('localhost:7474', 'neo4j', 'nathan3j')
	# create a doctionary to return. This contains both a list of nodes and a list of links which will be used in other functions
	result = {"nodes":[],"links":[]}

	# generate the query to find the person and return their details
	# the {N} and {S} are parameters
	query = "MATCH (p {name:{N}, surname:{S}}) RETURN ID(p) AS id, p.name AS name, p.surname AS surname, p.age AS age, p.occupation AS occupation, p.img_url AS img_url"

	# execute the query using the parameters passed to the function
	record = graph.cypher.execute(query, {"N":name,"S":surname})[0]
	# add the returned data to the list of nodes in the dictionary
	result["nodes"].append({"id":record.id,"name":str(record.name),"surname":str(record.surname),"age":record.age,"occupation":str(record.occupation),"img_url":str(record.img_url)})

	# return the dictionary
	return result

# function to get find a person and their friends in the Graph db
# inputs: name and surname - strings representing the name and surname of the person to find
# returns: a json object containing the nodes of the people and the links joining them
def getFriendNetwork(name, surname):
	# create a Graph object to represent the db
	graph = Graph()
	# connect the the db at the given location using the following user name and password
	authenticate('localhost:7474', 'neo4j', 'nathan3j')
	# call the getPerson() function to get the information of the person whose network is being found
	result = getPerson(name, surname)		

	# generate the query to find the person, their relationships to other people then return the information about the relationships and the people they are related to
	# the {N} and {S} are parameters
	query = "MATCH (p {name:{N}, surname:{S}})-[r]-(f) RETURN r, f, ID(f) AS idf, ID(p) AS idp"

	# execute the query and then for each returned result
	for record in graph.cypher.execute(query, {"N":name,"S":surname}):
		# add the people to the nodes list in the result dictionary
		result["nodes"].append({"id":record.idf,"name":str(record.f["name"]),"surname":str(record.f["surname"]),"age":record.f["age"],"occupation":str(record.f["occupation"]), "img_url":str(record.f["img_url"])})
		# add the relationships to the links list in the result dictionary
		result["links"].append({"source":record.idp, "target":record.idf, "since":str(record.r["since"]), "type":str(record.r.type), "level":str(record.r["level"])})
	
	# remove duplicate nodes
	result["nodes"] = {v['id']:v for v in result["nodes"]}.values()
	# return the result dictionary
	return result

# function to get find a person, their friends and the friends of their friends in the Graph db
# inputs: name and surname - strings representing the name and surname of the person to find
# returns: a json object containing the nodes of the people and the links joining them
def getFoFNetwork(name, surname):
	# create a Graph object to represent the db
	graph = Graph()
	# connect the the db at the given location using the following user name and password
	authenticate('localhost:7474', 'neo4j', 'nathan3j')
	# call the getFriendNetwork() function to get the person and their friends' data as well as the links
	result = getFriendNetwork(name, surname)

	# generate the query to find the person, their relationships to other people and those peoples relations to other people then return the information about the relationships and the people they are related to
	# the {N} and {S} are parameters
	query = "MATCH (p {name:{N}, surname:{S}})-[]-(f)-[r]-(ff) RETURN r, ff, ID(f) AS idf, ID(ff) AS idff"

	# execute the query and then for each returned result
	for record in graph.cypher.execute(query, {"N":name,"S":surname}):
		# add the people to the nodes list in the result dictionary
		result["nodes"].append({"id":record.idff,"name":str(record.ff["name"]),"surname":str(record.ff["surname"]),"age":record.ff["age"],"occupation":str(record.ff["occupation"]), "img_url":str(record.ff["img_url"])})
		# add the relationships to the links list in the result dictionary
		result["links"].append({"source":record.idf, "target":record.idff, "since":str(record.r["since"]), "type":str(record.r.type), "level":str(record.r["level"])})
	
	# remove duplicate nodes
	result["nodes"] = {v['id']:v for v in result["nodes"]}.values()
	# return the result dictionary
	return result

# The following lines of code can be used for testing
# result = getFoFNetwork("James", "Allingham")
# print(json.dumps(result, indent=4, sort_keys=True))