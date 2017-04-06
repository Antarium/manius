#coding: utf-8
from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class ExtensionUser(models.Model): 
	class Meta:
		db_table = 'ext_user'
		verbose_name = 'Расширение таблицы User'
		verbose_name_plural = 'Расширения таблицы User'
	user = models.OneToOneField(User)
	entry_level = models.IntegerField(default = 0, verbose_name = 'Средняя прибыль')
	redzone = models.IntegerField(default = 0, verbose_name = 'Красная зона', 
		help_text = 'Сумма ден. средств, ниже которой нельзя опускаться')
	greenzone = models.IntegerField(default = 1000, verbose_name = 'Зона комфорта',
		help_text = """выше этой суммы - все в порядке с финансами, ниже и до красной зоны - 
		минимальная зона комфорта""")
	balance = models.IntegerField(default = 0, verbose_name = 'Денег на счету', editable = False)

	def __str__(self):
		return self.user.username

	def change_balance(self, num_change, msg = None):
		self.balance = self.balance + num_change
		self.save(update_fields = ['balance'])
		account = Account(user_id = self.user.id, change = num_change, target = msg, balance = self.balance)
		account.save()


class Account(models.Model):
	class Meta:
		db_table = 'account_user'
		verbose_name = 'История счета'
		verbose_name_plural = 'История счета'
	user_id = models.PositiveIntegerField(verbose_name = 'id пользователя')
	created = models.DateTimeField(auto_now=False, auto_now_add=True, editable=False, verbose_name = 'дата')
	change = models.IntegerField(default = 0, verbose_name = 'изменение счета')
	target = models.CharField(max_length=50, default = 'Не указано', verbose_name = 'цель изменения счета')
	balance = models.IntegerField(verbose_name = 'Денег на счету')

class NegativeTarget(models.Model):
	class Meta:
		db_table = 'negative_target'
		verbose_name = 'Цель снятия средств'
		verbose_name_plural = 'Цели снятия средств'
	title = models.CharField(max_length=50, default = 'не указано')
	status = models.BooleanField(default=False, verbose_name='Общая(True) цель или частная(False)')
	user_id = models.PositiveIntegerField(verbose_name = 'id пользователя')
 
	def __str__(self):
		return self.title
