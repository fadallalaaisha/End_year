from django.shortcuts import render

def display_base(request):
    return render(request,'navbar.html',{})