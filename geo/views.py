from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")

def  kanto(request):
    return render(request, "kanto.html")

def johto(request):
    return render(request, "johto.html")

def unova(request):
    return render( request, "unova.html")