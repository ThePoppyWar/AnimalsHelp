from datetime import datetime

from django import forms
from django.core.exceptions import ValidationError

from AnimalsTeam.models import Animals, Personel, ROLE, Vet, Food, Adoption


class AnimalModelForm(forms.ModelForm):
    class Meta:
        model = Animals
        fields = '__all__'


class PersonelForm(forms.ModelForm):
    class Meta:
        model = Personel
        exclude = ['role', 'user']

    def clean(self):
        data = super().clean()
        if hasattr(self.user, 'personel'):
            raise ValidationError('You have already saved')


class AdopterForm(forms.ModelForm):
    class Meta:
        model = Personel
        exclude = ['role', 'user', 'animals']

    def clean(self):
        data = super().clean()
        if hasattr(self.user, 'personel'):
            raise ValidationError('You have already saved')


class AdoptionModelForm(forms.ModelForm):
    class Meta:
        model = Adoption
        fields = '__all__'

    def clean(self):
        data = super().clean()
        animal = data.get('animal')
        all_adoptions = Adoption.objects.all()
        for el in all_adoptions:
            if el.animal.name == animal.name:
                raise ValidationError('You have already saved')


def check_if_superuser(value):
    a = ['superAna2']
    if value is not a:
        raise ValidationError('You do not have authorize')


class VetForm(forms.ModelForm):
    class Meta:
        model = Vet
        fields = '__all__'


class FoodModelForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
