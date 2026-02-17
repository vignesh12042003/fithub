from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BMIRecord


def home(request):
    """Render the landing page."""
    return render(request, "home.html")


@login_required
def bmi(request):
    """Calculate BMI and store the result."""
    bmi = None
    category = None
    calories = None

    if request.method == "POST":
        height = float(request.POST["height"]) / 100
        weight = float(request.POST["weight"])

        bmi = round(weight / (height * height), 2)

        if bmi < 18.5:
            category = "Underweight"
        elif bmi < 25:
            category = "Normal"
        else:
            category = "Overweight"

        calories = int(weight * 30)

        BMIRecord.objects.create(
            user=request.user,
            height=height * 100,
            weight=weight,
            bmi_value=bmi,
            category=category,
        )

    return render(
        request,
        "bmi.html",
        {
            "bmi": bmi,
            "category": category,
            "calories": calories,
        },
    )

    records = BMIRecord.objects.filter(user=request.user).order_by("-created_at")
    return render(request, "bmi.html", {"records": records})


@login_required
def dashboard(request):
    """Display BMI history and latest record."""
    records = BMIRecord.objects.filter(user=request.user).order_by("-created_at")
    latest = records.first()

    return render(
        request,
        "dashboard.html",
        {
            "records": records,
            "latest": latest,
            "total_records": records.count(),
        },
    )


@login_required
def exercise(request):
    """Show exercise recommendations based on latest BMI."""
    latest_record = (
        BMIRecord.objects.filter(user=request.user)
        .order_by("-created_at")
        .first()
    )

    category = latest_record.category if latest_record else None

    return render(
        request,
        "exercise.html",
        {
            "category": category,
        },
    )
