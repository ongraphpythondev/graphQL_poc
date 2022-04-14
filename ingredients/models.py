from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name


class Ingredient(models.Model):
    category = models.ForeignKey(Category, related_name="ingredients", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    notes = models.TextField() 

    def __str__(self):
        return self.name 
