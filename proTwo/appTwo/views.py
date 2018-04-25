from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return HttpResponse('<em>Hellooooo World!!</em>')

def help(request):
    helpdict = {'help_insert': 'HELPHELPHELP Page'}
    return render(request, 'appTwo/help.html', context=helpdict)
