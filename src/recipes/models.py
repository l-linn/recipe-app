from django.db import models


# Create your models here.
class Recipe(models.Model):
    name = models.CharField(max_length=50)
    cook_zero = models.ForeignKey(
        "cooks.Cook", on_delete=models.CASCADE, null=True, blank=True
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
    ingredients = models.CharField(
        max_length=500, help_text="Please input ingredients separated with commas"
    )
    methods = models.TextField()

    def __str__(self):
        return str(self.name)
