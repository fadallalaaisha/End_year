from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def products(request):
    return render(request, 'products.html')    

def machines(request):
    return render(request,'machines.html')


def about(request):
    return render(request,'about.html')    

def read(request):
    return render(request,'read.html')      