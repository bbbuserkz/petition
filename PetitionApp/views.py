from django.shortcuts import render

from .services import PetitonClass

# Create your views here.
'''
Отображет главную страницу сайта
'''
def homeview(request):
    petition_class = PetitonClass()
    petitions = petition_class.get_active_pet(request, 6)
    if petitions.count()<4:
        return render(request, 'PetitionApp/index_wide.html', context={'pets': petitions, })
    else:
        return render(request, 'PetitionApp/index.html', context={'pets': petitions, })


def petitionDetailView(request, petid):
    petition_class = PetitonClass()
    petition = petition_class.get_pet(request, petid)
    return render(request, 'PetitionApp/petition.html', context={'pet': petition, })

def petitionAllView(request):
    petition_class = PetitonClass()
    petitions = petition_class.get_pets_paginator(request, 10)
    return render(request, 'PetitionApp/petitionAll.html', context={"items": petitions, })

def petitionPopularView(request):
    petition_class = PetitonClass()
    petitions = petition_class.get_pets_popular_paginator(request, 10)
    return render(request, 'PetitionApp/petitionPopular.html', context={"items": petitions, })

def biotest(request):
    return render(request, 'PetitionApp/biotest.html')