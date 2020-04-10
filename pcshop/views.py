from django.http import HttpResponse
#import render shortcut in django
from django.shortcuts import get_object_or_404, render

#REST modules
from rest_framework import viewsets, permissions
from .serializers import ProzessorSerializer, GPUSerializer, RAMSerializer, SSDSerializer, MainboardSerializer

from .models import Prozessor, GPU, SSD, RAM, Mainboard

#normal views
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

#REST views
class ProzessorViewSet(viewsets.ModelViewSet):
    #API endpoint
    queryset = Prozessor.objects.all()
    serializer_class = ProzessorSerializer
    permission_classes = [permissions.IsAuthenticated]

class GPUViewSet(viewsets.ModelViewSet):
    #API endpoint
    queryset = GPU.objects.all()
    serializer_class = GPUSerializer
    permission_classes = [permissions.IsAuthenticated]

class SSDViewSet(viewsets.ModelViewSet):
    #API endpoint
    queryset = SSD.objects.all()
    serializer_class = SSDSerializer
    permission_classes = [permissions.IsAuthenticated]

class RAMViewSet(viewsets.ModelViewSet):
    #API endpoint
    queryset = RAM.objects.all()
    serializer_class = RAMSerializer
    permission_classes = [permissions.IsAuthenticated]

class MainboardViewSet(viewsets.ModelViewSet):
    #API endpoint
    queryset = Mainboard.objects.all()
    serializer_class = MainboardSerializer
    permission_classes = [permissions.IsAuthenticated]

