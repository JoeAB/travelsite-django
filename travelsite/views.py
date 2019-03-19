from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render
from destinationFinder.managers import RestCountriesManager, RestCurrencyManager
from destinationFinder.models import Country, CountryDetails, Currency, Language, City
from django.http import HttpResponse
import json


# Create your views here.
@login_required
def importRestData(request):
	restCountriesManager = RestCountriesManager()
	data = restCountriesManager.getAll()
	#return HttpResponse(data[0]['name'])
	for dataItem in data:
		try:
			testCountry = Country.objects.get(name= dataItem['name'])
		except ObjectDoesNotExist:
			#we need to add it
			newCountry =Country.objects.create(name= dataItem['name'],country_code_alpha2= dataItem['alpha2Code'], country_code_alpha3= dataItem['alpha3Code'])
			newCountryDetails = CountryDetails.objects.create(country=newCountry,region=dataItem['region'],subregion=dataItem['subregion'],population=dataItem['population'],flag_url=dataItem['flag'])
			#resultsList[dataItem['alpha3Code']] =dataItem['name']
			#try currency
			for currencyItem in dataItem['currencies']:	
				try:
					currency = Currency.objects.get(code=currencyItem['code'])
					newCountryDetails.currencies.add(currency)
					
				except ObjectDoesNotExist:
					currency = Currency.objects.create(name=currencyItem['name'],code=currencyItem['code'],symbol=currencyItem['symbol'])
					newCountryDetails.currencies.add(currency)
					
			#try language
			for languageItem in dataItem['languages']:	
				try:
					language = Language.objects.get(iso639_2=languageItem['iso639_2'])
					newCountryDetails.languages.add(language)
					
				except ObjectDoesNotExist:
					language = Language.objects.create(name=languageItem['name'],iso639_1=languageItem['iso639_1'],iso639_2=languageItem['iso639_2'])
					newCountryDetails.languages.add(language)
					
	return HttpResponse('Added the following countries  ')

