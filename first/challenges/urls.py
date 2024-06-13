from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:month>", views.monthly_numbers),
    path("<str:month>", views.challenges, name="month_challenges")
]