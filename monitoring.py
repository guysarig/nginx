import requests
from requests.models import Response
from common import MyLogger

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

import datetime

class HealthTests:
    def __init__(self, logger: MyLogger):
        self.logger = logger
        self.date_format = "%Y-%m-%d %H:%M"


    def _connect_web_get(self, url: str) -> Response:
        '''
        inner connect_website method
        :param url: the website url
        :return: http response object
        '''
        return requests.get(url)

    def _create_browser(self, webdriver_path):
        #create a selenium object that mimics the browser
        browser_options = Options()
        #headless tag created an invisible browser
        browser_options.add_argument("--headless")
        browser_options.add_argument('--no-sandbox')
        browser = webdriver.Chrome(webdriver_path, options=browser_options)
        print("Done Creating Browser")
        return browser

    def _connect_browser_get(self, url: str) -> webdriver.Chrome:
        '''
        inner connect_website method
        :param url: the website url
        :return: http response object
        '''
        browser = self._create_browser("C:\\Users\\Guy\\AppData\\Local\\Google\\Chrome\\chromedriver.exe") #DON'T FORGET TO CHANGE THIS AS YOUR DIRECTORY
        browser.get(url)        
        return browser

    def web_connectivity(self, url: str) -> bool:
        '''
        check connectivity for a given url
        :param url: the website url
        :return: bool
        '''
        try:
            res = self._connect_web_get(url)
            if (res.status_code == 200):
                self.logger.info("the website at address {site_address} had passed the web connectivity check".format(site_address=url))
                browser = self._connect_browser_get(url)
                site_date_time = BeautifulSoup(browser.page_source).find("span", {"id": "date_time"}).next
                try:
                    datetime.datetime.strptime(site_date_time, self.date_format)
                    self.logger.info("the website returned a valid date_time: {msg}".format(msg=site_date_time))
                except Exception as e:
                    self.logger.error("the website at address {site_address} had returned an invalid date_time string: {msg}. exception message: {ex}.".format(site_address=url, msg=site_date_time, ex=e))
                return True
        except Exception as e:
            self.logger.error("the website at address {site_address} had failed {test_name} test, with the following exception message: {msg}.".format(site_address=url, test_name=self.web_connectivity.__name__, msg=e))
            

logger = MyLogger()
test_health = HealthTests(logger=logger)
test_health.web_connectivity(url="http://localhost")