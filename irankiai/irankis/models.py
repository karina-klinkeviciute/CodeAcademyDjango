from django.contrib import admin
from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _

from naudotojo_profilis.models import NaudotojoProfilis, Naudotojas


class Kategorija(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    def __str__(self):
        return self.name

class Irankis(models.Model):
    name = models.CharField(verbose_name=_("name"), max_length=255)

    # verbose name leidžia rašyti aiškesnius vartotojui rodomus laukų pavadinimus
    description = models.TextField(verbose_name=_("description"), blank=True, null=True)

    # taip pat galima verbose_name nusiųsti vertimui
    power = models.IntegerField(verbose_name=_("power of electric tool"), blank=True, null=True)


    delivery = models.BooleanField(verbose_name=_("delivery"))
    kategorijos = models.ManyToManyField(Kategorija)
    naudotojas = models.ForeignKey(NaudotojoProfilis, on_delete=models.CASCADE)
    nuotrauka = models.ImageField(upload_to="irankis", null=True, blank=True)


    # parašom funkciją, kuri atrenka pirmas tris kategorijas. Paskui ją naudosim Admin'e, kad ten galėtume parodyti
    # šituos dalykus sąraše
    def rodyti_kategorijas(self):
        return ', '.join(kategorija.name for kategorija in self.kategorijos.all()[:3])

    @admin.display(ordering='naudotojo_duomenys', description='Naudotojo duomenys')
    def get_naudotojo_vardas_pavarde(self):
        return f"{self.naudotojas.naudotojas.first_name} {self.naudotojas.naudotojas.last_name}"

    class Meta:

        # kad rodytų tvarkingus lietuviškus pavadinimus
        verbose_name = "Įrankis"
        verbose_name_plural = "Įrankiai"

    # kad admin aplinkoje (ir kitur) rodytų tvarkingai daikto pavadinimą, o ne "Irankisobject1" ar panašiai
    def __str__(self):
        return self.name

    # todo parašyti metodą "irankio_vienetu_kiekis"

    @property
    def laisvi_irankiai_count(self):
        laisvi = self.irankiovienetas_set.filter(ar_isnuomotas=False).count()
        return laisvi

    # todo parašyti metodą, kuris tikrintų, ar konkrečiam laikotarpiui šį įrankį galima išsinuomoti
    def ar_laisvas(self, dat_nuo, data_iki):
        raise NotImplementedError

class IrankioAtsiliepimas(models.Model):
    irankis = models.ForeignKey(Irankis, on_delete=models.CASCADE, blank=True, null=True)
    naudotojas = models.ForeignKey(Naudotojas, on_delete=models.CASCADE, blank=True, null=True)
    atsiliepimas = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Atsiliepimas"
        verbose_name_plural = 'Atsiliepimai'
        ordering = ['-date_created']

class IrankioVienetas(models.Model):
    # class VietoveChoices(models.TextChoices):
    #     KAUNAS = "kaunas", _("Kaunas")
    #     VILNIUS = "vilnius", _("Vilnius")
    #     KLAIPEDA = "klaipeda", _("Klaipėda")
    #     SIAULIAI = "siauliai", _("Šiauliai")
    #     PANEVEZYS = "panevezys", _("Panevėžys")

    irankis = models.ForeignKey(Irankis, on_delete=models.CASCADE)
    akumuliatoriaus_talpa = models.IntegerField(blank=True, null=True)

    # Vietovė galės būti tik iš viršuje nurodytų vietovės pasirinkimų
    # vietove = models.CharField(choices=VietoveChoices, max_length=255)
    QR_kodas = models.CharField(max_length=255)
    ar_isnuomotas = models.BooleanField(default=False)

    # todo ar_isnuomotas tikrinimą pagal nuomos faktus

    def __str__(self):
        return f"{self.irankis.name} - {self.QR_kodas}"

class NuomosFaktas(models.Model):
    irankio_vienetas = models.ForeignKey(IrankioVienetas, on_delete=models.SET_NULL, blank=True, null=True)
    pastabos = models.TextField()
    nuomotojas = models.ForeignKey(NaudotojoProfilis, on_delete=models.CASCADE, related_name="nuomotojo_nuomos_faktai")
    nuomininkas = models.ForeignKey(NaudotojoProfilis, on_delete=models.CASCADE, related_name="nuomininko_nuomos_faktai")
    # todo prideti lauka nuomos_pradzia
    # todo prideti lauka nuomos_pabaiga

    class Meta:
        verbose_name = "Nuomos faktas"
        verbose_name_plural = "Nuomos faktai"

    # todo pridėti metodą, kad suskaičiuotų nuomos ilgį valandomis/dienomis

    # todo pridėti metodą, kuris skaičiuotų kainą

    # todo pakeisti save metodą taip, kad kai išsaugojam nuomos faktą,
    #  email nusiųstų pranešimą nuomotojui (gal ir nuomoninkui irgi)

