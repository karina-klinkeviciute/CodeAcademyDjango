import uuid as uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Naudotojas(AbstractUser):

    # kadangi norim, kad naudotojas jungtųsi ne su naudotojo vardu (username),
    # bet su el. paštu (email), t.t. el. paštas naudojamas naudotojo identifikavimui,
    # todėl email pas kiekvieną naudotoją turi būti skirtingas.
    # Standartiniam naudotojo modely, ir AbstractUser modely jis nėra unikalus.
    # Todėl reikia perrašyti email lauką ir nurodyti, kad jis privalo būti unikalus, t.y. nesikartoti.
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )

    # Tam, kad naudotojo ID neitų iš eiles, t.y. nebūtų 1, 2, 3... mums reikia pridėti savo id lauką,
    # kuris būtų UUID formatu. Čia reikia naudoti UUID4 variantą.
    # Šis laukas turi būti nustatytas kai Primary Key.
    # Taip pat jis turi turėti numatytąją reikšmę uuid.uuid4,
    # kas reiškia, kad bus sugeneruota nauja atsitiktinė UUID4 reikšmė
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ivertinimas = models.IntegerField(null=True, blank=True)
    miestas = models.CharField(max_length=255, null=True, blank=True)

    # Kadangi naudotojo vardas mums nebėra aktualus, reikia perrašyti jo lauką.
    # Klasėje AbstractUser jis yra privalomas ir unikalus. Mums dabar tai tik trukdys.
    # Todėl reikia iš naujo mūsų modelyje aprašyti šį lauką, kad galėtume padaryti jį neunikaliu,
    # o taip pat, kad galėtume leisti, kad jis būtų tuščias.
    username = models.CharField(
        'username',
        max_length=1000,
        # unique=False,
        # help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
        # validators=[username_validator],
        # error_messages={
        #     'unique': _("A user with that username already exists."),
        # },
        null=True,
        blank=True
    )

    # Reikia pakeisti ir model manager mūsų naujam naudotojo modeliui.
    # Tai reikia padaryti todėl, kad model manager šiuo atveju rūpinasi naudotojų sukūrimu
    # Pas mus nauotojų kūrimas pasikeitė, nes nebenaudojam username lauko identifikacijai,
    # o naudojam email lauką.
    objects = MyUserManager()

    # Tam, kad naudotojas galėtų jungtis su el. paštu, o ne username, reikia nurodyti,
    # kad laukas, pagal kurį naudotojas bus identifikuojamas, yra email
    USERNAME_FIELD = "email"

    # Tėvinėje klasėje AbstractUser email buvo nurodytas, kaip required field.
    # Bet kai jį padarėm, kad jis būtų USERNAME_FIELD, tada jis savaime tapo privalomas (required).
    # Tokiu atveju jis dubliuojasi. Kad nesidubliuotų, reikia perrašyti atributą REQUIRED_FIELDS taip,
    # kad jame nebūtų email lauko.
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

class NaudotojoProfilis(models.Model):
    naudotojas = models.ForeignKey(Naudotojas, on_delete=models.CASCADE)
    ivertinimas = models.IntegerField(null=True, blank=True)

    def visi_irankiai(self):
        return ', '.join(irankis.name for irankis in self.irankis_set.all()[:3])

    visi_irankiai.short_description = "Įrankiai"

    def __str__(self):
        return f"{self.naudotojas.first_name} {self.naudotojas.last_name}"

    # todo pridėti funkciją "dabar išsinuomoti įrankiai"
    # todo pridėti funkciją "visi_nuomoti_irankiai"

