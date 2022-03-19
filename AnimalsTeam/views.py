from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, UpdateView, DeleteView

from AnimalsTeam.forms import AnimalModelForm, PersonelForm, VetForm, FoodModelForm, AdopterForm, AdoptionModelForm
from AnimalsTeam.models import Animals, Personel, Vet, Food, Adoption


# work
class Index(View):
    def get(self, request):
        return render(request, 'base.html')


# work
class AnimalsView(View):
    def get(self, request):
        animals = Animals.objects.all()
        return render(request, "animals_list.html", {"animals_list": animals})


# work
class AnimalDetailView(DetailView):
    model = Animals
    template_name = 'animal_detail_view.html'


# work
class CreateAnimalView(LoginRequiredMixin, CreateView):
    model = Animals
    form_class = AnimalModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('all_animals')


# work
class VolunteerView(View):
    def get(self, request):
        volunteers = Personel.objects.filter(role=2)
        return render(request, 'volunteer_list.html', {"volunteer_list": volunteers})


# work
class VolunteerDetailView(DetailView):
    model = Personel
    template_name = 'personel_detail_view.html'


# work
class AddvolunteerView(LoginRequiredMixin, View):
    def get(self, request):
        form = PersonelForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = PersonelForm(request.POST)
        form.user = request.user
        if form.is_valid():
            p = form.save(commit=False)
            p.role = 2
            p.user = request.user
            p.save()

            return redirect(f'/AnimalsTeam/personel/{p.id}/')
        else:
            return render(request, 'form.html', {'form': form})


# work
class AdopterView(View):
    def get(self, request):
        adoptioner = Personel.objects.filter(role=1)
        return render(request, 'adopter_list.html', {'adopter_list': adoptioner})


# work
class AddAdopterView(LoginRequiredMixin, View):
    def get(self, request):
        form = AdopterForm()
        return render(request, 'form.html', {'form': form})

    def post(self, request):
        form = AdopterForm(request.POST)
        form.user = request.user
        if form.is_valid():
            a = form.save(commit=False)
            a.role = 1
            a.user = request.user
            a.save()

            return redirect(f'/AnimalsTeam/adopter/{a.id}/')
        return render(request, 'form.html', {'form': form})




# work
class AdopterDetailView(DetailView):
    model = Personel
    template_name = 'adopter_detail_view.html'


# work
class AdoptionView(View):
    def get(self, request):
        adoption = Adoption.objects.filter()
        return render(request, 'adoption_list.html', {'adoption_list': adoption})


# work
class AdoptionCreateView(PermissionRequiredMixin, CreateView):
    model = Adoption
    form_class = AdoptionModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('adoption_list')
    permission_required = ['AnimalTeam.add_adoption']


class AdoptionDeleteView(PermissionRequiredMixin, DeleteView):
    model = Adoption
    template_name = 'adoption_delete_view.html'
    success_url = reverse_lazy('adoption_list')
    permission_required = ['AnimalTeam.delete_vet']

# work
class VetView(View):
    def get(self, request):
        vet = Vet.objects.all()
        return render(request, 'vet_list.html', {'vet_list': vet})


# work
class VetCreate(PermissionRequiredMixin, CreateView):
    mode = Vet
    form_class = VetForm
    template_name = 'form.html'
    success_url = reverse_lazy('all_vet')
    permission_required = ['AnimalTeam.add_vet']


# work
class VetDetailView(DetailView):
    model = Vet
    template_name = 'vet_detail.html'


# work
class VetDeleteView(PermissionRequiredMixin, DeleteView):
    model = Vet
    template_name = 'vet_delete_view.html'
    success_url = reverse_lazy('all_vet')
    permission_required = ['AnimalTeam.delete_vet']


# work
class FoodView(View):
    def get(self, request):
        food = Food.objects.all()
        return render(request, 'food_list.html', {'food_list': food})


# work
class FoodCreateView(LoginRequiredMixin, CreateView):
    model = Food
    form_class = FoodModelForm
    template_name = 'form.html'
    success_url = reverse_lazy('food')


# work
class FoodDetailView(DetailView):
    model = Food
    template_name = 'food_detail_view.html'
    success_url = reverse_lazy('food')


# work
class FoodModyfyView(LoginRequiredMixin, UpdateView):
    model = Food
    fields = ['stan']
    template_name = 'food_edit.html'
    success_url = reverse_lazy('food')


# work
class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')
