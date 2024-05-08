"""Website URLs file."""

from django.urls import path

from website.views import index, scenario_calculator

app_name = "website"

urlpatterns = [
    path("", index, name="index"),
    path("scenario-calculator/", scenario_calculator, name="scenario_calculator"),
]
