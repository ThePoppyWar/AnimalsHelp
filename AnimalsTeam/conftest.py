import pytest
# from django.contrib.auth.models import User
from django.contrib.auth.models import User
from django.test import Client as WebClient

from AnimalsTeam.models import Animals, Personel, Food


@pytest.fixture
def client():
    client = WebClient()
    return client


@pytest.fixture
def animals():
    lst = []
    a = Animals.objects.create(name="Cziko", species=2, health=1, status=3)
    lst.append(a)
    a = Animals.objects.create(name="Malinka", species=1, health=3, status=2)
    lst.append(a)
    a = Animals.objects.create(name="Czikita", species=6, health=4, status=2)
    lst.append(a)
    return lst

@pytest.fixture
def user():
    u = User.objects.create(username='test')
    u.set_password('testujemyto1')
    u.save()
    return u

@pytest.fixture
def food():
    lst = []
    f = Food.objects.create(name='Kocie', type=1, stan=100)
    lst.append(f)
    f = Food.objects.create(name='psie', type=2, stan=140)
    lst.append(f)
    f = Food.objects.create(name='słoma', type=1, stan=120)
    lst.append(f)
    return lst



# @pytest.fixture
# def volunteer():
#     lst = []
#     v = Personel.objects.create(name='helena', last_name='Magoo', role=1, description='Cośtam',
#                                 animals=1, user=3)
#     lst.append(v)
#     v = Personel.objects.create(name='hca', last_name='Dagoo', role=2, description='heheam',
#                                 animals=1, user=3)
#     lst.append(v)
#     v = Personel.objects.create(name='luca', last_name='berdo', role=1, description='marzena',
#                                 animals=1, user=2)
#     lst.append(v)
#     return lst
