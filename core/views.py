from django.shortcuts import render, HttpResponse

# Create your views here.
def hello(request, nome, idade):
    return HttpResponse('<h1>Hello {} de {} anos!</h1>'.format(nome, idade))

def add(request, a, b):
    return HttpResponse('<h1>{} + {} = {}</h1>'.format(a, b, a+b))