from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 

class SignUpForm(UserCreationForm):
	first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
	email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
	def clean_email(self):
		data = self.cleaned_data['email']
		if ".nhs." not in data:
			raise forms.ValidationError("Must be an NHS accredited address")
		return data

	class Meta:
		model = User
		fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
