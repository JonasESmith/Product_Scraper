import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class TopShelfHempTestCase(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.addCleanup(self.browser.quit)

    def test_page_loading(self):
        self.browser.get(
            "https://www.topshelfhemp.co/map?fbclid=IwAR3D6NX3b4E_uhZ3hRvq526yRXvfJprI3cMyMPFl-1r758oDcddjw52a9HE_aem_AV03lU6wZWa1nJPb1WqcJN9Unq-Si5IOoKEKs7pFKIzXdhapQ39S9b7m4b3vQKjIQCk"
        )

        # Wait for the map's canvas element to load
        WebDriverWait(self.browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "maplibregl-canvas"))
        )

        # Retrieve all elements for stores
        store_elements = self.browser.find_elements(By.CLASS_NAME, "maplibregl-marker")

        print(f"Found {len(store_elements)} store elements")

        page_html = self.browser.page_source
        print("Obtained page HTML, attempting to write to file...")

        with open("selenium_test_output.html", "w", encoding="utf-8") as file:
            file.write(page_html)
            print("Page HTML written to selenium_test_output.html successfully.")


if __name__ == "__main__":
    unittest.main(verbosity=2)
