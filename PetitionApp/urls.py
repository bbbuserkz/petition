from .views import homeview

from django.urls import path

urlpatterns = [
    path('', homeview, name='home_url'),
]