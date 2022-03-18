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
def animal():
    animal = Animals.objects.create(name="Cziko", species=2, health=1, status=3)
    return animal


@pytest.fixture
def user():
    u = User.objects.create(username='test')
    u.set_password('testujemyto1')
    u.save()
    return u


@pytest.fixture
def users():
    x = []
    for k in range(5):
        x.append(User.objects.create(username=k))

    return x


@pytest.fixture
def foods():
    lst = []
    f = Food.objects.create(name='Kocie', type=1, stan=100)
    lst.append(f)
    f = Food.objects.create(name='psie', type=2, stan=140)
    lst.append(f)
    f = Food.objects.create(name='słoma', type=1, stan=120)
    lst.append(f)
    return lst


@pytest.fixture
def food():
    food = Food.objects.create(name='Karma', type=1, stan=220)
    return food


@pytest.fixture
def volunteers(users, animals):
    lst = []
    for user in users:
        lst.append(Personel.objects.create(name='helena', last_name='Magoo',
                                           join_date="2022-12-22", role=2, description='Cośtam', user=user))
        lst[-1].animals.set(animals)
    return lst


@pytest.fixture
def volunteer(user, animals):
    volunteer = Personel.objects.create(name='maja', last_name='kuku',
                                        join_date="2019-11-12", role=2,
                                        description='Cośtam', user=user)
    volunteer.animals.set(animals)
    return volunteer


@pytest.fixture
def adopters(users, animals):
    lst = []
    for user in users:
        lst.append(Personel.objects.create(name='helena', last_name='Magoo',
                                           join_date="2022-12-22", role=1, description='Cośtam', user=user))
        lst[-1].animals.set(animals)
    return lst


@pytest.fixture
def adopter(user, animals):
    adopter = Personel.objects.create(name='kacha', last_name='pacyna',
                                      join_date="2018-03-12", role=2,
                                      description='Cośtam', user=user)
    adopter.animals.set(animals)
    return adopter
