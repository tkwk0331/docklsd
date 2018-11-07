from django import forms
from .models import Unyou


class UnyouForm(forms.ModelForm):

    class Meta:
        model = Unyou
        fields = ('lbc','main_lbc','company_name','telephone_number')
        widgets = {
                    'lbc': forms.NumberInput(attrs={'min':1}),
                    'main_lbc': forms.NumberInput(attrs={'min':1}),
                    'company_name': forms.TextInput(attrs={'placeholder':'記入例：株式会社ネオキャリア'}),
                    'telephone_number': forms.NumberInput(attrs={'min':1}),
                  }
