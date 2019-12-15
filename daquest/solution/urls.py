from django.urls import path

from . import views

app_name = 'solution'

urlpatterns = [
    path('', views.solution, name="solution"),
]
