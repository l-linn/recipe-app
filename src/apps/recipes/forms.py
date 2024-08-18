from django import forms


CHART__CHOICES = (  # specify choices as a tuple
    ("#0", "select"),
    ("#1", "Bar chart"),  # when user selects "Bar chart", it is stored as "#1"
    ("#2", "Pie chart"),
    ("#3", "Line chart"),
)

DIF__CHOICES = (
    ("#0", "select"),
    ("#1", "Easy"),
    ("#2", "Medium"),
    ("#3", "Intermediate"),
    ("#4", "Hard"),
)

CAT_CHOICES = (
    ("#0", "select"),
    ("#1", "Versatile"),
    ("#2", "V"),
    ("#3", "Ve"),
    ("#4", "Fish"),
    ("#5", "Contains Meat"),
)


# define class-based Form imported from Django forms
class RecipeSearchForm(forms.Form):
    recipe_name = forms.CharField(
        max_length=120,
        required=False,
    )
    category = forms.ChoiceField(choices=CAT_CHOICES)
    difficulty = forms.ChoiceField(choices=DIF__CHOICES)
    chart_type = forms.ChoiceField(choices=CHART__CHOICES)
