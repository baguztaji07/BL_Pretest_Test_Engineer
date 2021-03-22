class BasePage(object):
	"""docstring for BasePage"""
	def __init__(self, driver):
		self.driver = driver
		
class SearchResultPage(BasePage):
	def is_results_found(self):
		return "Hasil pencarian" in self.driver.page_source