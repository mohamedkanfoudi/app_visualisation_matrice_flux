from django.shortcuts import render
from testdb.models import network
# Create your views here.

def shownet(request):
    showall=network.objects.all()
    return render(request,'netall.html',{"data":showall})