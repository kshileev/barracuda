# -*- coding: utf-8 -*-
from datetime import datetime
from django.db import models
from entities.models import LegalEntity

CURRENCY = (
	('RUB', 'Рубль'),
	('EUR', 'Евро'),
	('USD', 'Доллар'),
	('CHF', 'Швейцарский Франк'),
    ('GBP', 'Британский фунт')
)

PAYMENT = (
    ('cash', 'Наличный'),
    ('ncas', 'Безналичный'),
)

PAYMENT2 = (
    ('CASH', 'наличный'),
    ('NCSH', 'безналичный'),
    ('WALT', 'черная касса')
)

class Bank(models.Model):
	class Meta:
		verbose_name = 'банк' 
		verbose_name_plural = 'банки'
	
	name = models.TextField('название', max_length=128)
	is_foreign = models.BooleanField('иностранный', default = False)
	
	def __unicode__(self):
		return u'{0}'.format(self.name)

class Account(models.Model):
	class Meta:
		verbose_name = 'счет'
		verbose_name_plural = 'счета'
	

	no = models.CharField('номер', max_length = 24, unique = True)
	currency = models.CharField(name='валюта', max_length = 3, choices = CURRENCY)
	comment = models.TextField('комментарий', blank = True)
	bank = models.ForeignKey(Bank, related_name = '+', verbose_name = 'банк')
	type = models.CharField(verbose_name = 'тип', choices = PAYMENT2, max_length = 4)
	contractor = models.ForeignKey(LegalEntity, verbose_name = 'юрлицо')
	
	def __unicode__(self):
		return u'{0} {1} {2}'.format(self.currency, self.no, "" if (self.bank is None) else self.bank.name)

class Transaction(models.Model):
	class Meta:
		verbose_name = 'транзакция'
		verbose_name_plural = 'транзакции'
	
	timestamp = models.DateTimeField(verbose_name = 'время', default = datetime.now)
	account_from = models.ForeignKey(Account, related_name = '+', verbose_name = 'отправитель')
	account_to = models.ForeignKey(Account, related_name = '+', verbose_name = 'получатель')
	amount = models.DecimalField(verbose_name = 'сумма', max_digits = 11, decimal_places = 4)
	currency = models.CharField(name='валюта', max_length = 3, choices = CURRENCY)

	def __unicode__(self):
		return u'{0} {1}'.format(self.account_from, self.amount)