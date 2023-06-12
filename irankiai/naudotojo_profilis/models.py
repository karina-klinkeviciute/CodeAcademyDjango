from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class NaudotojoProfilis(models.Model):
    naudotojas = models.ForeignKey(User, on_delete=models.CASCADE)
    ivertinimas = models.IntegerField()

    def visi_irankiai(self):
        return ', '.join(irankis.pavadinimas for irankis in self.irankis_set.all()[:3])

    visi_irankiai.short_description = "Įrankiai"

    def __str__(self):
        return f"{self.naudotojas.first_name} {self.naudotojas.last_name}"

    # todo pridėti funkciją "dabar išsinuomoti įrankiai"
    # todo pridėti funkciją "visi_nuomoti_irankiai"

