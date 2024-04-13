from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Countries(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название страны')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'


class Contacts(models.Model):
    email = models.EmailField(verbose_name='Email')
    country = models.ForeignKey(Countries, on_delete=models.PROTECT, verbose_name='Страна')
    city = models.TextField(verbose_name='Город')
    street = models.TextField(verbose_name='Улица')
    house_number = models.PositiveSmallIntegerField(verbose_name='Номер дома')

    def __str__(self):
        return f'{self.email} -({self.country}, {self.city}, {self.street}, {self.house_number})'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

