from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

app_name = 'pcshop'

urlpatterns = [
    path('', views.index, name='index'),
    path('prozessor/', views.ProzessorView, name='prozessor'),
    #path('gpu/', views.GPUView, name='gpu'),
    #path('mainboard/', views.MainboardView, name='mainboard'),
    #path('ram/', views.RAMView, name='ram'),
    #path('ssd/', views.SSDView, name='ssd'),
    #path('<int:name>/possible', views.bla, name=''),
]

urlpatterns = format_suffix_patterns(urlpatterns)