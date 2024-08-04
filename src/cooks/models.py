from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Cook(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True
    )  # what to set as default or it doesn't matter too much?

    fav_recipes = models.ManyToManyField("recipes.Recipe", null=True)

    def __str__(self):
        return str(self.name)
