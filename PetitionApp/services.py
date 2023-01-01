from django.http import Http404
from django.shortcuts import get_object_or_404


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
        try:
            petitions = PetitionModel.objects.filter(status=True).order_by('-id')[:count]
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

    def get_category(self, request, catid):
        category = get_object_or_404(PetitonCategoryModel, pk=catid)
        return category
