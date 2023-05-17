from django.db import models


class Kategorija(models.Model):
    pavadinimas = models.CharField(max_length=255)


class Irankis(models.Model):
    pavadinimas = models.CharField(max_length=255)
    aprasymas = models.TextField(blank=True, null=True)
    galia = models.IntegerField(blank=True, null=True)
    pristatymas = models.BooleanField()
    kategorijos = models.ManyToManyField(Kategorija)

    class Meta:
        verbose_name = "Įrankis"
        verbose_name_plural = "Įrankiai"


class NuomosFaktas(models.Model):
    irankis = models.ForeignKey(Irankis, on_delete=models.SET_NULL, blank=True, null=True)
    pastabos = models.TextField()

    class Meta:
        verbose_name = "Nuomos faktas"
        verbose_name_plural = "Nuomos faktai"
