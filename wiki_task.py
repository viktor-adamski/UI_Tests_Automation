import time
from selenium import webdriver
from random import shuffle

# listOfLinks - there I'm collecting links, which the program clicked
# title - there I'm saving title of visited page, that I can to define, that the program is appeared on necessary page
# noneType - is used for detecting that the links is clickable

listOfLinks, title, noneType = [], '', type(None)

# Activating WebDriver

driver = webdriver.Chrome(executable_path='C:/Users/kremen/OneDrive/Рабочий стол/chromedriver')
driver.maximize_window()
driver.get('https://en.wikipedia.org/wiki/Main_Page')

# loop for finding necessary the page, which will working while not finding necessary the page

while title != 'Philosophy':
    # if title = '', that means that the program is on home page of wiki and we need to find all link of articles
    # in another case the program will take all links from article

    if not title:
        elements = driver.find_elements_by_css_selector("div.mp-bordered+div a")

        # using 'shuffle' to get random article

        shuffle(elements)
    else:
        elements = driver.find_elements_by_css_selector("div.mw-body-content p a")

    # loop where the program is checking that links is normal links without links on files, images, is clickable and etc
    # and if link is as we need, then program clicks on it and save this link to variable ''listOfLinks''
    # and save the title of article to variable 'title'
    # in another case, the program skip this link

    for i in range(0, len(elements)):
        if type(elements[i].get_attribute("href")) is noneType or elements[i].get_attribute("href").find('#') > -1 \
                or elements[i].get_attribute("href").find('/wiki/') == -1 \
                or listOfLinks.count(elements[i].get_attribute("href").lower()) > 0 \
                or elements[i].get_attribute("href").find('https://en.wikipedia.org/') == -1 \
                or elements[i].get_attribute("href").find('disambiguation') > -1 \
                or elements[i].get_attribute("href").find(':', 7) > -1 or not elements[i].is_displayed():
            continue
        else:
            listOfLinks.append(elements[i].get_attribute("href").lower())
            elements[i].click()
            title = driver.find_elements_by_css_selector("h1.firstHeading")[0].get_attribute('innerHTML')
            time.sleep(1)
            break

# printing into output amount of visiting pages and close browser

print(len(listOfLinks))
driver.quit()