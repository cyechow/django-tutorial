from django.urls import path

from . import views

app_name = 'calculator'
url_patterns = [
    path('',views.IndexView.as_view(), name='index'),
]