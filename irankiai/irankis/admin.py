from django.contrib import admin

from irankis.models import Irankis, NuomosFaktas, Kategorija, IrankioVienetas


class IrankioVienetasAdmin(admin.ModelAdmin):

    # įrankių vienetų sąraše rodom šiuos laukus
    list_display = ('irankis', 'akumuliatoriaus_talpa', 'ar_isnuomotas')

    # įrankių vienetų sąrašą galima bus filtruoti pagal šiuos laukus
    list_filter = ('ar_isnuomotas', )

    # šiuos laukus galima redaguoti tiesiogiai
    list_editable = ('akumuliatoriaus_talpa', 'ar_isnuomotas')

    # sugrupuojam informacij1 5 atskirus laukus
    fieldsets = (
        ("Pagrindine informacija", {"fields": ("irankis", "akumuliatoriaus_talpa")}),
        ("Papildoma informacija", {"fields": ("vietove", "QR_kodas", "ar_isnuomotas")})
    )
    # paie6ka 6iuose laukuose. "irankis_pavadinimas" yra lukas ilentelės "įrankis"
    search_fields = ('vietove', 'irankis__pavadinimas')


# padarom, kad įrannkio vienetus galima būtų pridėti ir redaguoti pridedant ar redaguojant įrankį
class IrankioVienetasInline(admin.TabularInline):
    model = IrankioVienetas
    extra = 0
    can_delete = False  # jei False, trinti negalima. Jei True - galima. Default - True
    readonly_fields = ('QR_kodas', )  # laukai, kuri7 redaguoti negalima


class IrankisAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', 'galia', 'pristatymas', 'rodyti_kategorijas', 'get_naudotojo_vardas_pavarde')
    list_filter = ('pristatymas', )
    # 2ia 5dedam vir6uje apra6yt1 "inline", kad galima b8t7 redaguoti 5rankio vienetus kartu su 5rankiu
    inlines = [IrankioVienetasInline]
    search_fields = ('pavadinimas', )

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('pavadinimas', )

admin.site.register(IrankioVienetas, IrankioVienetasAdmin)
admin.site.register(Kategorija, KategorijaAdmin)
admin.site.register(Irankis, IrankisAdmin)
admin.site.register(NuomosFaktas)



