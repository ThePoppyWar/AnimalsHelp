from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse

# Create your models here.

ROLE = (
    (1, 'adopter'),
    (2, "volunteer"),
)

SPECIES = (
    (1, 'dog'),
    (2, 'cat'),
    (3, 'rabit'),
    (4, 'horse'),
    (5, 'bird'),
    (6, 'goat'),
    (6, 'cow'),
)
HEALTH = (
    (1, "healthy"),
    (2, "chronically sick"),
    (3, "seriously ill"),
    (4, "during treatment"),
    (5, "moribund"),
)

STATUS_ADOPTION = (
    (1, 'waiting for adoption'),
    (2, 'in the middle of trying to adopt'),
    (3, 'not to adoption'),
    (4, 'adopted'),
)

STATUS_ADOPTER = (
    (1, 'in the middle of trying to adopt'),
    (2, 'adopted'),
)

SPECIALIZATION = (
    (1, 'pets permitted'),
    (2, 'exotic pets'),
    (3, 'livestock'),
)

TYPE_OF_FOOD = (
    (1, "emergency animal feed"),
    (2, "animal feed")
)


class Animals(models.Model):
    name = models.CharField(max_length=60, unique=True)
    species = models.IntegerField(choices=SPECIES)
    health = models.IntegerField(choices=HEALTH)
    status = models.IntegerField(choices=STATUS_ADOPTION)

    def __str__(self):
        return f"{self.name}"

    def get_absolute_url(self):
        return reverse('animal_detail_view', args=(self.pk,))


class Personel(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=120)
    role = models.IntegerField(choices=ROLE)
    join_date = models.DateTimeField(blank=False)
    description = models.CharField(max_length=500)
    animals = models.ManyToManyField(Animals, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}{self.last_name}'

    def get_absolute_url(self):
        return reverse('personel_detail_view', args=(self.pk,))

    def get_absolute_url1(self):
        return reverse('adopter_detail_view', args=(self.pk,))


# class Adopter(models.Model):
#     name = models.CharField(max_length=60)
#     last_name = models.CharField(max_length=120)
#     address = models.CharField(max_length=120)
#     animal = models.ManyToManyField(Animals, blank=True)
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return f'{self.name} {self.last_name}'
#
#     def get_absolute_url(self):
#         return reverse('adopter_detail_view', args=(self.pk,))

class Adoption(models.Model):
    animal = models.ForeignKey(Animals, on_delete=models.CASCADE)
    adopter = models.ForeignKey(Personel, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS_ADOPTER)


class Vet(models.Model):
    name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=120)
    specialization = models.IntegerField(choices=SPECIALIZATION)
    animals = models.ManyToManyField(Animals, blank=True)

    def __str__(self):
        return f"{self.name} {self.last_name}"

    def get_absolute_url(self):
        return reverse('vet_detail_view', args=(self.pk,))


class Food(models.Model):
    name = models.CharField(max_length=60)
    type = models.IntegerField(choices=TYPE_OF_FOOD)
    stan = models.IntegerField()

    def __str__(self):
        return f"{self.stan} {self.name} {self.type}"

    def get_absolute_url(self):
        return reverse('food_detail_view', args=(self.pk,))