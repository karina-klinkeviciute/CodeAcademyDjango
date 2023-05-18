from django.db import models


class Kategorija(models.Model):
    pavadinimas = models.CharField(max_length=255)

    def __str__(self):
        return self.pavadinimas

class Irankis(models.Model):
    pavadinimas = models.CharField(max_length=255)
    aprasymas = models.TextField(blank=True, null=True)
    galia = models.IntegerField(blank=True, null=True)
    pristatymas = models.BooleanField()
    kategorijos = models.ManyToManyField(Kategorija)

    def rodyti_kategorijas(self):
        return ', '.join(kategorija.pavadinimas for kategorija in self.kategorijos.all()[:3])

    class Meta:
        verbose_name = "Įrankis"
        verbose_name_plural = "Įrankiai"

    def __str__(self):
        return self.pavadinimas

class IrankioVienetas(models.Model):
    irankis = models.ForeignKey(Irankis, on_delete=models.CASCADE)
    akumuliatoriaus_talpa = models.IntegerField(blank=True, null=True)
    vietove = models.CharField(max_length=255)
    QR_kodas = models.CharField(max_length=255)
    ar_isnuomotas = models.BooleanField(default=False)

class NuomosFaktas(models.Model):
    irankio_vienetas = models.ForeignKey(IrankioVienetas, on_delete=models.SET_NULL, blank=True, null=True)
    pastabos = models.TextField()

    class Meta:
        verbose_name = "Nuomos faktas"
        verbose_name_plural = "Nuomos faktai"
