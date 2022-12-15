from django import forms
from . models import series

class SeriesForm(forms.ModelForm):
    class Meta:
        model = series
        fields = ['name','desc','year','Language','image']
