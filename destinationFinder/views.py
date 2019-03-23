from django.shortcuts import render
from .managers import RestCountriesManager, RestCurrencyManager
from .models import Country, CountryDetails, Currency, Language, City, BlogPost
from django.http import HttpResponse
from django.utils import timezone
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
	blogPostList = BlogPost.objects.filter(topic_country__id=countryID).order_by('-created_date')[:3]

	return render(request, 'destinationFinder/details.html', {'country':country, 'countryDetails':countryDetails, 'currencyDict': currencyDict, 'languageDict' :languageDict, 'recentPosts': blogPostList})

def viewPost(request, postID):
	post = BlogPost.objects.get(id=postID)
	return render(request,'destinationFinder/viewPost.html',{'post':post})
#def writePost(request, countryID, cityID=None):
	

#def createPost(request, countryID, cityID=None):
