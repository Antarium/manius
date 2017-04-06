#coding: utf-8
from django.shortcuts import render
from django.views.generic.base import TemplateView

from django.shortcuts import redirect

from tech.forms import SupportForm

class AddMessage(TemplateView):
	def post(self, request, *args, **kwargs):
		form_support = SupportForm(request.POST)
		if form_support.is_valid():
			form_support.save()
		return redirect('index')