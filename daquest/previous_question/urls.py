from django.urls import path

from . import views

app_name = 'previous_question'

urlpatterns = [
    path('', views.previous_question, name="previous_question"),
]
