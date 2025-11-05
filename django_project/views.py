from django.shortcuts import render
from django.http import HttpResponse

def salom_beruvchi(request):
     return HttpResponse("Assalomu aleykum boy ota")


def mamlakat(request):
    return HttpResponse("O'zbekiston Respublikasi")

def viloyat(request):
    return HttpResponse("O'zbekiston Respublikasi Surhandaryo viloyati")

def shahar(request):
    return HttpResponse("O'zbekiston Respublikasi Surhandaryo viloyati Termez shahri")

def akademiya(request):
    return HttpResponse("O'zbekiston Respublikasi Surhandaryo viloyati Termez shahri Joylinks academiya")


