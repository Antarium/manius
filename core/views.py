#coding: utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
import datetime
import json

from django.views.generic.edit import UpdateView
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.http.response import HttpResponse, Http404
from django.core.exceptions import ObjectDoesNotExist
from django.core.context_processors import csrf
from django.views.decorators.csrf import csrf_exempt

from core.forms import LoginForm, VidgetForm
from core.models import NegativeTarget, ExtensionUser, Account
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tech.forms import SupportForm

# Create your views here. 

class IndexView(TemplateView):
	#template_name = None
	def get(self, request, *args, **kwargs):
		self.form_support = SupportForm(initial={'feedback_mail': request.user.email})
		self.ext_user = ExtensionUser.objects.filter(user=request.user).first()
		return super(IndexView, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['target_list'] = NegativeTarget.objects.filter(user_id=0).order_by('id')
		context['form_support'] = self.form_support
		user = self.request.user
		if self.ext_user:
			context['user_capital'] = self.ext_user
			context['entry_level'] = self.ext_user.entry_level
			context['redzone'] = self.ext_user.redzone
			context['greenzone'] = self.ext_user.greenzone
		return context

@login_required
def ChangeBalance(request):
	if request.method == 'POST':
		num_negative = int(request.POST.get('negative'))
		num_positive = int(request.POST.get('positive'))
		target = request.POST.get('target')
		user = request.user
		ext_user = ExtensionUser.objects.get(user=user)
		ext_user.change_balance(num_positive-num_negative, target)
	return redirect('/')

@login_required
@csrf_exempt 
def GetData(request):
	if request.is_ajax():
		answer = {}
		user_id = request.user.id
		accounts = Account.objects.filter(user_id=user_id)
		answer['account_list'] = []
		for account in accounts:
			answer['account_list'].append({	'day':account.created.date().day, 'month':account.created.date().month,
											'year':account.created.date().year, 'date_string':'{}'.format(account.created.date()), 
											'change':account.change, 'target':account.target, 
											'balance':account.balance})
		return HttpResponse(json.dumps(answer), content_type = "application/json")
	return redirect('/')

class LoginView(TemplateView):
	template_name = 'login.html'
	form = None

	def get(self, request, *args, **kwargs):
		self.form = LoginForm()
		return super(LoginView, self).get(request, *args, **kwargs)
	def get_context_data(self, **kwargs):
		context = super(LoginView, self).get_context_data(**kwargs)
		context['form'] = self.form
		return context
	def post(self, request, *args, **kwargs):
		self.form = LoginForm(request.POST)
		if self.form.is_valid():
			user = authenticate(username=self.form.cleaned_data['username'],
				password=self.form.cleaned_data['password'])
			if user is not None:
				if user.is_active:
					login(request, user)
					return redirect('index')
				else:
					return super(LoginView, self).get(request, *args, **kwargs)
			else:
				return super(LoginView, self).get(request, *args, **kwargs)
		else:
			return super(LoginView, self).get(request, *args, **kwargs)

def RegView(request, reg = 'no'):
	args = {}
	args.update(csrf(request))
	args['reg_status'] = reg
	args['form'] = UserCreationForm()
	if request.POST:
		new_user_form = UserCreationForm(request.POST)
		if new_user_form.is_valid():
			new_user_form.save()
			new_user = authenticate(username=new_user_form.cleaned_data['username'], password=new_user_form.cleaned_data['password2'])
			login(request, new_user)
			return redirect('/reg/yes/')
		else:
			args['form'] = new_user_form
			return render_to_response('reg.html', args)
	else:
		return render_to_response('reg.html', args)

@login_required
def ExtInfoUser(request):
	args = {}
	args.update(csrf(request))
	if request.POST:
		data = request.POST.copy()
		user = request.user
		if data.get('id_email'):
			user.email = data.get('id_email')
			user.save()
		balance = int(data.get('id_balance'))
		entry_level = int(data.get('id_entry_level'))
		redzone = int(data.get('id_redzone'))
		greenzone = int(data.get('id_greenzone'))
		ext_user = ExtensionUser()
		ext_user.user_id = user.id
		ext_user.balance = balance
		ext_user.entry_level = entry_level
		ext_user.redzone = redzone
		ext_user.greenzone = greenzone
		ext_user.save()
	return redirect('/')

class ChangeAccount(TemplateView):
	def post(self, request, *args, **kwargs):
		new_password = request.POST.get('name_password')
		user_email = request.POST.get('new_email')
		user = request.user
		if new_password:
			user.set_password(new_password)
		user.email = user_email
		user.save()
		return redirect ('index')


class ChangeVidget(TemplateView):
	def post(self, request, *args, **kwargs):
		ext_user = get_object_or_404(ExtensionUser, user=request.user)
		ext_user.entry_level = request.POST.get('entry_level')
		ext_user.redzone = request.POST.get('redzone')
		ext_user.greenzone = request.POST.get('greenzone')
		ext_user.save()
		return redirect('index')

"""
class ChangeVidget(UpdateView):
	form_class = VidgetForm()
	queryset = ExtensionUser.objects.all()
	success_url = '/'

	def form_valid(self, form):
		#qs = self.queryset.filter(user=request.user).first()
		#qs.update(**form.cleaned_data)
		return redirect(self.get_succes_url())
"""


