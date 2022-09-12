from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Team

# Create your views here.
def index(request):
    return HttpResponse('<h1>Super SentAPI</h1>')

def get_teams(request):
    teams = Team.objects.all().values()
    return JsonResponse({"teams": list(teams)})