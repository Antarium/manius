#coding: utf-8
from django.db import models

# Create your models here.

class TechSupport(models.Model):
	TYPE_MESSAGE = (
		(1, 'Предложения'),
		(2, 'Ошибка'),
	)
	class Meta:
		db_table = 'tech_support'
		verbose_name = 'Техподдержка'
		verbose_name_plural = 'Техподдержка'
		ordering = ['-created']
	type_message = models.PositiveSmallIntegerField(choices = TYPE_MESSAGE, default = 2, db_index = True, 
		verbose_name = 'Тип сообщения')
	feedback_mail = models.EmailField(null = True, blank = True, verbose_name = 'e-mail для обратной связи')
	caption = models.CharField(max_length = 100, default = '', blank = True, null = True, verbose_name = 'Заголовок')
	text = models.TextField(default = '', verbose_name = 'Текст сообщения')
	created = models.DateTimeField(auto_now = False, auto_now_add = True, verbose_name = 'Дата обращения')
	files = models.ImageField(upload_to = 'upload/%Y/%m/%d', null = True, blank = True, verbose_name = 'Изображение')
	closed = models.BooleanField(default=False, verbose_name = 'Задача закрыта', editable = False)

	def __str__(self):
		return self.caption

class ProcessSupport(models.Model):
	STATE = (
		(1, 'В работе'),
		(0, 'Готово'),
	)
	class Meta:
		db_table = 'process_support' 
		verbose_name = 'Обработка обращения'
		verbose_name_plural = 'Обработка обращений'
	message = models.ForeignKey(TechSupport, on_delete = models.PROTECT, verbose_name = 'Обращение')
	text = models.TextField(default = '', verbose_name = 'Комментарий')
	state = models.PositiveIntegerField(choices = STATE, default = 1, verbose_name = 'Состояние завки')
	created = models.DateTimeField(auto_now=True, auto_now_add=False, verbose_name = 'Дата обработки')

	def __str__(self):
		return self.text

	def save(self):
		super(ProcessSupport, self).save()
		if self.state == 0:
			self.message.closed = True
			self.message.save()
		else:
			if self.message.closed == True:
				self.message.closed = False
				self.message.save()