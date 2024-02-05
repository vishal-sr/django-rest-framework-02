from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.


class Languages(models.Model):
    languages = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.languages}"


class Author(models.Model):
    name = models.CharField(max_length=25)
    language = models.ManyToManyField(Languages,  related_name="Languages")

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    title = models.CharField(max_length=50)
    ratings = models.IntegerField(validators=[
        MinValueValidator(0), MaxValueValidator(5)
    ])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name="Author")

    def __str__(self):
        return f"{self.title} -- {self.author}"
