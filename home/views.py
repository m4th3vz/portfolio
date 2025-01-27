# home/views.py
from django.views.generic import TemplateView

class IndexViews(TemplateView):
    template_name = 'home/index.html'