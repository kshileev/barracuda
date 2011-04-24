# -*- coding: utf-8 -*-
from django.db import models

from entities.models import LegalEntity, Person
from finances.models import CURRENCY, PAYMENT

COUNTRIES = (
    ('RU', 'Россия'),
    ('DE', 'Германия'),
    ('ND', 'Нидерланды'),
    ('US', 'США'),
    ('CN', 'Китай')
)

POINTS = (
    ('ORDR', 'Заказ'),
    ('LOAD', 'Загрузка'),
    ('CSAR', 'Таможня-прибытие'),
    ('CSDP', 'Таможня-убытие'),
    ('ULAR', 'Выгрузка-прибытие'),
    ('UL',	 'Выгрузка')
)


class Conveyance(models.Model):
    class Meta:
        verbose_name = 'перевозка'
        verbose_name_plural = 'перевозки'

    truck = models.CharField(verbose_name='номер машины', max_length = 16)
    carrier = models.ForeignKey(Person, verbose_name = 'перевозчик')
    is_active = models.BooleanField('в пути', default = True)
    idle_reason = models.CharField('простой-причина', max_length = 128, blank = True)
    comment = models.TextField('комментарий', blank = True)

    def __unicode__(self):
        return unicode(self.truck)

class ConveyancePoint(models.Model):
    class Meta:
        verbose_name = 'точка перевозки'
        verbose_name_plural = 'точки перевозки'
        ordering = ('timestamp',)

    conveyance = models.ForeignKey(Conveyance, verbose_name = 'перевозка', related_name = 'points')
    timestamp = models.DateTimeField(verbose_name = 'время')
    location = models.CharField(verbose_name = 'страна', max_length = 4, choices = COUNTRIES)
    type = models.CharField(verbose_name ='тип', max_length = 4, choices = POINTS)

class Warehouse(models.Model):
    class Meta:
        verbose_name = 'склад'
        verbose_name_plural = 'склады'

    name = models.CharField(verbose_name = 'название', max_length = 255)
    address = models.CharField(verbose_name = 'адрес', max_length = 512)

    def __unicode__(self):
        return self.name

class Customs(models.Model):
    class Meta:
        verbose_name = 'таможня'
        verbose_name_plural = 'таможни'

    number = models.IntegerField(verbose_name='идентификатор', max_length=8)
    name = models.CharField(verbose_name = 'название', max_length = 255)
    address = models.CharField(verbose_name = 'адрес', max_length = 512)

    def __unicode__(self):
        return self.number

class CCD(models.Model):
    class Meta:
        verbose_name = 'ГТД'
        verbose_name_plural = 'ГТД'

    #we have few CCD per conveyance
    conveyance = models.OneToOneField(Conveyance, verbose_name = 'перевозка', null = False)

    customs = models.ForeignKey(Customs, verbose_name='таможня')
    date = models.DateField(verbose_name = 'дата')
    unique_number = models.CharField(verbose_name = 'номер', max_length = 8, unique = True)

    exporter = models.ForeignKey(LegalEntity, verbose_name = 'экспортер', related_name='exporter')
    importer = models.ForeignKey(LegalEntity, verbose_name = 'импортер', related_name='importer')

    country = models.CharField(verbose_name='Страна отправления', max_length=2, choices=COUNTRIES)
    truck = models.CharField(verbose_name='машина', max_length = 10)
    
    currency = models.CharField(verbose_name='валюта', max_length = 3, choices = CURRENCY)
    total_sum = models.DecimalField(verbose_name = 'общая сумма по счету', max_digits = 11, decimal_places = 4)
    exchange_rate = models.DecimalField(verbose_name = 'курс валюты', max_digits = 5, decimal_places = 4)

    corrected_cost = models.DecimalField(verbose_name = 'КТС', max_digits = 11, decimal_places = 4)

    def __unicode__(self):
        return u'ГТД {0}/{1}/{2}'.format(self.customs, self.date, self.unique_number)

class CargoExpenseType(models.Model):
    class Meta:
        verbose_name = 'статья расходов'
        verbose_name_plural = 'статьи расходов'

    name = models.CharField(verbose_name = 'наименование', max_length = 64)

    def __unicode__(self):
        return self.name

class CargoExpense(models.Model):
    class Meta:
        verbose_name = 'расход'
        verbose_name_plural = 'расходы'

    cargo = models.ForeignKey(Conveyance, verbose_name = 'перевозка')
    models.DecimalField(verbose_name = 'сумма', max_digits = 11, decimal_places = 4)
    currency = models.CharField(verbose_name='валюта', max_length = 3, choices = CURRENCY)
    payment = models.CharField(verbose_name = 'нал/безнал', max_length = 4, choices = PAYMENT)
    type = models.ForeignKey(CargoExpenseType, verbose_name = 'статья расхода')
