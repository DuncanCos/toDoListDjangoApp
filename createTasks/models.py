from django.db import models

# Create your models here.

class tache (models.Model):
    nomDeTache = models.CharField(max_length=255)
    etatTache = models.CharField(max_length=9)

class tacheAFaire (models.Model):
    nomDeTache = models.CharField(max_length=255)

class tacheTerminee (models.Model):
    nomDeTache = models.CharField(max_length=255)