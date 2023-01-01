from django.shortcuts import render


# Create your views here.
'''
Отображет главную страницу сайта
'''
def homeview(requests):
    return render(requests, 'PetitionApp/index.html')
