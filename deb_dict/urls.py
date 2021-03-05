from typing import List, Union

from django.urls import path, URLResolver, URLPattern
from .views import index, word, commingsoon

urlpatterns  = [
    path("ind/", index, name='index'),
    path("word/", word, name='word'),
    path("", commingsoon, name='commingsoon')

]
