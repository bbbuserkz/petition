from django.db import models

from PetitionApp.models import PetitionModel


# Create your models here.

class ViewerModel(models.Model):
    """Пользователь, переадресация на страницу аутентификации Айту
    * для получения данных для составления документов подписания ИИН ФИО Место ИД
    """
    ip = models.GenericIPAddressField(verbose_name='IP пользователя')
    petCategory = models.CharField(max_length=512, null=True, blank=True, verbose_name="Тип страницы")
    petition = models.ForeignKey('PetitionApp.PetitionModel', on_delete=models.CASCADE,
                                 null=True, verbose_name="Петиция")
    date_view = models.DateTimeField(auto_now_add=True, verbose_name="Дата просмотра")

    def __str__(self):
        return self.ip

    def get_user_ip(self, request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip

    class Meta:
        verbose_name = 'Посещения'
        verbose_name_plural = 'Посещения'
