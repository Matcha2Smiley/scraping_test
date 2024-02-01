import time
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://researchers.general.hokudai.ac.jp/search/index.html")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.NAME, value="search-keyword")
submit_button = driver.find_element(by=By.NAME, value="mFreeword")

text_box.send_keys("光合成")
submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

time.sleep(50)

driver.quit()