from django.test import TestCase
from .models import Cook
from recipes.models import Recipe


# Create your tests here.
class CookTestCase(TestCase):
    def setUpTestData():
        # Set up non-modified objects used by all test methods

        fav_recipes = Recipe(name="Tacos", cooking_time=5, serves=2)
        fav_recipes.save()

        Cook.objects.create()

    def testCookName(self):
        # Get a cook object to test
        cook = Cook.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its data
        field_label = cook._meta.get_field("name").verbose_name
        # Compare the value to the expected result
        self.assertEqual(field_label, "name")

    def test_cook_name_max_length(self):
        # Get a cook object to test
        cook = Cook.objects.get(id=1)
        # Get the metadata for the 'name' field and use it to query its max_length
        max_length = cook._meta.get_field("name").max_length
        # Compare the value to the expected result
        self.assertEqual(max_length, 50)


# cook.name = '' the value in mock data


# how do I test fav_recipes?
