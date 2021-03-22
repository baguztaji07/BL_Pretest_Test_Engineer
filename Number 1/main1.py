import unittest
import requests
import json
from selenium import webdriver
import operatornya

class PythonJsonData(unittest.TestCase):

	def setUp(self):
		# print("setup")
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

		#api url
		url = "https://jsonplaceholder.typicode.com/posts"

		#send get request
		response = requests.get(url)

		#parse response to json format
		self.json_response = json.loads(response.text)

	def test_userId(self):
		i = 0
		for x in self.json_response:
			assert operatornya.isInteger(self.json_response[i]['userId'])
			i+=1

	def test_id(self):
		i = 0
		for x in self.json_response:
			assert operatornya.isInteger(self.json_response[i]['id'])
			i+=1

	def test_title(self):
		i = 0
		for x in self.json_response:
			assert operatornya.isString(self.json_response[i]['title'])
			i+=1

	def test_body(self):
		i = 0
		for x in self.json_response:
			assert operatornya.isString(self.json_response[i]['body'])
			i+=1

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()