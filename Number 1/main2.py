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
		self.url = "https://jsonplaceholder.typicode.com/posts"

	def test_postReq(self):
		#read input json file
		file = open('D:\\Kerjooo\\QA Bukalapak\\PreTest\\BL_Pretest_Test_Engineer\\Number 1\\data.json','r')
		json_input = file.read()
		request_json = json.loads(json_input)

		#make json post request
		response = requests.post(self.url,request_json)

		#validating response code
		assert response.status_code == 201

		#close file
		file.close()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()