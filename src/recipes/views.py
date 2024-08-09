from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from .models import Recipe


# Create your views here.
# The render function requires two arguments ( request and template) and returns an HttpResponse object with that rendered text.
def recipes_home(request):
    return render(request, "recipes/recipes_home.html")


class RecipeListView(ListView):  # class-based view
    model = Recipe  # specify model
    template_name = "recipes/all_recipes.html"  # specify template


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = "recipes/recipe_details.html"
