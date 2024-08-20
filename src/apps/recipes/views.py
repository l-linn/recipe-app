from django.shortcuts import render
from django.views.generic import ListView, DetailView  # to display lists
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from .forms import RecipeSearchForm
from .utils import get_chart
from .models import Recipe
import pandas as pd


# Create your views here.
# The render function requires two arguments ( request and template) and returns an HttpResponse object with that rendered text.
def recipes_home(request):
    return render(request, "recipes/recipes_home.html")


def search_recipes(request):
    form = RecipeSearchForm(request.POST or None)
    # df means DataFrame
    recipes_df = None
    chart = None

    # check if the button is clicked
    if request.method == "POST":
        recipe_name = request.POST.get("recipe_name")
        chart_type = request.POST.get("chart_type")
        recipe_category = request.POST.get("recipe_category")
        cooking_time = request.POST.get("cooking_time")

        # apply filter to extract data
        qs = Recipe.objects.filter(
            Q(name=recipe_name)
            | Q(category=recipe_category)
            | Q(cooking_time=cooking_time)
        )

        if qs:
            recipes_df = pd.DataFrame(qs.values("name", "cooking_time", "category"))
            chart = get_chart(chart_type, recipes_df, labels=recipes_df["name"].values)
            recipes_df = recipes_df.to_html()

    # pack up data to be sent to template in the context dictionary
    context = {"form": form, "recipes_df": recipes_df, "chart": chart}

    return render(request, "recipes/search_recipes.html", context)


class RecipeListView(LoginRequiredMixin, ListView):  # class-based view
    model = Recipe  # specify model
    template_name = "recipes/all_recipes.html"  # specify template


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = "recipes/recipe_details.html"


# import pdb
# pdb.set_trace()
# qs = [q for q in qs if q.difficulty == recipe_difficulty]
