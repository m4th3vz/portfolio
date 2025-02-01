# home/urls.py
from django.urls import path
from .views import IndexViews, BolsoViews, PythonViews, GithubViews, ChatbotViews

urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('bolso', BolsoViews.as_view(), name='bolso'),
    path('python', PythonViews.as_view(), name='python'),
    path('github', GithubViews.as_view(), name='github'),
    path('chatbot', ChatbotViews.as_view(), name='chatbot'),
]
