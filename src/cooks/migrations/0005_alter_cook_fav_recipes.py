# Generated by Django 4.2.14 on 2024-08-09 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_recipe_pic'),
        ('cooks', '0004_cook_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cook',
            name='fav_recipes',
            field=models.ManyToManyField(related_name='recipes_fav', to='recipes.recipe'),
        ),
    ]
