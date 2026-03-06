from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

# Create your models here.


class BaseModel(models.Model):
    full_name = models.CharField(max_length=120, validators=[MinLengthValidator(2)])
    birth_date = models.DateField(default='1900-01-01')
    nationality = models.CharField(max_length=50, default='Unknown')

    class Meta:
        abstract = True


class Director(BaseModel):
    years_of_experience = models.SmallIntegerField(validators=[MinValueValidator(0)], default=0)


