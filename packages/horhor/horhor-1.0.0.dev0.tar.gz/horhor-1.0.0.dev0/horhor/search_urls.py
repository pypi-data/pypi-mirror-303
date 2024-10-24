from django.urls import path
from horhor.views import search

urlpatterns = [
    path("", search, name="crx_search"),
]
