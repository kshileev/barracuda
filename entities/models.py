# -*- coding: utf-8 -*-
from django.db import models

LEGAL_ENTITY_TYPE = (
    ('BARU',	'Барракуда-Россия'),
    ('BAFO',	'Барракуда-Зарубеж'),
    ('BACL',	'Барракуда-Kлиент'),
    ('PRGM',	'Программа'),
    ('CLNT',	'Клиент'),
    ('VNDR',	'Поставщик'),
    ('OTHR',	'Другое')
)

PERSON_TYPE = (
    ('CLNT', 'клиент'),
    ('CURR', 'перевозчик')
)

class LegalEntity(models.Model):
    title		= models.CharField(verbose_name = 'название', max_length = 255)
    address		= models.TextField(verbose_name = 'адрес', max_length = 512)
    type		= models.CharField(verbose_name = 'тип', max_length = 4, choices = LEGAL_ENTITY_TYPE)

    def __unicode__(self):
        return self.title

class Person(models.Model):
    name = models.CharField(max_length = 64, unique = True, verbose_name = 'имя')
    type = models.CharField(verbose_name='тип', max_length=4, choices= PERSON_TYPE)

    def __unicode__(self):
        return self.name
