from django.db import models


# Create your models here.
class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cook = models.ForeignKey(
        "cooks.Cook",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="recipes",
    )
    cooking_time = models.IntegerField(
        help_text="Please input how long it takes in minutes"
    )
    difficulty_choice = (
        ("easy", "Easy"),
        ("medium", "Medium"),
        ("intermediate", "Intermediate"),
        ("hard", "Hard"),
    )
    difficulty = models.CharField(max_length=20, choices=difficulty_choice)
    serves = models.PositiveIntegerField()
    ingredient = models.ManyToManyField("recipes.Ingredient")
    methods = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.cook} - {self.cooking_time} - {self.difficulty}"
