# Generated by Django 4.2.14 on 2024-08-08 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_rename_ingredients_ingredient_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='pic',
            field=models.ImageField(default='no_picture.png', upload_to='recipes'),
        ),
    ]
