from django.urls import path

from irankis.views import index
from naudotojo_profilis.views import IrankiaiView

urlpatterns = [
    # 5ranki7 nuorodos
    path("", index, name="index"),
    path("visi/", IrankiaiView.as_view(), name="irankis-list")
]
