# home/urls.py
from django.urls import path
from .views import IndexViews, Page1Views, Page2Views, Page3Views, AboutViews, PythonViews, AplicacaoWebViews, HtmlCssViews, HospedagemViews

urlpatterns = [
    path('', IndexViews.as_view(), name='index'),
    path('python/', PythonViews.as_view(), name='python'),
    path('aplicacaoweb/', AplicacaoWebViews.as_view(), name='aplicacaoweb'),
    path('htmlcss/', HtmlCssViews.as_view(), name='htmlcss'),
    path('hospedagem/', HospedagemViews.as_view(), name='hospedagem'),
    path('about/', AboutViews.as_view(), name='about'),
    path('page1/', Page1Views.as_view(), name='page1'),
    path('page2/', Page2Views.as_view(), name='page2'),
    path('page3/', Page3Views.as_view(), name='page3'),
    
]
