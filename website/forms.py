"""Forms for the website app."""

from django import forms

# Create a form that takes the following five inputs from a user:
# - The mortgage amount
# = Scenario 1 mortgage rate
# - Scenario 1 mortgage term
# - Scenario 2 mortgage rate
# - Scenario 2 mortgage term

TERM_CHOICES = [
    (6, "6 months"),
    (12, "1 year"),
    (18, "18 months"),
    (24, "2 years"),
    (36, "3 years"),
    (48, "4 years"),
    (60, "5 years"),
]


class ScenarioCalculatorForm(forms.Form):
    """Form for the scenario calculator."""

    mortgage_amount = forms.DecimalField(
        min_value=0,
        decimal_places=2,
        label="Enter your  Mortgage Amount",
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    scenario_1_rate = forms.DecimalField(
        label="Scenario 1 Mortgage Rate",
        required=True,
        min_value=0,
        max_value=100,
        decimal_places=2,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    scenario_2_rate = forms.DecimalField(
        label="Scenario 2 Mortgage Rate",
        required=True,
        min_value=0,
        max_value=100,
        decimal_places=2,
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )
    scenario_1_term = forms.ChoiceField(
        label="Scenario 1 Mortgage Term",
        required=True,
        choices=TERM_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
    scenario_2_term = forms.ChoiceField(
        label="Scenario 2 Mortgage Term",
        required=True,
        choices=TERM_CHOICES,
        widget=forms.Select(attrs={"class": "form-select"}),
    )
