from django.shortcuts import render


# Create your views here.
# The render function requires two arguments ( request and template) and returns an HttpResponse object with that rendered text.
def recipes_home(request):
    return render(request, "recipes/recipes_home.html")
