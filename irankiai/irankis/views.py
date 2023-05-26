from django.shortcuts import render
from django.views.generic import ListView, DetailView

from irankis.models import Irankis, IrankioVienetas


# Create your views here.
def index(request):

    # suskai2iuojam reikiamus duomenis
    irankiu_kiekis = Irankis.objects.count()
    irankiu_vienetu_kiekis = IrankioVienetas.objects.count()


    # į šabloną turi b8ti paduodamas žodynas su duomenimmis
    context = {
        "irankiu_kiekis": irankiu_kiekis,
        "irankiu_vienetu_kiekis": irankiu_vienetu_kiekis
    }

    # žodynas su duomenimis per kintamąjį context sujungiamas su šablonu index ir grąžinamas į naršyklę
    return render(request, "index.html", context=context)


class IrankiaiView(ListView):
    model = Irankis
    template_name = "irankiai.html"

    # jei norim, kad grąžintų tik išfiltruotus (šiuo atveju tik tuos, kurie turi pristatymą):
    # queryset = Irankis.objects.filter(pristatymas=True)

    def get_queryset(self):

        # čia galimi papildomi veiksmai

        return Irankis.objects.filter(pristatymas=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["papildoma_informacija"] = "tiesiog bet koks tekstas"

        return context
class IrankisView(DetailView):
    model = Irankis
    template_name = "irankis.html"
