import pytest as pytest
from django.test import TestCase, Client

from django.urls import reverse
# Create your tests here.
from AnimalsTeam.models import Animals


def test_index(client):
    url = reverse('index')
    response = client.get(url)
    assert response.status_code == 200


# login
@pytest.mark.django_db
def test_user(client, user):
    url = reverse('login')
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'username': "test",
        'password': 'testujemyto1'
    }
    response = client.post(url, dct)
    assert response.status_code == 302


# logout
@pytest.mark.django_db
def test_logout_view(client, user):
    dct = {
        'username': "test",
        'password': 'testujemyto1'
    }
    url = reverse('logout')
    response = client.post(url, dct)
    assert response.wsgi_request.user.is_authenticated == False


@pytest.mark.django_db
def test_animals(client, animals):
    url = reverse("all_animals")
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context["animals_list"].count() == len(animals)
    for item in animals:
        assert item in context['animals_list']


@pytest.mark.django_db
def test_food(client, food):
    url = reverse('food')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context["food_list"].count() == len(food)
    for item in food:
        assert item in context['food_list']

# @pytest.mark.django_db
# def test_Volunteer(client, volunteer):
#     url = reverse("about_volunteers")
#     response = client.get(url)
#     assert response.status_code == 200
#     context = response.context
#     assert context["volunteer_list"].count() == len(volunteer)
#     for item in volunteer:
#         assert item in context['volunteer_list']

# @pytest.mark.django_db
# def test_animals(client, animals):
#     url = reverse('all_animals')
#     response = client.get(url)
#     assert response.status_code == 200
#     assert len(Animals.objects.all()) >= 1
