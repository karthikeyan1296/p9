from django.shortcuts import render
from django.http import HttpResponse


def trail(request):
    return HttpResponse("<h1>Project is on air</h1>")

def base(request):
    return render(request,"base.html")

def home(request):
    return render(request,"rsk/home.html")

def profile(request):
    name="karthi"
    return render(request,"rsk/profile.html",{'name':name})