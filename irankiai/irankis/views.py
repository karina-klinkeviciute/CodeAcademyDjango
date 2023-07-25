from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.db.models import Q
from django.views.generic.edit import FormMixin, CreateView

from irankis.forms import AtsiliepimoForma
from irankis.models import Irankis, IrankioVienetas

from django.utils.translation import gettext_lazy as _

# Create your views here.
def index(request):

    # suskaičiuojam reikiamus duomenis
    irankiu_kiekis = Irankis.objects.count()
    irankiu_vienetu_kiekis = IrankioVienetas.objects.count()
    apsilankymu_kiekis = request.session.get("apsilankymai", 0)
    apsilankymu_kiekis += 1
    request.session["apsilankymai"] = apsilankymu_kiekis

    # į šabloną turi būti paduodamas žodynas su duomenimmis
    context = {
        "irankiu_kiekis": irankiu_kiekis,
        "irankiu_vienetu_kiekis": irankiu_vienetu_kiekis,
        "apsilankymai": apsilankymu_kiekis
    }

    # žodynas su duomenimis per kintamąjį context sujungiamas su šablonu index ir grąžinamas į naršyklę
    return render(request, "irankis/index.html", context=context)



def search(request):
    """
    paprasta paieška. query ima informaciją iš paieškos laukelio,
    search_results prafiltruoja pagal įvestą tekstą knygų pavadinimus ir aprašymus.
    Icontains nuo contains skiriasi tuo, kad icontains ignoruoja ar raidės
    didžiosios/mažosios.
    """
    query = request.GET.get('query')
    search_results = Irankis.objects.filter(Q(pavadinimas__icontains=query) | Q(aprasymas__icontains=query))
    return render(request, 'irankis/search.html', {'irankiai': search_results, 'query': query})


class IrankiaiView(ListView):
    model = Irankis
    template_name = "irankis/irankiai.html"
    paginate_by = 3

    # jei norim, kad grąžintų tik išfiltruotus (šiuo atveju tik tuos, kurie turi pristatymą):
    # queryset = Irankis.objects.filter(pristatymas=True)

    # def get_queryset(self):
    #
    #     # čia galimi papildomi veiksmai
    #
    #     return Irankis.objects.filter(pristatymas=True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["papildoma_informacija"] = _("any text")

        return context


class IrankisView(FormMixin, DetailView):
    model = Irankis
    template_name = "irankis/irankis.html"
    form_class = AtsiliepimoForma

    def get_success_url(self):
        return reverse('irankis-detail', kwargs={'pk': self.object.id})

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.instance.irankis = self.object
        form.instance.naudotojas = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):

        laisvu_kiekis = self.object.laisvi_irankiai_count
        if laisvu_kiekis > 0:
            ar_yra_laisvu = True
        else:
            ar_yra_laisvu = False
        data = super().get_context_data()

        data["ar_yra_laisvu"] = ar_yra_laisvu

        return data


class ManoIrankiaiView(ListView):
    model = Irankis
    template_name = "irankis/mano_irankiai.html"
    # paginate_by = 3

    def get_queryset(self):
        prisijunges_naudotojas = self.request.user
        mano_irankiai = Irankis.objects.filter(naudotojas__naudotojas=prisijunges_naudotojas)
        return mano_irankiai


class CreateIrankisView(CreateView):
    model = Irankis
    fields = ["name", "description", "delivery", "kategorijos", "naudotojas", "nuotrauka"]
    success_url = '/irankiai/mano/'
