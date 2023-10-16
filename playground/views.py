from django.shortcuts import render
from django.http import HttpResponse

def calculate():
    x = 1 
    y = 2
    z = 3
    return x

def say_hello(request):
    x = calculate()
    y = 2
    return render(request, 'hello.html', { 'name': 'Colter'})
