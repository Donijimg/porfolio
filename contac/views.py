from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def contacto(request):
  return HttpResponse ("contacto.html")