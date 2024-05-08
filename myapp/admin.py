from django.contrib import admin
from .models import Project, WeekActivity, WorkWeek
from.views import create_week_activity
from.forms import WeekActivityForm

class WeekActivityAdmin(admin.ModelAdmin):
    form = WeekActivityForm

admin.site.register(Project)
admin.site.register(WeekActivity, WeekActivityAdmin)
admin.site.register(WorkWeek)