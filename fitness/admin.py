from django.contrib import admin
from .models import BMIRecord

@admin.register(BMIRecord)
class BMIRecordAdmin(admin.ModelAdmin):
    list_display = ('user', 'bmi_value', 'category', 'created_at')
