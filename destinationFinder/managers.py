import requests
import os
import json

class RestCountriesManager:

	API_PATH = 'https://restcountries.eu/rest/v2'

	def query(self, requestString):
		response = requests.get(requestString)
		if response.status_code == 200:
			return response.json()
		else:
			#if we fail for any reason, we want an exception
			raise Exception("Failure getting data from REST endpoint")

	def searchByName(self, nameQuery):
		searchQuery= self.API_PATH +'/name/'+nameQuery
		return self.query(searchQuery)

	def getByCountryCode(self, code):
		searchQuery= self.API_PATH +'/alpha/'+ code
		return self.query(searchQuery)

	def getCountriesByRegion(self, region):
		searchQuery= self.API_PATH +'/region/'+ region
		return self.query(searchQuery)

	def getAll(self):
		searchQuery = self.API_PATH + '/all'
		return self.query(searchQuery) 

class RestCurrencyManager:

	API_PATH = 'http://data.fixer.io/api/'

	def __init__(self):
		dirName = os.path.dirname(__file__)
		filename = os.path.join(dirName, 'config.js')
		with open(filename) as data_file:
			self.key = json.load(data_file)['key']


	def getExchangeRates(self, code):
		path = self.API_PATH + 'latest?access_key='+self.key
		response = requests.get(path)
		if response.status_code != 200:
			return {"Error" : "Currency data not currently available."}
		data = response.json()
		exchangeDict = dict()
		exchangeDict['USD'] = data['rates']['USD']
		exchangeDict['EUR'] = data['rates']['EUR']
		exchangeDict[code] = data['rates'][code]
		return exchangeDict




