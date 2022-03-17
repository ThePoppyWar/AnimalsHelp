from datetime import datetime

from django import forms

from AnimalsTeam.models import Animals, Personel, ROLE, Vet, Food, Adopter


class AnimalModelForm(forms.ModelForm):

    class Meta:
        model = Animals
        fields = '__all__'

class PersonelForm(forms.ModelForm):
    class Meta:
        model = Personel
        exclude = ['role', 'user']


class AdopterForm(forms.ModelForm):
    class Meta:
        model = Adopter
        exclude = ['user']



class VetForm(forms.ModelForm):

    class Meta:
        model = Vet
        fields = '__all__'

class FoodModelForm(forms.ModelForm):

    class Meta:
        model = Food
        fields = '__all__'









