from django.db import models

# Create your models here.
class Irankis(models.Model):
    pavadinimas = models.CharField(max_length=255)
    aprasymas = models.TextField(blank=True, null=True)
    galia = models.IntegerField(blank=True, null=True)
    pristatymas = models.BooleanField()

class NuomosFaktas(models.Model):
    irankis = models.ForeignKey(Irankis, on_delete=models.SET_NULL, blank=True, null=True)
    pastabos = models.TextField()


