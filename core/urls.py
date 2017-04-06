from django.conf.urls import patterns, url
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from core.views import IndexView, LoginView, ChangeBalance, GetData, RegView, ExtInfoUser, \
						ChangeAccount, ChangeVidget

urlpatterns = [
	url(r'^login/', LoginView.as_view(), name='login'),
	url(r'^logout/', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}, name = 'logout'),
	url(r'^change_balance/$', ChangeBalance, name='change_balance'),
	url(r'^get_full_data/', GetData, name='get_data'),
	url(r'^reg/save_info/$', ExtInfoUser, name='ext_info_user'),
	url(r'^reg/(?P<reg>\w+)/$', RegView, name='reg_view_info'),
	url(r'^reg/$', RegView, name='reg_view'),
	url(r'^change_account/$', ChangeAccount.as_view(), name='change_account'),
	url(r'^change_vidget1/$', ChangeVidget.as_view(), name='change_account'),
	url(r'^mobile/$', login_required(IndexView.as_view(template_name = 'mobile/index.html')), name='mobile_index'),
	url(r'^$', login_required(IndexView.as_view(template_name = 'index.html')), name='index'),
]
