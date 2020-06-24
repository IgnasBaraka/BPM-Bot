from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located


with webdriver.Chrome() as driver:
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.marktplaats.nl/a/auto-s/audi/m1557624092-audi-a6-2-0-tdi-a-business-edition-3-x-s-line-verkocht.html?c=df2f21f683612b45d62c413c0ca719df&previousPage=lr")
    Kenteken = driver.find_elements_by_xpath('//*[@id="car-attributes"]/div[1]/div[5]/span[2]')
    print(Kenteken)