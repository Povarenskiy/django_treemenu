from django.urls import path
from . import views
from django.urls import re_path


urlpatterns = [
    re_path('(?P<path>)', views.index, name='index'),
]
