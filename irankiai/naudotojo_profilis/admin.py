from django.contrib import admin

from naudotojo_profilis.models import NaudotojoProfilis

class NaudotojoProfilisAdmin(admin.ModelAdmin):
    list_display = ('ivertinimas', 'visi_irankiai')

# Register your models here.
admin.site.register(NaudotojoProfilis, NaudotojoProfilisAdmin)

