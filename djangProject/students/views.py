from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.


#return a simple http response
def student_view(request):
    return HttpResponse("Hello, this is the student view.")

def come_inside(request):
    return HttpResponse("welcome inside")

def say_Name(request):
    return HttpResponse("My name is Majesty")

def students(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())

def majesty(request):
    template = loader.get_template("majesty.html")
    return HttpResponse(template.render())

def family(request):
    template = loader.get_template("family.html")
    return HttpResponse(template.render())
