from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name}"

class Dish(models.Model):
    name = models.CharField(max_length=64)
    max_allowed_extras = models.PositiveIntegerField()
    small_prize = models.FloatField(null=True, blank=True)
    standard_prize = models.FloatField(null=True, blank=True)
    large_prize = models.FloatField(null=True, blank=True)
    category = models.ManyToManyField(Category, blank=True, related_name='category_content')

    def __str__(self):
        #str_cat = ""
        #for elem in self.category.all():
        #    str_cat += " "
        #    str_cat += str(elem)
        #return f"{self.name} in category / -ies: {str_cat}"
        return f"{self.name}"

class Additional(models.Model):
    name = models.CharField(max_length=64)
    addable_to = models.ManyToManyField(Dish, blank=True, related_name='addables')

    def __str__(self):
        return f"{self.name}"
