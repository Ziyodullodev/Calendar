from django.urls import path
from . import views


urlpatterns = [
    path('', views.Calendar, name="calendar"),
]
