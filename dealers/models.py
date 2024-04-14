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
    house_number = models.CharField(max_length=50, verbose_name='Номер дома')

    def __str__(self):
        return f'{self.email} -({self.country}, {self.city}, {self.street}, {self.house_number})'

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'


class Products(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название продукта')
    model = models.CharField(max_length=150, verbose_name='Модель продукта')
    market_launch_date = models.DateTimeField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f'{self.title} - ({self.model}, {self.market_launch_date})'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Factory(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название завода')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукты')
    provider = models.OneToOneField('self', on_delete=models.CASCADE, verbose_name='Поставщик', **NULLABLE)
    time_to_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Задолженность', default=0)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'завод'
        verbose_name_plural = 'заводы'


class RetailNetwork(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название розничной сети')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукты')
    provider = models.ForeignKey(Factory, on_delete=models.PROTECT, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Задолженность')
    time_to_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class IndividualEntrepreneur(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    contacts = models.ForeignKey(Contacts, on_delete=models.CASCADE, verbose_name='Контакты')
    products = models.ForeignKey(Products, on_delete=models.PROTECT, verbose_name='Продукты')
    provider = models.ForeignKey(RetailNetwork, on_delete=models.PROTECT, verbose_name='Поставщик')
    time_to_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    debt = models.DecimalField(max_digits=12, decimal_places=2, verbose_name='Задолженность')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Предприниматель'
        verbose_name_plural = 'Предприниматели'
