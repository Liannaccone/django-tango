from django.shortcuts import render
from django.http import HttpResponse
from appTwo.models import User
# Create your views here.
def index(request):
    return HttpResponse('<em>Hellooooo World!!</em>')

def user_listing(request):
    user_list = User.objects.order_by('last_name')
    user_dict = {'users': user_list}
    return render(request, 'appTwo/user.html', context=user_dict)

def help(request):
    helpdict = {'help_insert': 'HELPHELPHELP Page'}
    return render(request, 'appTwo/help.html', context=helpdict)
