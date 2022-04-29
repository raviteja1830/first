import django_filters
from .models import Listings

class ListingFilter(django_filters.FilterSet):
	class Meta:
		model = Listings
		fields = ['title','condition']

