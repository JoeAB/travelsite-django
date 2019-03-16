from django.test import TestCase
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User

from .models import Country, CountryDetails, Currency, Language, City, BlogPost, BlogComment
from .managers import RestCountriesManager, RestCurrencyManager

import json, datetime

#Model tests

class CountryModelTests(TestCase):
	def test_create_valid(self):
		try:
			country = newCountry()
			testCountry = Country.objects.get(name="My new empire")
		except Exception as e:
			self.fail(e)
	def test_remove_valid(self):
		try:
			country = newCountry()
			country.delete()
			testCountry = Country.objects.get(name="My new empire")
			self.fail("Country not deleted")
		except ObjectDoesNotExist:
			pass
		#any other error we should fail, since something is wrong
		except Exception as e:
			self.fail(e)

class CountryDetailsTests(TestCase):
	def test_create_valid(self):
		try:
			country = newCountry()
			countryDetails = newCountryDetails(country)
			testCountry = CountryDetails.objects.get(country__name="My new empire")
		except Exception as e:
			self.fail(e)

#class CurrencyTests(TestCase):

#class LanguageTests(TestCase):

#class CityTests(TestCase):

class BlogPostTests(TestCase):
	def test_create_valid(self):
		try:
			user = newTestUser()
			country = newCountry()
			post = newBlogPost(user, country)
			testPost = BlogPost.objects.get(title="yaba da ba ding dong")
		except Exception as e:
			self.fail(e)

#class BlogCommentTests(TestCase):

#Manager class tests

class RestCountriesManagerTest(TestCase):
	def test_getAll(self):
		try:
			manager = RestCountriesManager()
			results = manager.getAll()
		except Exception as e:
			self.fail(e)

#class RestCurrencyManagerTest(TestCase):

#View tests


#Put common functionality many tests will use here
def newTestUser():
	return User.objects.create_user(username="CoolJ667", password="password12345")
def newCountry():
	return Country.objects.create(name="My new empire",country_code_alpha2='GE', country_code_alpha3='GDE')

def newCountryDetails(country):
	return CountryDetails.objects.create(country=country, region="Asia", subregion="East Asia", population=10000000)

def newBlogPost(user, country):
	return BlogPost.objects.create(author=user, topic_country=country, title="yaba da ba ding dong", text= "too cool for school", created_date= datetime.datetime.now())
