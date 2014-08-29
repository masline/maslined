from django import forms
from django.core.validators import RegexValidator


class ContactForm(forms.Form):
	name = forms.CharField(max_length=100)
	company = forms.CharField(max_length=100)
	email = forms.EmailField()
	phone = forms.CharField(required=False,
							   max_length=14,
							   validators=[RegexValidator(regex='^\(?\d{3}\)?(-| |.)?\d{3}(-| |.)?\d{4}$', message='(###) ###-####', code='Invalid number')])
	msg = forms.CharField(widget=forms.Textarea, label="Reason for contacting, include part numbers if applicable")