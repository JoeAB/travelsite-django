from django.contrib import admin
from .models import Country, CountryDetails, Currency, Language


admin.site.register(Country)
admin.site.register(CountryDetails)
admin.site.register(Currency)
admin.site.register(Language)
