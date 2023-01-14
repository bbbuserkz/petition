from django.shortcuts import render

from .services import PetitonClass

# Create your views here.
'''
Отображет главную страницу сайта
'''
def homeview(requests):
    petition_class = PetitonClass()
    petitions = petition_class.get_active_pet(requests, 4)
    return render(requests, 'PetitionApp/index.html', context={'pets': petitions, })
