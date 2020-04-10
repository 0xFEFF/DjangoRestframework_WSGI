from django.db import models

# Create your models here.
class Prozessor(models.Model):
    Serie = models.CharField(max_length=50)
    Modell = models.CharField(max_length=50)
    Codename = models.CharField(max_length=50)
    Kerne = models.IntegerField(default=0)
    Threads = models.IntegerField(default=0)
    Prozessortakt = models.FloatField(default=0.0)
    Turbotakt = models.FloatField(default=0.0)

    def __str__(self):
        return self.Serie + ' ' + self.Modell

class RAM(models.Model):
    Modellname = models.CharField(max_length=50)
    Gesamtkapazitaet = models.IntegerField(default=0)
    Modulanzahl = models.IntegerField(default=0)
    Speicherart = models.CharField(max_length=30)
    Speichertyp = models.CharField(max_length=20)
    Bauform = models.CharField(max_length=10)

    def __str__(self):
        return self.Modellname + ' ' + self.Gesamtkapazitaet

class GPU(models.Model):
    Name = models.CharField(max_length=50)
    Hersteller = models.CharField(max_length=50)
    Grafikprozessor = models.CharField(max_length=20)

    def __str__(self):
        return self.Name + ' ' + self.Hersteller

class Mainboard(models.Model):
    Modell = models.CharField(max_length=50)
    Sockel = models.CharField(max_length=20)
    Chipsatz = models.CharField(max_length=20)
    Formfaktor = models.CharField(max_length=20) 
    RAM_Typ = models.CharField(max_length=20)
    RAM_Bauform = models.CharField(max_length=20)
    RAM_Architektur = models.CharField(max_length=20)
    RAM_Einzelmodul = models.IntegerField(default=0)
    BIOS = models.CharField(max_length=20)

    def __str__(self):
        return self.Modell + ' ' + self.Sockel

class SSD(models.Model):
    Hersteller = models.CharField(max_length=50)
    Modellserie = models.CharField(max_length=50)
    Kapazität = models.IntegerField(default=0)
    Lesegeschw = models.IntegerField(default=0)
    Schreibgeschw = models.IntegerField(default=0)

    def __str__(self):
        return self.Hersteller + ' ' + self.Modellserie

#class HDD(models.Model):

#class Gehaeuse(models.Model):

#class Netzteil(models.Model):