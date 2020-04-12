from django.http import HttpResponse

from .serializers import ProzessorSerializer, GPUSerializer, RAMSerializer, SSDSerializer, MainboardSerializer
from .models import Prozessor, GPU, SSD, RAM, Mainboard

from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, viewsets, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response



#normal views
def index(request):
    return HttpResponse("Welcome to the PC shop site.")

@api_view(['GET', 'POST'])
def ProzessorView(request, format=None):
    #display all processor or create a new one
    if request.method == 'GET':
        prozessor = Prozessor.objects.all()
        serializer = ProzessorSerializer(prozessor, many = True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProzessorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

"""
def GPUView(request):
    

def MainboardView(request):
    return HttpResponse("Mainboard")

def RAMView(request):
    return HttpResponse("RAM")

def SSDView(request):
    return HttpResponse("SSD")
"""

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

