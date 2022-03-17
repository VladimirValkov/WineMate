from django.forms import ModelForm
from django import forms

from table.models import Main

class MainForm(ModelForm):
    class Meta:
        model = Main
        fields = '__all__'

    def clean(self):
        super(MainForm, self).clean()
        return self.cleaned_data
