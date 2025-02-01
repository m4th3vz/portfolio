# home/views.py
from django.views.generic import TemplateView

class IndexViews(TemplateView):
    template_name = 'home/index.html'

class BolsoViews(TemplateView):
    template_name = 'home/bolso.html'

class PythonViews(TemplateView):
    template_name = 'home/python.html'

class GithubViews(TemplateView):
    template_name = 'home/github.html'

class ChatbotViews(TemplateView):
    template_name = 'home/chatbot.html'
