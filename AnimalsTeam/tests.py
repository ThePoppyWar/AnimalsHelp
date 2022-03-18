import pytest as pytest
from django.test import TestCase, Client

from django.urls import reverse
# Create your tests here.
from AnimalsTeam.models import Animals, Personel, Food


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


# view list animals
@pytest.mark.django_db
def test_animals(client, animals):
    url = reverse("all_animals")
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context["animals_list"].count() == len(animals)
    for item in animals:
        assert item in context['animals_list']


# list food
@pytest.mark.django_db
def test_foods(client, foods):
    url = reverse('food')
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context["food_list"].count() == len(foods)
    for item in foods:
        assert item in context['food_list']


# list volunteers
@pytest.mark.django_db
def test_Volunteers(client, volunteers):
    url = reverse("about_volunteers")
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context["volunteer_list"].count() == len(volunteers)
    for item in volunteers:
        assert item in context['volunteer_list']


# list adopter
@pytest.mark.django_db
def test_Adopters(client, adopters):
    url = reverse("adopter_list")
    response = client.get(url)
    assert response.status_code == 200
    context = response.context
    assert context["adopter_list"].count() == len(adopters)
    for item in adopters:
        assert item in context['adopter_list']


# add volunteer
@pytest.mark.django_db
def test_volunteer_add_view_with_login(user, client, animals):
    url = reverse('add_volunteers')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'name': 'basia',
        'last_name': 'Kosa',
        'role': 2,
        'join_date': '2022-03-22',
        'description': 'cos cos cos cos',
        'animals': [x.id for x in animals]
    }
    client.post(url, dct)
    assert Personel.objects.first()


# add adopter
@pytest.mark.django_db
def test_adopter_add_view_with_login(user, client, animals):
    url = reverse('add_adopter')
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    dct = {
        'name': 'basia',
        'last_name': 'Kosa',
        'role': 1,
        'join_date': '2022-03-22',
        'description': 'cos cos cos cos',
        'animals': [x.id for x in animals]
    }
    client.post(url, dct)
    assert Personel.objects.first()


# modyfy food
@pytest.mark.django_db
def test_get_FoodModyfyView_view_with_login(user, client, food):
    url = reverse('food_edite_view', args=(food.id,))
    client.force_login(user)
    response = client.get(url)
    assert response.status_code == 200
    food_before = food
    dct = {
        'stan': 125
    }
    client.post(url, dct)
    assert food_before.stan != Food.objects.last().stan


# detail food
@pytest.mark.django_db
def test_food_detail_view(client, food):
    url = reverse('food_detail_view', args=(food.id,))
    dct = {
        'food': food.id,
    }
    response = client.get(url)
    assert response.status_code == 200

# animal detail
@pytest.mark.django_db
def test_animals_detail_view(client, animal):
    url = reverse('animal_detail_view', args=(animal.id, ))
    dct = {
        'animal': animal.id,
    }
    response = client.get(url, dct)
    assert response.status_code == 200

# detail volunteer
@pytest.mark.django_db
def test_volunteer_detail_view(client, volunteer):
    url = reverse('personel_detail_view', args=(volunteer.id, ))
    dct = {
        'volunteer': volunteer.id,
    }
    response = client.get(url, dct)
    assert response.status_code == 200

# detail adopter
@pytest.mark.django_db
def test_adopter_detail_view(client, adopter):
    url = reverse('adopter_detail_view', args=(adopter.id, ))
    dct = {
        'adopter': adopter.id,
    }
    response = client.get(url, dct)
    assert response.status_code == 200
