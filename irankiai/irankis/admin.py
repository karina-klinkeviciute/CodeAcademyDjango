from django.contrib import admin

from irankis.models import Irankis, NuomosFaktas, Kategorija, IrankioVienetas, IrankioAtsiliepimas


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
    search_fields = ('vietove', 'irankis__name')


# padarom, kad įrannkio vienetus galima būtų pridėti ir redaguoti pridedant ar redaguojant įrankį
class IrankioVienetasInline(admin.TabularInline):
    model = IrankioVienetas
    extra = 0
    can_delete = False  # jei False, trinti negalima. Jei True - galima. Default - True
    readonly_fields = ('QR_kodas', )  # laukai, kuri7 redaguoti negalima


class IrankisAdmin(admin.ModelAdmin):
    list_display = ('name', 'power', 'delivery', 'rodyti_kategorijas',
                    'get_naudotojo_vardas_pavarde', 'laisvi_irankiai_count')
    list_filter = ('delivery', )
    # čia įdedam viršuje aprašytą "inline", kad galima būtų redaguoti įrankio vienetus kartu su įrankiu
    inlines = [IrankioVienetasInline]
    search_fields = ('name', )
    fields = ('name', 'power', 'delivery', 'laisvi_irankiai_count', 'naudotojas')
    readonly_fields = ('laisvi_irankiai_count', )

class IrankioAtsiliepimasAdmin(admin.ModelAdmin):
    list_display = ('irankis', 'naudotojas', 'date_created')

class KategorijaAdmin(admin.ModelAdmin):
    list_display = ('name', )


admin.site.register(IrankioAtsiliepimas, IrankioAtsiliepimasAdmin)
admin.site.register(IrankioVienetas, IrankioVienetasAdmin)
admin.site.register(Kategorija, KategorijaAdmin)
admin.site.register(Irankis, IrankisAdmin)
admin.site.register(NuomosFaktas)



