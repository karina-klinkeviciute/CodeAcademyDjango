from django.urls import path

from irankis.views import index, IrankiaiView, IrankisView

urlpatterns = [
    # 5ranki7 nuorodos
    path("", index, name="index"),
    path("visi/", IrankiaiView.as_view(), name="irankis-list"),
    path("visi/<int:pk>", IrankisView.as_view(), name="irankis-detail")
]
