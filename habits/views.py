from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.utils.timezone import now

from .models import FitnessHabit, DailyHabitLog


@login_required
def daily_habits(request):
    """Handle daily fitness habit tracking."""
    today = now().date()

    habits = FitnessHabit.objects.filter(is_active=True)

    log, created = DailyHabitLog.objects.get_or_create(
        user=request.user,
        date=today,
    )

    if request.method == "POST":
        selected_ids = request.POST.getlist("habits")

        log.completed_habits.clear()

        for habit_id in selected_ids:
            habit = FitnessHabit.objects.get(id=habit_id)
            log.completed_habits.add(habit)

        total = habits.count()
        completed = log.completed_habits.count()

        log.completion_percent = (
            int((completed / total) * 100) if total > 0 else 0
        )
        log.save()

        return redirect("daily_habits")

    completed = log.completed_habits.all()
    progress = log.completion_percent

    history = (
        DailyHabitLog.objects
        .filter(user=request.user)
        .exclude(date=today)
        .order_by("-date")
    )

    context = {
        "habits": habits,
        "completed": completed,
        "progress": progress,
        "history": history,
        "today": today,
    }

    return render(request, "habits/habits.html", context)
