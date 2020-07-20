from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    state = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    notes = models.TextField()
    category = models.ForeignKey(
        Category, related_name='ingredients', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
