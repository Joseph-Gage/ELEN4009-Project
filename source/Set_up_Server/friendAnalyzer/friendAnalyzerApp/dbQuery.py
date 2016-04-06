from py2neo import Graph, authenticate
import json

def getPerson(name, surname):
	graph = Graph()
	authenticate('localhost:7474', 'neo4j', 'nathan3j')
	result = {"nodes":[],"links":[]}

	query = "MATCH (p {name:{N}, surname:{S}}) RETURN ID(p) AS id, p.name AS name, p.surname AS surname, p.age AS age, p.occupation AS occupation, p.img_url AS img_url"

	record = graph.cypher.execute(query, {"N":name,"S":surname})[0]
	result["nodes"].append({"id":record.id,"name":str(record.name),"surname":str(record.surname),"age":record.age,"occupation":str(record.occupation),"img_url":str(record.img_url)})

	return result

def getFriendNetwork(name, surname):
	graph = Graph()
	authenticate('localhost:7474', 'neo4j', 'nathan3j')
	result = getPerson(name, surname)		

	query = "MATCH (p {name:{N}, surname:{S}})-[r]-(f) RETURN r, f, ID(f) AS idf, ID(p) AS idp"

	for record in graph.cypher.execute(query, {"N":name,"S":surname}):
		result["nodes"].append({"id":record.idf,"name":str(record.f["name"]),"surname":str(record.f["surname"]),"age":record.f["age"],"occupation":str(record.f["occupation"]), "img_url":str(record.f["img_url"])})
		result["links"].append({"source":record.idp, "target":record.idf, "since":str(record.r["since"]), "type":str(record.r.type), "level":str(record.r["level"])})
	
	result["nodes"] = {v['id']:v for v in result["nodes"]}.values()
	return result

def getFoFNetwork(name, surname):
	graph = Graph()
	authenticate('localhost:7474', 'neo4j', 'nathan3j')	
	result = getFriendNetwork(name, surname)

	query = "MATCH (p {name:{N}, surname:{S}})-[]-(f)-[r]-(ff) RETURN r, ff, ID(f) AS idf, ID(ff) AS idff"

	for record in graph.cypher.execute(query, {"N":name,"S":surname}):
		result["nodes"].append({"id":record.idff,"name":str(record.ff["name"]),"surname":str(record.ff["surname"]),"age":record.ff["age"],"occupation":str(record.ff["occupation"]), "img_url":str(record.ff["img_url"])})
		result["links"].append({"source":record.idf, "target":record.idff, "since":str(record.r["since"]), "type":str(record.r.type), "level":str(record.r["level"])})
	
	result["nodes"] = {v['id']:v for v in result["nodes"]}.values()
	return result


#result = getFoFNetwork("James", "Allingham")
#print(json.dumps(result, indent=4, sort_keys=True))