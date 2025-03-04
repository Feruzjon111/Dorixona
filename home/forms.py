from django import forms
from .models import Dorixona
class DorixonaForm(forms.ModelForm):
    class Meta:
        model = Dorixona
        fields = ['name', 'price', 'year', 'description', 'soni', 'image']

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if len(name) < 1:
            raise forms.ValidationError("Dori nomini togri kiriting!")
        return name

    def clean_price(self):
        price = self.cleaned_data.get('price')
        if price < 0:
            raise forms.ValidationError("Dori narxini togri kiriting!")
        return price

    def clean_year(self):
        year = self.cleaned_data.get('year')
        if year < 2025:
            raise forms.ValidationError("Dori muddati tugagan!!!")
        return year

    def clean_description(self):
        description = self.cleaned_data.get('description')
        if len(description) < 1:
            raise forms.ValidationError("Tavsif yozing!")
        return description

    def clean_soni(self):
        soni = self.cleaned_data.get('soni')
        if soni < 0:
            raise forms.ValidationError("Dori sonini togri kiriting!")
        return soni


