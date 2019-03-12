from django.shortcuts import render
from destinationFinder.managers import RestCountriesManager
from django.http import HttpResponse
import requests


# Create your views here.
def index(request):
	countryDictionary = dict()
	countyManager = RestCountriesManager()
	data = countyManager.getAll()
	for dataItem in data:
		countryDictionary[dataItem['alpha3Code']] = dataItem['name']
	countryTuple = list(countryDictionary.items())

	return render(request, 'destinationFinder/index.html',{'countryTuple': countryTuple})


