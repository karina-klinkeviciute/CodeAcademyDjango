from django.contrib import admin

from naudotojo_profilis.models import NaudotojoProfilis

class NaudotojoProfilisAdmin(admin.ModelAdmin):
    list_display = ('ivertinimas', 'rodyti_irankius')

# Register your models here.
admin.site.register(NaudotojoProfilis, NaudotojoProfilisAdmin)

