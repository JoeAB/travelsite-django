from django.conf import settings
from django.db import models


class Country(models.Model):
	name = models.TextField()
	country_code_alpha2 = models.CharField(max_length=3)
	country_code_alpha3 = models.CharField(max_length=3)

#split this out from country so we don't construct all this when showing our list page
class CountryDetails(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	currencies = models.ManyToManyField('Currency', blank=True)
	languages = models.ManyToManyField('Language', blank=True)
	region = models.TextField(max_length=150)
	subregion = models.TextField(max_length=150)
	#integer should be fine unless we have a massive populaton boom or alien settlers
	population = models.IntegerField()
	flag_url = models.TextField(null=True)

class Currency(models.Model):
	countries = models.ManyToManyField('CountryDetails', blank=True)
	name = models.TextField(max_length=150)
	code = models.CharField(max_length=3)
	symbol = models.CharField(max_length=250)

class Language(models.Model):
	countries = models.ManyToManyField('CountryDetails', blank=True)
	name = models.TextField(max_length=150)
	iso639_1 = models.CharField(max_length=2)
	iso639_2 = models.CharField(max_length=2)

class City(models.Model):
	country = models.ForeignKey(Country, on_delete=models.CASCADE)
	#Just in case there are long city names, like the full Thai name for Bangkok
	name = models.TextField()
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)
	population = models.IntegerField()
	utc_offset = models.DecimalField(max_digits=4, decimal_places=2)


class BlogPost(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	topic_country = models.ForeignKey(Country, on_delete=models.CASCADE)
	#topic city should be optional in the case of general country level postss
	topic_city = models.ForeignKey(City, on_delete=models.SET_NULL, blank=True, null=True)
	title = models.TextField(max_length=150)
	text = models.TextField()
	created_date = models.DateTimeField()

class BlogComment(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)
	text = models.TextField()


