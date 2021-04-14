from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def if_statement(request):
    login = True
    return render(request,"if_statement.html", context = {'login':login})

def if_else(request):
    login = True
    return render(request,"if_else.html", context = {'login':login,'a':255,'b':45})

def for_loop(request):
    login = True
    return render(request,"for_loop.html",context = {'items':['Apple','Ball','Cat'],'profile':{'name':'Nimish','age':24,'sal':101202000}})
