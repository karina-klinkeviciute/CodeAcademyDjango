from django.urls import path

from irankis.views import index, IrankiaiView, IrankisView, search, ManoIrankiaiView, CreateIrankisView, \
    DeleteIrankisView

urlpatterns = [
    # 5ranki7 nuorodos
    path("", index, name="index"),
    path("visi/", IrankiaiView.as_view(), name="irankis-list"),
    path("visi/<int:pk>", IrankisView.as_view(), name="irankis-detail"),
    path("mano/", ManoIrankiaiView.as_view(), name="mano-irankis-list"),
    path("mano_create/", CreateIrankisView.as_view(), name="mano-irankis-create"),
    path("mano_delete/<int:pk>", DeleteIrankisView.as_view(), name="mano-irankis-delete"),
    path('search/', search, name='search'),
]
