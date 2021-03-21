import unittest
import requests
import json
import jsonpath
from selenium import webdriver
import operatornya

class PythonJsonData(unittest.TestCase):

	def setUp(self):
		print("setup")
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")

		#api url
		url = "https://jsonplaceholder.typicode.com/posts"

		#send get request
		response = requests.get(url)

		#parse response to json format
		self.json_response = json.loads(response.text)

	def test_userId(self):
		# length = len(json_response)
		# print(length)
		i = 0
		for x in self.json_response:
			print(self.json_response[i]['userId'])
			print(i)
			# assert operatornya.isInteger(json_response[i]['userId'])
			i+=1


		# mainPage = page.MainPage(self.driver)
		# assert mainPage.is_title_matches()
		# mainPage.search_text_element = "pycon"
		# mainPage.click_go_button()
		# search_result_page = page.SearchResultPage(self.driver)
		# assert search_result_page.is_results_found()

	def tearDown(self):
		self.driver.close()

if __name__ == "__main__":
	unittest.main()