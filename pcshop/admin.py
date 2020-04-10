from django.contrib import admin

# Register your models here.
from .models import Prozessor, RAM, GPU, SSD, Mainboard

admin.site.register(Prozessor)
admin.site.register(RAM)
admin.site.register(GPU)
admin.site.register(SSD)
admin.site.register(Mainboard)
