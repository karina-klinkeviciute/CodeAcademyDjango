from django.urls import path

from naudotojo_profilis.views import naudotojai, naudotojas

urlpatterns = [
    path("", naudotojai, name="naudotojai"),
    path("<int:naudotojo_id>", naudotojas, name="naudotojas")
]

