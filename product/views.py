from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Count

def index(request):
    return render(request, 'product/index.html',)

def testform(request):
    if request.method == "POST":
        nm=request.POST['name']
        ct=request.POST['category']
        pc=request.POST['price']
        dt=request.POST['details']
        print(nm, ct, dt, pc)

    return render(request, "product/testform.html",)


def username(request):
    if request.method=="POST":
        nm=request.POST['name']
        print(nm)
    return render(request, "product/username.html",)
