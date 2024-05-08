from django.shortcuts import render, redirect
from django.http import JsonResponse
from.forms import WeekActivityForm
from .models import WorkWeek

def create_week_activity(request):
    if request.method == 'POST':
        form = WeekActivityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('week_activity_list')  # or any other success URL
    else:
        form = WeekActivityForm()
    return render(request, 'create_week_activity.html', {'form': form})

def get_week_choices(request):
    if request.method == 'GET':
        year = request.GET.get('year')
        if year:
            week_numbers = WorkWeek.objects.filter(year=year).values_list('week_number', flat=True)
            week_labels = [f"{obj.week_number} ({obj.start_date} - {obj.end_date})" for obj in WorkWeek.objects.filter(year=year)]
            choices = list(zip(week_numbers, week_labels))
            return JsonResponse({'choices': choices})
    return JsonResponse({'choices': []})
