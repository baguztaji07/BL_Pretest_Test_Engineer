import unittest
import page
from selenium import webdriver

class SearchProduct(unittest.TestCase):

	def setUp(self):
		# print("setup")
		self.driver = webdriver.Chrome("C:\Program Files (x86)\chromedriver.exe")
		self.driver.get("https://bukalapak.com")

	def test_search_a_product(self):
		self.driver.find_element_by_id("v-omnisearch__input").send_keys("Iphone")
		self.driver.find_element_by_class_name("v-omnisearch__submit").click()
		search_result_page = page.SearchResultPage(self.driver)
		assert search_result_page.is_results_found()

	def tearDown(self):
		self.driver.quit()

if __name__ == "__main__":
	unittest.main()