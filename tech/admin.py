from django.contrib import admin

from tech.models import TechSupport, ProcessSupport

# Register your models here.

class ProcessSupportInline(admin.StackedInline):
	model = ProcessSupport
	can_delete = False
	verbose_name_plural = 'Обработка запроса в тех.поддержку'

class TechSupportAdmin(admin.ModelAdmin):
	list_display = ('caption', 'text', 'files', 'type_message', 'feedback_mail', 'closed', 'created',)
	ordering = ('-created', 'closed')
	list_per_page = 10
	list_max_show_all = 50
	list_filter = ('type_message',)
	readonly_fields = ('created', 'closed',)
	search_fields = ('caption', 'feedback_mail',)
	inlines = (ProcessSupportInline, )


admin.site.register(TechSupport, TechSupportAdmin)
admin.site.register(ProcessSupport)
