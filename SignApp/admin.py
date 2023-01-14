from django.contrib import admin

from .models import *
# Register your models here.

@admin.register(SignUserModel)
class SignUserModelAdmin(admin.ModelAdmin):
    pass

@admin.register(SignIdentificationModel)
class SignIdentificationModelAdmin(admin.ModelAdmin):
    pass

@admin.register(SignCategoryModel)
class SignCategoryModelAdmin(admin.ModelAdmin):
    pass
