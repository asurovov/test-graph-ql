from django.contrib import admin

from server.ingredients.models import Category, Ingredient, Pet

admin.site.register(Category)
admin.site.register(Ingredient)
admin.site.register(Pet)
