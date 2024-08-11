from django.db import models
from django.shortcuts import reverse


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
    difficulty = models.CharField(
        max_length=20, choices=difficulty_choice, editable=False
    )

    def calculate_difficulty(self):
        num_ingredients = (
            Ingredient.objects.count()
        )  # How do I get the number of ingredient?

        if self.cooking_time < 10 and num_ingredients < 4:
            self.difficulty = "easy"
        elif self.cooking_time < 10 and num_ingredients >= 4:
            self.difficulty = "medium"
        elif self.cooking_time >= 10 and num_ingredients < 4:
            self.difficulty = "intermediate"
        else:
            self.difficulty = "Hard"

    serves = models.PositiveIntegerField()
    ingredient = models.ManyToManyField("recipes.Ingredient")
    methods = models.TextField()

    pic = models.ImageField(upload_to="recipes", default="no_picture.png")

    def get_absolute_url(self):
        return reverse("recipes:detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.name} - {self.cook} - {self.cooking_time} - {self.difficulty}"
