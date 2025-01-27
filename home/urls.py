# home/urls.py
from django.urls import path
from .views import IndexViews

urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
]
