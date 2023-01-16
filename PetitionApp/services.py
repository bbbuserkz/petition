from django.http import Http404
from django.shortcuts import get_object_or_404
from django.utils import timezone
import datetime
from django.core.paginator import Paginator

from .models import PetitionModel, PetitonCategoryModel


class PetitonClass:
    def get_last_pet(self, request, count: int):
        # Last added petitions
        try:
            petitions = PetitionModel.objects.all().order_by('-id')[:count]
        except:
            raise Http404()
        return petitions

    def get_active_pet(self, request, count: int):
        now = datetime.datetime.now(tz=timezone.utc)
        try:
            petitions = PetitionModel.objects.filter(status=True, dateEnd__gte=now).order_by('-id')[:count]
        except:
            raise Http404()
        return petitions

    def get_pet(self, request, petid: int):
        petition = get_object_or_404(PetitionModel, pk=petid)
        return petition

    def get_popular_pet(self, request, count: int):
        pass

    def get_categories(self, request, count: int):
        try:
            if count:
                categories = PetitonCategoryModel.objects.filter(status=True)[:count]
            else:
                categories = PetitonCategoryModel.objects.filter(status=True)
        except:
            raise Http404()
        return categories

    def get_category(self, request, catid):
        category = get_object_or_404(PetitonCategoryModel, pk=catid)
        return category

    def get_pets_paginator(self, request, itemcount: int):
        now = datetime.datetime.now(tz=timezone.utc)
        items = PetitionModel.objects.filter(status=True, dateEnd__gte=now).order_by('-id')
        paginator = Paginator(items, itemcount)
        page_number = request.GET.get('page')
        if not page_number:
            page_number = 1
        page_obj = paginator.get_page(page_number)
        return page_obj

    def get_pets_popular_paginator(self, request, itemcount: int):
        now = datetime.datetime.now(tz=timezone.utc)
        items = PetitionModel.objects.filter(status=True, dateEnd__gte=now).order_by('-id')
        paginator = Paginator(items, itemcount)
        page_number = request.GET.get('page')
        if not page_number:
            page_number = 1
        page_obj = paginator.get_page(page_number)
        return page_obj