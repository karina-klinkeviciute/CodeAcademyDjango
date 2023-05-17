from django.contrib import admin

from irankis.models import Irankis, NuomosFaktas, Kategorija


# from irankis.models import Irankis, NuomosFaktas


class IrankisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'galia', 'pristatymas', 'rodyti_kategorijas')
    list_filter = ('pristatymas', )

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', )

admin.site.register(Kategorija, KategorijaAdmin)
admin.site.register(Irankis, IrankisAdmin)
admin.site.register(NuomosFaktas)


