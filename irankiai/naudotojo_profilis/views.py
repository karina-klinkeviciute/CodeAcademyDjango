from django.shortcuts import render

from naudotojo_profilis.models import NaudotojoProfilis


# Create your views here.
def naudotojai(request):
    visi_naudotojai = NaudotojoProfilis.objects.all()

    context = {
        "naudotojai": visi_naudotojai
    }

    return render(request, "naudotojai.html", context=context)
