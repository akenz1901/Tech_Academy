from django import forms
from .models import Cohort, Native


class CohortForm(forms.ModelForm):
    class Meta:
        model = Cohort
        fields = ('name', 'description')


class NativeForm(forms.ModelForm):
    class Meta:
        model = Native
        fields = ('first_name', 'last_name', 'image', 'cohort')
