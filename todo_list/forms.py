from django import forms
from .models import Lists

class ListForm(forms.ModelForm):
	item = forms.CharField(required = False)
	class Meta:
		model = Lists
		fields = ["item", "completed"]