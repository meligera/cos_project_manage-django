from django.db import models
from django.contrib.postgres.fields import ArrayField

class Project(models.Model):
    activity = models.CharField(max_length=100)
    stage = models.CharField(null=True, max_length=20, choices=[
        ('ТЗ', 'ТЗ'),
        ('Закупка', 'Закупка'),
        ('Проектирование', 'Проектирование'),
        ('Опытная эксплуатация', 'Опытная эксплуатация'),
        ('ПМИ', 'ПМИ'),
        ('Завершено', 'Завершено'),
        ('Внедрение', 'Внедрение'),
    ])
    status = models.CharField(null=True, max_length=20, choices=[
        ('Открыто', 'Открыто'),
        ('Закрыто', 'Закрыто'),
        ('Ожидание', 'Ожидание'),
    ])
    basis = models.TextField(null=True, blank=True)
    representive = models.CharField(max_length=50, choices=[
        ('УМК', 'УМК'),
        ('Фонд ТиУ', 'Фонд ТиУ'),
        # ... (add other choices)
    ], default='Фонд ТиУ')
    foreigh_manager = models.CharField(max_length=100, null=True, blank=True)
    analytic = models.CharField(max_length=50, choices=[
        ('Голубев А.А.', 'Голубев А.А.'),
        ('Пискарев С.Н.', 'Пискарев С.Н.'),
        ('Клюжин А.О.', 'Клюжин А.О.'),
        ('Асмаев А.А.', 'Асмаев А.А.'),
    ])
    creation_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.activity

class WeekActivity(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='week_activities')
    week_number = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    activity = models.TextField()
    def __str__(self):
        return f"{self.activity}, {self.week_number}, {self.project}"


class WorkWeek(models.Model):
    year = models.PositiveIntegerField()
    week_number = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    week_activities = models.ManyToManyField(WeekActivity, blank=True)
    def __str__(self):
        return f"{self.start_date} - {self.end_date}"