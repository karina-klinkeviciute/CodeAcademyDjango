from django.contrib import admin

from irankis.models import Irankis, NuomosFaktas, Kategorija, IrankioVienetas
from naudotojo_profilis.models import NaudotojoProfilis


# from irankis.models import Irankis, NuomosFaktas





class IrankioVienetasAdmin(admin.ModelAdmin):
    list_display = ('irankis', 'akumuliatoriaus_talpa', 'ar_isnuomotas')
    list_filter = ('ar_isnuomotas', )
    list_editable = ('akumuliatoriaus_talpa', 'ar_isnuomotas')

    fieldsets = (
        ("Pagrindine informacija", {"fields": ("irankis", "akumuliatoriaus_talpa")}),
        ("Papildoma informacija", {"fields": ("vietove", "QR_kodas", "ar_isnuomotas")})
    )
    search_fields = ('vietove', 'irankis__pavadinimas')
class IrankioVienetasInline(admin.TabularInline):
    model = IrankioVienetas
    extra = 0
    can_delete = False
    readonly_fields = ('QR_kodas', )

class IrankisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'galia', 'pristatymas', 'rodyti_kategorijas')
    list_filter = ('pristatymas', )
    inlines = [IrankioVienetasInline]
    search_fields = ('pavadinimas', )

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', )

admin.site.register(IrankioVienetas, IrankioVienetasAdmin)
admin.site.register(Kategorija, KategorijaAdmin)
admin.site.register(Irankis, IrankisAdmin)
admin.site.register(NuomosFaktas)



