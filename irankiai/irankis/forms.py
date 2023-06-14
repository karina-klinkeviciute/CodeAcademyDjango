from irankis.models import IrankioAtsiliepimas
from django import forms


class AtsiliepimoForma(forms.ModelForm):
    class Meta:
        model = IrankioAtsiliepimas
        fields = ('atsiliepimas', 'irankis', 'naudotojas')
        widgets = {'irankis': forms.HiddenInput(), 'naudotojas': forms.HiddenInput()}
