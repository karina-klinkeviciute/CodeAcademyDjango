from django.contrib import admin

from irankis.models import Irankis, NuomosFaktas, Kategorija


# from irankis.models import Irankis, NuomosFaktas


class IrankisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'galia', 'pristatymas', 'rodyti_kategorijas')


admin.site.register(Irankis, IrankisAdmin)
admin.site.register(NuomosFaktas)
admin.site.register(Kategorija)


