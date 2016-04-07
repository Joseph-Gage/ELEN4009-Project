from django.shortcuts import render_to_response 
from django.http import HttpResponse
import dbQuery as db
import json

#Function For each view:
def home(request):
	return render_to_response("/var/www/friendAnalyzer/friendAnalyzerApp/templates/home.html")

def friendNetwork(request):
	content = {"FriendGraph": json.dumps(db.getFoFNetwork("Joseph", "Gage"))}
	return render_to_response("/var/www/friendAnalyzer/friendAnalyzerApp/templates/test.html",content)

	# 