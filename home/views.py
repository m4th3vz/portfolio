# home/views.py
from django.views.generic import TemplateView

class IndexViews(TemplateView):
    template_name = 'home/index.html'

class PythonViews(TemplateView):
    template_name = 'home/python.html'

class AplicacaoWebViews(TemplateView):  
    template_name = 'home/aplicacao_web.html'

class HtmlCssViews(TemplateView):
    template_name = 'home/html_css.html'

class HospedagemViews(TemplateView):
    template_name = 'home/hospedagem.html'

class AboutViews(TemplateView):
    template_name = 'home/about.html'

class Page1Views(TemplateView):
    template_name = 'home/page1.html'

class Page2Views(TemplateView):
    template_name = 'home/page2.html'

class Page3Views(TemplateView):
    template_name = 'home/page3.html'