"""AnimalsHelp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from AnimalsTeam import views

urlpatterns = [
    path('volunteers/', views.VolunteerView.as_view(), name='about_volunteers'),
    path('personel/<int:pk>/', views.VolunteerDetailView.as_view(), name='personel_detail_view'),
    path('add_volunteers/', views.AddvolunteerView.as_view(), name='add_volunteers'),
    path('delete_personal/<int:pk>/', views.PersonalDeleteView.as_view(), name='delete_person'),

    path('animals/', views.AnimalsView.as_view(), name="all_animals"),
    path('animal/<int:pk>/', views.AnimalDetailView.as_view(), name='animal_detail_view'),
    path('add_animal/', views.CreateAnimalView.as_view(), name='add_animals'),

    path('vet/', views.VetView.as_view(), name='all_vet'),
    path('vet/<int:pk>/', views.VetDetailView.as_view(), name='vet_detail_view'),

    path('food', views.FoodView.as_view(), name='food'),
    path('add_food', views.FoodCreateView.as_view(), name='add_food'),
    path('food/<int:pk>/', views.FoodDetailView.as_view(), name='food_edit'),

    path('adopter/', views.AdopterView.as_view(), name='adopter_list'),
    # path('add_adopter/', views.AddAdoptionView.as_view(), name='add_adoption'),
]