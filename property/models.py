from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):

    new_building = models.BooleanField(verbose_name='Новостройка',
        default=False,
        null=True,
        db_index=True)
    created_at = models.DateTimeField(
        verbose_name='Когда создано объявление',
        default=timezone.now,
        db_index=True)

    description = models.TextField(verbose_name='Текст объявления', blank=True)
    price = models.IntegerField(verbose_name='Цена квартиры', db_index=True)

    town = models.CharField(
        verbose_name='Город, где находится квартира',
        max_length=50,
        db_index=True)
    town_district = models.CharField(
        verbose_name='Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное')
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4')
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж')

    rooms_number = models.IntegerField(
        verbose_name='Количество комнат в квартире',
        db_index=True)
    living_area = models.IntegerField(
        verbose_name='количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True)

    has_balcony = models.NullBooleanField(verbose_name='Наличие балкона', db_index=True)
    active = models.BooleanField(verbose_name='Активно-ли объявление', db_index=True)
    construction_year = models.IntegerField(
        verbose_name='Год постройки здания',
        null=True,
        blank=True,
        db_index=True)
    liked_by = models.ManyToManyField(User, related_name="liked_flat", blank=True)

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Disliker(models.Model):

    disliker = models.ForeignKey(
        User,
        related_name='dislikers',
        verbose_name='Кому не понравилась квартира',
        on_delete=models.CASCADE)
    flat = models.ForeignKey(
        Flat,
        related_name='dislikers',
        verbose_name='Квартира, которая не понравилась',
        on_delete=models.CASCADE)
    message = models.TextField(blank=False)

    def __str__(self):
        return f'{self.disliker}, {self.flat.town} ({self.flat.address}р.)'


class Owner(models.Model):
    fullname = models.CharField(
        verbose_name='ФИО владельца',
        max_length=200,
        db_index=True)
    phonenumber = models.CharField(verbose_name='Номер владельца', max_length=20)
    phonenumber_normalized = PhoneNumberField(
        verbose_name='Нормализованный номер владельца',
        null=True,
        blank=True
    )
    flats = models.ManyToManyField(
        Flat,
        related_name='owners',
        verbose_name='Квартиры в собственности'
    )

    def __str__(self):
        return self.fullname


