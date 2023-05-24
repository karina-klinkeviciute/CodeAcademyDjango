from django.shortcuts import render

from irankis.models import Irankis, IrankioVienetas


# Create your views here.
def index(request):

    # suskai2iuojam reikiamus duomenis
    irankiu_kiekis = Irankis.objects.count()
    irankiiu_vienetu_kiekis = IrankioVienetas.objects.count()


    # į šabloną turi b8ti paduodamas žodynas su duomenimmis
    context = {
        "irankiu_kiekis": irankiu_kiekis,
        "irankiu_vienetu_kiekis": irankiiu_vienetu_kiekis
    }

    # žodynas su duomenimis per kintamąjį context sujungiamas su šablonu index ir grąžinamas į naršyklę
    return render(request, "index.html", context=context)
