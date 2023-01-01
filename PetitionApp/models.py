from django.db import models
from ckeditor.fields import RichTextField
from pytils import translit
import os
from datetime import datetime

from SignApp.models import SignCategoryModel

# Create your models here.
class PetitonCategoryModel(models.Model):
    # модель категории петиции
    title = models.CharField(max_length=512, verbose_name="Наименование категории")
    status = models.BooleanField(default=False, verbose_name='Активация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Категория петиции"
        verbose_name_plural = "Категории петиции"


class PetitionModel(models.Model):
    def get_file_path(self, filename):
        name, ext = os.path.splitext(filename)
        path = ''.join(["static/img/petitions/", translit.slugify(name)])
        return '{0}{1}'.format(path, ext)

    title = models.CharField(max_length=512, verbose_name='Наименование петиции')
    description = RichTextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to=get_file_path, blank=True,
                              null=True, verbose_name="Картинка петции")
    petCategory = models.ForeignKey('PetitonCategoryModel', null=True, on_delete=models.CASCADE,
                                 blank=True, verbose_name="Категория петиции")
    signCategory = models.ForeignKey('SignApp.SignCategoryModel', null=True, on_delete=models.CASCADE,
                                 blank=True, verbose_name="Метод идентификации")
    dateCreate = models.DateTimeField(default=datetime.now,
                                      verbose_name="Дата создания записи")
    dateStart = models.DateTimeField(default=datetime.now, null=True,
                                     blank=True, verbose_name="Дата начала петиции")
    dateEnd = models.DateTimeField(default=datetime.now, null=True,
                                   blank=True, verbose_name="Дата завершения петиции")
    author = models.CharField(max_length=512, blank=True,
                              null=True, verbose_name="Автор петиции")
    authorEmail = models.CharField(max_length=256, blank=True,
                                   null=True, verbose_name="Email Автора петиции")
    authorContact = models.CharField(max_length=256, blank=True,
                                     null=True, verbose_name="Контактные данные автора петици")
    signSum = models.IntegerField(default=1, verbose_name="Заказанное количество подписей")
    onMain = models.BooleanField(default=False, verbose_name="Вывести на главный баннер")
    status = models.BooleanField(default=False, verbose_name="Статус отображения на сайте")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Петциия"
        verbose_name_plural = "Петции"
