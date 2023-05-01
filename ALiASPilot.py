#! //home/aakarsh-gram/Softwares/ALiASPilot/env/bin/python

import openpyxl 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

excel = ''
sheetname = ''
# webdriver_path = '/usr/local/bin/geckodriver'
whatsapp_web_url = 'https://web.whatsapp.com'
whatsapp_grp = 'ALiAS Volunteers'

driver = webdriver.Firefox()
driver.get(whatsapp_web_url)
try:
    # element = WebDriverWait(driver, 120).until(
    #     EC.presence_of_element_located((By.CLASS_NAME, 'selectable-text copyable-text iq0m558w'))
    # )
    driver.find_element_by(((By.CLASS_NAME, 'selectable-text copyable-text iq0m558w')))
finally:
    driver.quit()

# driver.find_element(element).send_keys(whatsapp_grp + Keys.ENTER)
# element.send_keys(whatsapp_grp + Keys.ENTER)
# driver.find_element((By.CLASS_NAME, 'selectable-text')).send_keys(whatsapp_grp + Keys.ENTER)
# driver.find_element((By.NAME, "q")).send_keys(whatsapp_grp + Keys.ENTER)
div = driver.find_element((By.CLASS_NAME, "to2l77zo"))