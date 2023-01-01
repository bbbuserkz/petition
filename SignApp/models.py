from django.db import models
from PetitionApp.models import *
from UserApp.models import RespondentModel


# Create your models here.

class SignCategoryModel(models.Model):
    # модель категории петиции
    # sms - sms identification, biometric - bio ident
    title = models.CharField(max_length=512, verbose_name="Наименование категории")
    inlineCode = models.CharField(max_length=512, verbose_name="Наименование (системно)")
    status = models.BooleanField(default=False, verbose_name='Активация')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Метод идентификации"
        verbose_name_plural = "Методы идентификации"


class SignIdentificationModel(models.Model):
    # модель категории петиции
    # sms - sms identification, biometric - bio ident
    def get_file_path(self, filename):
        name, ext = os.path.splitext(filename)
        path = ''.join(["static/img/liveness3d/", translit.slugify(name)])
        return '{0}{1}'.format(path, ext)

    identificationMethod = models.ForeignKey('SignCategoryModel', on_delete=models.CASCADE,
                                             null=True, verbose_name="Метод идентификации")
    respondent = models.ForeignKey('UserApp.RespondentModel', on_delete=models.CASCADE,
                                   null=True, verbose_name="Респондент")
    petition = models.ForeignKey('PetitionApp.PetitionModel', on_delete=models.CASCADE,
                                 null=True, verbose_name="Петиция")
    liveness3d = models.ImageField(upload_to=get_file_path, null=True, blank=True,
                                   verbose_name='Фото биометрия')
    redirect_code = models.CharField(max_length=500, blank=True, verbose_name="Данные пользователя (зашифрованные данные)")
    access_token = models.CharField(max_length=1200, blank=True, verbose_name="Access_token")
    doc1 = models.FileField(upload_to=get_file_path, null=True, blank=True,
                            verbose_name='Петииця на подпись')
    signId1 = models.IntegerField(default=2021, null=True, verbose_name="ИД загруженного документа в service")
    signSms1 = models.IntegerField(default=2021, null=True, verbose_name="SMS для идентификации")
    signSmsId1 = models.CharField(max_length=256, null=True, verbose_name="ID SMS идентификации")
    doc1s = models.FileField(upload_to=get_file_path, null=True, blank=True,
                             verbose_name='Петиция (Подписанный)')
    signStatus = models.BooleanField(default=False, verbose_name="Статус подписания")
    signDate = models.DateField(null=True, blank=True, verbose_name="Дата подписи")

    def __str__(self):
        return str(self.respondent.mobileNumber)

    class Meta:
        verbose_name = "Идентитфикация и подпись"
        verbose_name_plural = "Идентитфикация и подпись"


class SignUserModel(models.Model):
    respondent = models.ForeignKey('UserApp.RespondentModel', on_delete=models.CASCADE,
                                   null=True, verbose_name="Респондент")
    petition = models.ForeignKey('PetitionApp.PetitionModel', on_delete=models.CASCADE,
                                 null=True, verbose_name="Петиция")
    dateAdd = models.DateTimeField(auto_now_add=True, verbose_name="Дата подписания петиции")
    signCategory = models.ForeignKey('SignCategoryModel', null=True, on_delete=models.CASCADE,
                                     blank=True, verbose_name="Метод идентификации")
    ip = models.GenericIPAddressField(null=True, blank=True, verbose_name="IP адрес респондента")
    signIdentification = models.ForeignKey('SignIdentificationModel', null=True, on_delete=models.CASCADE,
                                           blank=True, verbose_name="Идентификация пользователя")
    status = models.BooleanField(default=True, verbose_name="Результат подписи")

    def __str__(self):
        return str(self.respondent.mobileNumber)

    class Meta:
        verbose_name = "Подписанные петиции"
        verbose_name_plural = "Подписанные петиции"
