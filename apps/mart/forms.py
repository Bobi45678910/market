from django import forms

from apps.mart.models.AdModel import Ad


class AdForm(forms.ModelForm):
    class Meta:
        model = Ad
        fields = [
            'name', 'category', 'city', 'despcription',
            'type', 'price'
        ]
