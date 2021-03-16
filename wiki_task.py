import time
from selenium import webdriver
from random import shuffle


class Wiki:
    wiki_main_url = 'https://en.wikipedia.org/wiki/Main_Page'
    listOfLinks = []
    title = ''
    noneType = type(None)

    def __init__(self, path_to_drive, search_page):
        self.search_page = search_page
        self.driver = webdriver.Chrome(executable_path=path_to_drive)
        self.driver.maximize_window()
        self.driver.get(self.wiki_main_url)

    def get_elements(self):
        if not self.title:
            elements = self.driver.find_elements_by_css_selector("div.mp-bordered+div a")
            shuffle(elements)
            return elements
        else:
            return self.driver.find_elements_by_css_selector("div.mw-body-content p a")

    def get_data(self, elements, i):
        if type(elements[i].get_attribute("href")) is self.noneType or elements[i] \
                .get_attribute("href").find('#') > -1 or elements[i].get_attribute("href").find('/wiki/') == -1 \
                or self.listOfLinks.count(elements[i].get_attribute("href").lower()) > 0 \
                or elements[i].get_attribute("href").find('https://en.wikipedia.org/') == -1 \
                or elements[i].get_attribute("href").find('disambiguation') > -1 \
                or elements[i].get_attribute("href").find(':', 7) > -1 or not elements[i].is_displayed():
            return 1
        else:
            self.listOfLinks.append(elements[i].get_attribute("href").lower())
            elements[i].click()
            self.title = self.driver.find_elements_by_css_selector("h1.firstHeading")[0] \
                .get_attribute('innerHTML')
            time.sleep(1)
            return 0

    def find_page(self):
        while self.title != self.search_page:
            elements = self.get_elements()

            for i in range(0, len(elements)):
                if not self.get_data(elements, i):
                    break

        self.printing_result()

    def printing_result(self):
        print(len(self.listOfLinks))
        self.driver.quit()


wiki = Wiki('/Users/Vito/Desktop/Selenium/Wiki_task/chromedriver', 'Philosophy')
wiki.find_page()
