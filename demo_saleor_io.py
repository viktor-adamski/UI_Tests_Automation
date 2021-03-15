from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path='/Users/Vito/Desktop/Selenium/demo_saleor_io/chromedriver')
driver.maximize_window()
driver.get('https://demo.saleor.io/')
time.sleep(3)


def clicking(classes_name, time_to_sleep):
    for i in classes_name:
        driver.find_element_by_class_name(i).click()
        time.sleep(time_to_sleep)


def sign_in(field, key):
    for i in range(len(field)):
        element = driver.find_element_by_name(field[i])
        element.clear()
        element.send_keys(key[i])


def main():
    clicking(["main-menu__icon", "active-tab"], 3)

    sign_in(["email", "password"], ["admin@example.com", "admin"])

    clicking(["login-form__button", "main-menu__nav-dropdown"], 5)

    driver.find_element_by_partial_link_text("PARROT").click()
    time.sleep(5)

    clicking(["sc-kjoXOD.imDaoE", "sc-eXNvrr.cDrDlU"], 5)

    driver.find_element_by_name("quantity").send_keys("5")
    time.sleep(5)

    clicking(["sc-iwsKbI.fKClap", "button.secondary"], 5)


main()
driver.quit()