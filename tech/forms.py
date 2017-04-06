from django.forms import ModelForm
from tech.models import TechSupport

class SupportForm(ModelForm):
	"""
	def __init__(self, user_email=''):
		self.user_email = user_email
	"""
	class Meta:
		model = TechSupport
		fields = ['feedback_mail', 'type_message', 'caption', 'text', 'files']
		
