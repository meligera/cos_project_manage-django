from django import forms
from.models import WeekActivity, Project, WorkWeek
from django.utils import timezone
import datetime

class WeekActivityForm(forms.ModelForm):
    project = forms.ModelChoiceField(queryset=Project.objects.exclude(status='Закрыто'))
    week_number = forms.ChoiceField(choices=[])
    year = forms.TypedChoiceField(coerce=int)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        current_date = timezone.now().date()
        current_year = current_date.year
        current_week_number = current_date.isocalendar()[1]

        self.fields['year'].choices = [(year, year) for year in WorkWeek.objects.values_list('year', flat=True).distinct()]
        self.fields['year'].initial = current_year

        week_numbers = WorkWeek.objects.filter(year=current_year).values_list('week_number', flat=True)
        week_labels = [f"{obj.week_number} ({obj.start_date} - {obj.end_date})" for obj in WorkWeek.objects.filter(year=current_year)]
        self.fields['week_number'].choices = list(zip(week_numbers, week_labels))
        self.fields['week_number'].initial = current_week_number

    class Meta:
        model = WeekActivity
        fields = ('project', 'week_number', 'year', 'activity')
