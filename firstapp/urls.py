from django.urls import path
from . import views

urlpatterns = [
    path('all-foods/', views.all_foods)
]
