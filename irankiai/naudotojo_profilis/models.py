import uuid as uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import User, AbstractUser
from django.db import models

# Create your models here.


class MyUserManager(BaseUserManager):
    def create_user(self, email, miestas, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            miestas=miestas,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, miestas, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            miestas=miestas,
        )
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class Naudotojas(AbstractUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    ivertinimas = models.IntegerField(null=True, blank=True)
    miestas = models.CharField(max_length=255, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
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

    objects = MyUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["miestas"]

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

