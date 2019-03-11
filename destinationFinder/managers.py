import requests

class RestCountriesManager:

	API_PATH = 'https://restcountries.eu/rest/v2'

	def query(self, requestString):
		response = requests.get(requestString)
		if response.status_code == 200:
			return response.json()
		else:
			return response.status_code

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

