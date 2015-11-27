from django.shortcuts import render
from django.http import HttpResponse
from .spider import Spider
# Create your views here.

def index(request):
    context = {'b':'test'}

    return render(request, 'mainPage/index.html', context)


def spiderResult(request):
    gogogo = Spider()
    allList = gogogo.letsGo
    return render(request, 'mainPage/tables.html', {'allList':allList})    

