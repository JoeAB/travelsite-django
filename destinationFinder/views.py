from django.shortcuts import render
from .managers import RestCountriesManager, RestCurrencyManager
from .models import Country, CountryDetails, Currency, Language, City
from django.http import HttpResponse
import requests
import json


# Create your views here.
def index(request):
	countries = Country.objects.all()

	return render(request, 'destinationFinder/index.html',{'countries': countries})

def details(request, countryID):
	country = Country.objects.get(id=countryID)
	countryDetails = CountryDetails.objects.get(country__id=countryID)
	currencyDict = {}
	languageDict = {}
	currencyManager = RestCurrencyManager()
	for currencyValue in countryDetails.currencies.all():
		currencyDict[currencyValue.name] = currencyManager.getExchangeRates(currencyValue.code)
	for languageValue in countryDetails.languages.all():
		languageDict[languageValue.name] = languageValue.iso639_2

	return render(request, 'destinationFinder/details.html', {'country':country, 'countryDetails':countryDetails, 'currencyDict': currencyDict, 'languageDict' :languageDict })
