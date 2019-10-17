from django import forms
from .models import *

class AddImageForm(forms.ModelForm):

	class Meta:
		model = ImageUpload
		fields = ['name', 'add_image']
