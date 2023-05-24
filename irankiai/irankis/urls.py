from django.urls import path

from irankis.views import index

urlpatterns = [
    # 5ranki7 nuorodos
    path("", index, name="index"),
]
