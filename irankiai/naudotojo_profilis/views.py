from django.shortcuts import render
from django.views.generic import ListView

from irankis.models import Irankis
from naudotojo_profilis.models import NaudotojoProfilis


# Create your views here.
def naudotojai(request):
    visi_naudotojai = NaudotojoProfilis.objects.all()

    context = {
        "naudotojai": visi_naudotojai
    }

    return render(request, "naudotojai.html", context=context)

def naudotojas(request, naudotojo_id):
    naudotojo_info = NaudotojoProfilis.objects.get(pk=naudotojo_id)
    return render(request, "naudotojas.html", context={"naudotojas": naudotojo_info})


class IrankiaiView(ListView):
    model = Irankis
    template_name = "irankiai.html"
