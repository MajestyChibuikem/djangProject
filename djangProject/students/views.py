from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


#return a simple http response
def student_view(request):
    return HttpResponse("Hello, this is the student view.")