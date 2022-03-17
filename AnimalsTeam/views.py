from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, DeleteView

from AnimalsTeam.forms import AnimalModelForm, PersonelForm, VetForm, FoodModelForm, AdopterForm
from AnimalsTeam.models import Animals, Personel, Vet, Food, Adoption, Adopter

#Działa
class Index(View):
    def get(self, request):
        return render(request, 'base.html')

#Działa
class AnimalsView(View):
    def get(self, request):
        animals = Animals.objects.all()
        return render(request, "animals_list.html", {"animals_list": animals})

#Działa
class AnimalDetailView(DetailView):
    model = Animals
    template_name = 'animal_detail_view.html'

#działa
class CreateAnimalView(CreateView):
    model = Animals
    form_class = AnimalModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('all_animals')

#działa
class VolunteerView(View):
    def get(self, request):
        volunteers = Personel.objects.filter(role=2)
        return render(request, 'volunteer_list.html', {"volunteer_list": volunteers})

#działa
class VolunteerDetailView(DetailView):
    model = Personel
    template_name = 'personel_detail_view.html'

#Działą
class AddvolunteerView(View):
    def get(self, request):
        form = PersonelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = PersonelForm(request.POST)
        if form.is_valid():
            p = form.save(commit=False)
            p.role = 2
            p.user = request.user
            p.save()

            return redirect(f'/personel/{p.id}/')
        else:
            return render(request, 'form.html', {'form': form})

class PersonalDeleteView(DeleteView):
    model = Personel
    template_name = 'book_delete_view.html'
    success_url = reverse_lazy('index')

class AdopterView(View):
    def get(self, request):
        adoption = Adopter.objects.all()
        return render(request, 'adopter_list.html', {'adopter_list': adoption})


# class AddAdopterView:
#     def get(self, request):
#         form = AdopterForm()
#         return render(request, 'form.html', {'form': form})
#
#     def post(self, request):
#         form = AdopterForm(request.POST)
#         if form.is_valid():
#             Adoption.objects.create(animals=form.cleaned_data['animals'],
#                                     )


class VetView(View):
    def get(self, request):
        vet = Vet.objects.all()
        return render(request, 'vet_list.html', {'vet_list': vet})


class VetDetailView(DetailView):
    model = Vet
    template_name = 'vet_detail.html'


class FoodView(View):
    def get(self, request):
        food = Food.objects.all()
        return render(request, 'food_list.html', {'food_list': food})


class FoodCreateView(CreateView):
    model = Food
    form_class = FoodModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('food')


class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail_view.html'
    success_url = reverse_lazy('food')
