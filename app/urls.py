from django.urls import path
from . import views


urlpatterns = [
    path('', views.Calendar, name="calendar"),
    path('search/<int:year>/<int:oy>/', views.Search, name="keyingi"),
]
