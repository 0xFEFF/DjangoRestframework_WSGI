from rest_framework import serializers

from .models import Prozessor, GPU, RAM, SSD, Mainboard

class ProzessorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Prozessor
        fields = ['Serie', 'Modell', 'Codename', 'Kerne', 'Threads', 'Prozessortakt', 'Turbotakt']

class GPUSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GPU
        fields = [ 'Name', 'Hersteller', 'Grafikprozessor']

class RAMSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = RAM
        fields = ['Modellname', 'Gesamtkapazitaet', 'Modulanzahl', 'Speicherart', 'Speichertyp', 'Bauform']

class SSDSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SSD
        fields = ['Hersteller', 'Modellserie', 'Kapazität', 'Lesegeschw', 'Schreibgeschw']

class MainboardSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Mainboard
        fields = ['Modell', 'Sockel', 'Chipsatz', 'Formfaktor', 'RAM_Typ', 'RAM_Bauform', 'RAM_Architektur', 'RAM_Einzelmodul', 'BIOS']