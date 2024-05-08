"""Forms for the website app."""

from django import forms

# Create a form that takes the following five inputs from a user:
# - The mortgage amount
# = Scenario 1 mortgage rate
# - Scenario 1 mortgage term
# - Scenario 2 mortgage rate
# - Scenario 2 mortgage term


class ScenarioCalculatorForm(forms.Form):
    """Form for the scenario calculator."""

    mortgage_amount = forms.DecimalField(label="Mortgage Amount")
    scenario_1_rate = forms.DecimalField(label="Scenario 1 Mortgage Rate")
    scenario_1_term = forms.IntegerField(label="Scenario 1 Mortgage Term")
    scenario_2_rate = forms.DecimalField(label="Scenario 2 Mortgage Rate")
    scenario_2_term = forms.IntegerField(label="Scenario 2 Mortgage Term")
