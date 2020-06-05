from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class ExternalVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_view_CV(self):
        # Employer visits home page
        self.browser.get('http://localhost:8000/')

        # Employer notices the menu bar has a CV link
        link = self.browser.find_element_by_link_text('CV')
        self.assertIsNotNone(link)

        # Employer follows link to CV
        link.click()
        
        time.sleep(1) 
        # Employer views a page containing Katie Midgley's CV. This includes:
            # Personal details
            # Education
            # Work Experience
            # Other Skills

        headings = self.browser.find_elements_by_tag_name('h1')
        texts = []
        for heading in headings:
            texts.append(heading.text)

        self.assertIn("Education", texts)
        self.assertIn("Work Experience", texts)
        self.assertIn("Other Skills", texts)

        # Employer does not see any edit of remove buttons
        buttons = self.browser.find_elements_by_class_name('btn')
        self.assertFalse(buttons)

        # Employer has seen all they want 
        self.browser.quit()

if __name__ == '__main__':  
    unittest.main()  