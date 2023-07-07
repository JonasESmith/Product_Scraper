import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class GoogleTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_title(self):
        self.browser.get("http://www.google.com")
        self.assertIn("Google", self.browser.title)

        # Find the search box using its name attribute value
        search_box = self.browser.find_element(By.NAME, "q")

        # Clear the search box in case there's any pre-filled text
        search_box.clear()

        # Type the search query into the search box
        search_box.send_keys("eqalink.com")

        # Submit the search form
        search_box.submit()

        # Wait for the search results page to load
        wait = WebDriverWait(self.browser, 10)
        wait.until(EC.title_contains("eqalink.com - Google Search"))

        # Assert that the search results page has loaded by checking the page title
        self.assertIn("eqalink.com - Google Search", self.browser.title)

        # Save the page HTML to a file
        with open("selenium_test_output.html", "w", encoding="utf-8") as file:
            file.write(self.browser.page_source)


if __name__ == "__main__":
    unittest.main(verbosity=2)
