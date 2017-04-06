from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from core.models import ExtensionUser

class LoginForm(forms.Form):
	username = forms.CharField(label='Логин ')
	password = forms.CharField(widget=forms.PasswordInput, label='Пароль')

class RegForm(UserCreationForm):
	def is_valid(self):
		return super(RegForm, self).is_valid()

class VidgetForm(forms.ModelForm):
	class Meta:
		model = ExtensionUser
		fields = '__all__'
		exclude = ['balance', 'user']

