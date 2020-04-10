from django.http import HttpResponse
#import loader to use with template
from django.template import loader

#import render shortcut in django
from django.shortcuts import get_object_or_404, render

#import Http Error 404
from django.http import Http404

from .models import Prozessor, GPU

def index(request):
    return HttpResponse("Welcome to the PC shop site.")

def ProzessorView(request):
    proz_list = Prozessor.objects.all()
    context = {'proz_list': proz_list}
    return render(request, 'pcshop/prozessor.html', context)

def GPUView(request):
    try:
        gpu_list = GPU.objects.all()
        context = {'gpu_list': gpu_list}
    except GPU.DoesNotExist:
        raise Http404("No GPU")
    return render(request, 'pcshop/gpu.html', context)

def MainboardView(request):
    return HttpResponse("Mainboard")

def RAMView(request):
    return HttpResponse("RAM")

def SSDView(request):
    return HttpResponse("SSD")
