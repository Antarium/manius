from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

from core.models import ExtensionUser, Account, NegativeTarget

# Register your models here.

class ExtensionUserInline(admin.StackedInline):
	model = ExtensionUser
	can_delete = False
	verbose_name_plural = 'Дополнения к таблице User'

class UserAdmin(UserAdmin):
	inlines = (ExtensionUserInline, )

class AccountAdmin(admin.ModelAdmin):
	list_display = ('user_id','created','change', 'target', 'balance',)
	list_per_page = 10
	list_max_show_all = 50
	#date_hierarchy = 'created'
	list_filter = ('user_id', 'target', )

class NegativeTargetAdmin(admin.ModelAdmin):
	list_display = ('id', 'title', 'status', 'user_id',)

#admin.site.register(ExtensionUser)
admin.site.register(Account, AccountAdmin)
admin.site.register(NegativeTarget, NegativeTargetAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
	