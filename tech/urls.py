from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView

from tech.views import AddMessage


urlpatterns = [
	url(r'^new_message/$', AddMessage.as_view(), name='add_message'),
	url(r'^info/$', TemplateView.as_view(template_name='info.html'), name='info_page'),
	url(r'^downloads/$', TemplateView.as_view(template_name='downloads.html'), name='downloads_page'),
]
