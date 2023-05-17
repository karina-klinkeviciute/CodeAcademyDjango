from django.db import models

# Create your models here.
class Irankis(models.Model):
    pavadinimas = models.CharField(max_length=255)
    aprasymas = models.TextField()
    galia = models.IntegerField()
    pristatymas = models.BooleanField()

class NuomosFaktas(models.Model):
    irankis = models.ForeignKey(Irankis, on_delete=models.SET_NULL)
    pastabos = models.TextField()

