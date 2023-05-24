from django.urls import path

from naudotojo_profilis.views import naudotojai

urlpatterns = [
    path("", naudotojai, name="naudotojai")
]

