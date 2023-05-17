from django.contrib import admin

from irankis.models import Irankis, NuomosFaktas

# from irankis.models import Irankis, NuomosFaktas


class IrankisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'galia', 'pristatymas')


admin.site.register(Irankis, IrankisAdmin)
admin.site.register(NuomosFaktas)


