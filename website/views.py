"""Website views file."""

import logging

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from website.forms import ScenarioCalculatorForm

logger = logging.getLogger(__name__)


def index(request: HttpRequest) -> HttpResponse:
    """View for the index page."""
    return render(request, "website/index.html")


def scenario_calculator(request: HttpRequest) -> HttpResponse:
    """View for the scenario calculator page."""
    if request.method == "POST":
        form = ScenarioCalculatorForm(request.POST)
        if form.is_valid():
            mortgage_amount = form.cleaned_data["mortgage_amount"]
            scenario_1_rate = form.cleaned_data["scenario_1_rate"]
            scenario_2_rate1 = form.cleaned_data["scenario_2_rate"]
            scenario_1_term = int(form.cleaned_data["scenario_1_term"])
            scenario_2_term1 = int(form.cleaned_data["scenario_2_term"])

            calculated_rate: float = calculate_scenario(
                mortgage_amount,
                scenario_1_rate,
                scenario_1_term,
                scenario_2_rate1,
                scenario_2_term1,
            )

            message = (
                f"For scenario 2 to be better, you are predicting that the cheapest "
                f"mortgage rate in {scenario_1_term - scenario_2_term1} months' time "
                f"will be less than {calculated_rate}%."
            )

            return render(
                request,
                "website/scenario_calculator.html",
                {
                    "form": form,
                    "calculated_rate": calculated_rate,
                    "message": message,
                },
            )
    else:
        form = ScenarioCalculatorForm()

    return render(request, "website/scenario_calculator.html", {"form": form})


def calculate_scenario(
    mortgage_amount: float,
    scenario_1_rate: float,
    scenario_1_term: int,
    scenario_2_rate1: float,
    scenario_2_term1: int,
) -> float:
    """Calculate the payments for two scenarios."""
    logger.debug(f"{mortgage_amount=}")
    logger.debug(f"{scenario_1_rate=}")
    logger.debug(f"{scenario_1_term=}")
    logger.debug(f"{type(mortgage_amount)=}")
    logger.debug(f"{type(scenario_1_rate)=}")
    logger.debug(f"{type(scenario_1_term)=}")

    scenario_1_total = (mortgage_amount * scenario_1_rate / 100 / 12) * (
        scenario_1_term
    )

    scenario_2_rate_1_subtotal = (mortgage_amount * scenario_2_rate1 / 100 / 12) * (
        scenario_2_term1
    )

    scenario_2_rate2_subtotal = scenario_1_total - scenario_2_rate_1_subtotal

    scenario_2_term2 = scenario_1_term - scenario_2_term1

    months_in_year = 12

    result = (
        scenario_2_rate2_subtotal / scenario_2_term2 / mortgage_amount * months_in_year
    )

    # retun the result as a percentage with two decimal places
    return round(result * 100, 2)
