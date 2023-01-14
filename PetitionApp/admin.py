from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(PetitionModel)
class PetitionModelAdmin(admin.ModelAdmin):
    readonly_fields = ["dateCreate", ]
    list_display = ['title', 'petCategory', 'dateStart', 'dateEnd']

@admin.register(PetitonCategoryModel)
class PetitonCategoryModelAdmin(admin.ModelAdmin):
    pass
