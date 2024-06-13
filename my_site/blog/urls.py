from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path('all_posts', views.all_posts, name="all_posts"),
    path("all_posts/<slug:slug>", views.SinglePostView.as_view(), name="detailed_post"),
    path("stored_posts", views.ReadLater.as_view(), name="read_later"),
]