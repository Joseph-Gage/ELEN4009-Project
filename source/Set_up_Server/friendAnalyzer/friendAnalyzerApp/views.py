from django.shortcuts import render_to_response 
from django.http import HttpResponse

#Function For each view:
def home(request):
    return render_to_response("/var/www/friendAnalyzer/friendAnalyzerApp/templates/home.html")