import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://qiita.com/")

title = driver.title

driver.implicitly_wait(0.5)

text_box = driver.find_element(by=By.CLASS_NAME, value="style-7sxcw7")
# submit_button = driver.find_element(by=By.NAME, value="mFreeword")

text_box.send_keys("Java")
text_box.send_keys(Keys.ENTER)
# submit_button.click()

message = driver.find_element(by=By.ID, value="message")
text = message.text

time.sleep(50)

# driver.quit()