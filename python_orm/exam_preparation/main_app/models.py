from django.core.validators import MinLengthValidator, MinValueValidator, MaxLengthValidator, MaxValueValidator
from django.db import models
from django.db.models import TextChoices, CASCADE

from main_app.managers import DirectorManager
from main_app.mixins import AwardedMixin, LastUpdatedMixin


# Create your models here.


class BaseModel(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown')

    class Meta:
        abstract = True


class Director(BaseModel):
    years_of_experience = models.SmallIntegerField(validators=[MinValueValidator(0)], default=0)

    objects = DirectorManager()

class Actor(AwardedMixin, LastUpdatedMixin, BaseModel):
    pass


class GenreChoices(TextChoices):
    ACTION = 'Action', 'Action'
    COMEDY = 'Comedy', 'Comedy'
    DRAMA = 'Drama', 'Drama'
    OTHER = 'Other', 'Other'


class Movie(AwardedMixin, LastUpdatedMixin, models.Model):
    title = models.CharField(max_length=150, validators=[MinLengthValidator(5)])
    release_date = models.DateField()
    storyline = models.TextField(null=True, blank=True)
    genre = models.CharField(max_length=6, choices=GenreChoices.choices, default=GenreChoices.OTHER)
    rating = models.DecimalField(max_digits=3, decimal_places=1, validators=[MinValueValidator(0.0), MaxValueValidator(10.0)], default=0.0)
    is_classic = models.BooleanField(default=False)
    director = models.ForeignKey(to=Director, on_delete=models.CASCADE)
    starring_actor = models.ForeignKey(to=Actor, null=True, blank=True, on_delete=models.SET_NULL, related_name='starring_movies')
    actors = models.ManyToManyField(to=Actor, related_name='actor_movies')