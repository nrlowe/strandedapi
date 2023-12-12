from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test (request) :
 
    # This will return Hello Geeks
    # string as HttpResponse
    return HttpResponse("Hello, welcome to Stranded")