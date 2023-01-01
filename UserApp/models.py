from django.db import models
from datetime import datetime

# Create your models here.
class RespondentModel(models.Model):
    """
    ПОДПИСАНТЫ ПЕТИЦИИ
        status используется для отображения актуальности данных пользователя
        При изменении данных пользователя статус меняется на False и
        создается новый пользователь в текущей таблице
    """
    firstName = models.CharField(max_length=250, verbose_name="Имя")
    secondName = models.CharField(max_length=250, verbose_name="Фамилия")
    identifyNumber = models.CharField(max_length=12, verbose_name="ИИН/БИН")
    mobileNumber = models.CharField(max_length=11, verbose_name="Мобильный номер")
    email = models.EmailField(max_length=120, blank=True, null=True, verbose_name="email")
    dateCreate = models.DateTimeField(default=datetime.now,
                                      verbose_name="Дата создания записи")
    status = models.BooleanField(default=True, verbose_name="Актуальность данных")

    def __str__(self):
        return self.identifyNumber

    class Meta:
        verbose_name = "Респондент"
        verbose_name_plural = "Респонденты"
