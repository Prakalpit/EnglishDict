from typing import List, Union

from django.urls import path, URLResolver, URLPattern
from .views import index, word

urlpatterns  = [
    path("", index, name='index'),
    path("word/", word, name='word'),
]
