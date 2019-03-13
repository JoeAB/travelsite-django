from django.shortcuts import render
from destinationFinder.managers import RestCountriesManager, RestCurrencyManager
from django.http import HttpResponse
import requests
import json


# Create your views here.
def index(request):
	countryDictionary = dict()
	countyManager = RestCountriesManager()
	data = countyManager.getAll()
	for dataItem in data:
		countryDictionary[dataItem['alpha3Code']] = dataItem['name']
	countryTuple = list(countryDictionary.items())

	return render(request, 'destinationFinder/index.html',{'countryTuple': countryTuple})

def details(request, countryID):
	countyManager = RestCountriesManager()
	currencyManager = RestCurrencyManager()
	exchangeDict = dict()
	countryDetails = countyManager.getByCountryCode(countryID)
	exchangeRates = currencyManager.getExchangeRates()
	exchangeDict['USD'] = exchangeRates['rates']['USD']
	exchangeDict['EUR'] = exchangeRates['rates']['EUR']
	exchangeDict[countryDetails['currencies'][0]['code']] = exchangeRates['rates'][countryDetails['currencies'][0]['code']]
	return render(request, 'destinationFinder/details.html', {'countryDetails':countryDetails, 'exchangeDict': exchangeDict })
