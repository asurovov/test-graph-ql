from django import forms
from graphene_django.forms.mutation import DjangoFormMutation

from server.ingredients.models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('name',)


class CategoryForm(forms.Form):
    name = forms.CharField()


class CategoryMutation(DjangoFormMutation):
    class Meta:
        form_class = CategoryForm
