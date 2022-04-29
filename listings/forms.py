from django import forms
from .models import Listings

class ListingForm(forms.ModelForm):
	class Meta:
		model = Listings
		fields = '__all__'