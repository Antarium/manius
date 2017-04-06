import re
from django.http import HttpResponseRedirect
from django.conf import settings 

class DetectMobileVersion:

	def process_request(self, request):
		u_agent = request.META.get('HTTP_USER_AGENT')
		part = re.search('\(+\w+', u_agent)
		platform = part.group(0)[1:].lower()
		response = None
		if request.user.is_authenticated and request.path_info == '/':
			if platform in settings.MOBILE_PLATFORM:
				response = HttpResponseRedirect('/mobile/', status= 302)
				return response
