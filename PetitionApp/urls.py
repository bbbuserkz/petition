from .views import homeview, petitionDetailView, petitionAllView, petitionPopularView, biotest

from django.urls import path

urlpatterns = [
    path('petition_detail/<int:petid>/', petitionDetailView, name='pet_url'),
    path('petition_all/', petitionAllView, name='petall_url'),
    path('petition_popular/', petitionPopularView, name='petpopular_url'),
    path('test/', biotest, name="test_url"),
    path('', homeview, name='home_url'),

]