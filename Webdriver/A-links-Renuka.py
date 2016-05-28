# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re

class ALinks(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://deanza.edu/"
        self.verificationErrors = []
    
    def test_p_links(self):
        link_title = {
            "Physics Department" : "De Anza College :: Physics :: Home",
            "Placement Tests" : "De Anza College :: Assessment Center :: Home",
             "Planetarium" : "De Anza Fujitsu Planetarium - Show Schedule - Astronomy and Laser Shows",
             "Policies" : "De Anza College :: Policies :: Home",
             "Political Science Department" : "De Anza College :: Political Science :: Home",
             "Prerequisite Clearance Request" : "De Anza College :: Assessment Center :: Prerequisites, Corequisites and Advisories :: Overview",
             "President's Office" : "De Anza College :: Office of the President :: Meet the President",
             "Placement Tests Results" : "MyPortal | Foothill-De Anza Community College District",
            }
        	
        driver = self.driver
        driver.get(self.base_url + "directory/dir-az.html")

        for link in link_title:
            title = link_title[link]
            driver.find_element_by_link_text(link).click()
            try: self.assertEqual(title, driver.title)
            except AssertionError as e: self.verificationErrors.append(str(e))
            driver.back()

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
