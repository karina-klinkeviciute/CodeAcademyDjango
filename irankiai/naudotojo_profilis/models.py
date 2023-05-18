from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class NaudotojoProfilis(models.Model):
    naudotojas = models.ForeignKey(User, on_delete=models.CASCADE)
    ivertinimas = models.IntegerField()

    def rodyti_irankius(self):
        return ', '.join(irankis.pavadinimas for irankis in self.irankiai_set.all()[:3])

    rodyti_irankius.short_description = "Įrankiai"
