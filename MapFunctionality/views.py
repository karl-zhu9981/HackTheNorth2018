from django.shortcuts import render

def index(request):
    d = {}
    return render(request,'map.html',{})