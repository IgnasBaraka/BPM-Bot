from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.marktplaats.nl/l/auto-s/f/diesel+sedan/474+483/#PriceCentsTo:500000|constructionYearFrom:2007|mileageFrom:200000")
elem = driver.find_element_by_xpath('//*[@id="content"]/div[2]/ul/li[2]/a')
elem.click()
element = driver.find_element_by_xpath('//*[@id="car-attributes"]/div[1]/div[7]/span[2]')

actions = ActionChains(driver)

actions.move_to_element(element).perform()

kenteken = driver.find_element_by_xpath('//*[@id="car-attributes"]/div[1]/div[5]/span[2]')
print (kenteken.text)
text = kenteken.text




driver.get('https://www.finnik.nl/?referrer')

element = driver.find_element_by_xpath('/html/body/div[2]/form/button')
element.click()
search = driver.find_element_by_xpath('/html/body/section[1]/div/div[1]/article[2]/div/form/div/input')
search.click()

search.send_keys(text)
