from django.forms import ModelForm
from django import forms

from table.models import Main

class AddForm(ModelForm):
    class Meta:
        model = Main

        fields = '__all__'

    def clean(self):
        super(AddForm, self).clean()

        #category = self.cleaned_data.get('category')


        return self.cleaned_data