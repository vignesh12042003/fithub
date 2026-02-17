from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


class FitnessHabit(models.Model):
    """Master list of fitness habits."""
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class DailyHabitLog(models.Model):
    """Tracks a user's daily habit completion."""
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=now)

    completed_habits = models.ManyToManyField(
        FitnessHabit,
        blank=True,
    )

    completion_percent = models.IntegerField(default=0)

    class Meta:
        unique_together = ("user", "date")

    def __str__(self):
        return f"{self.user.username} - {self.date}"
