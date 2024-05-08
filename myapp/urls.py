from django.urls import path
from. import views

urlpatterns = [
    path('create_week_activity/', views.create_week_activity, name='create_week_activity'),
    path('get_week_choices/', views.get_week_choices, name='get_week_choices'),
]
