import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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

text_box.send_keys("Java")
text_box.send_keys(Keys.ENTER)


# CSVへの書き込み

with open('scraped_data.csv', mode='w', newline='', encoding='utf-16') as file:
    writer = csv.writer(file)
    writer.writerow(['ID', '名前', 'タイトル'])  

    try:
        element_present = EC.presence_of_element_located((By.CSS_SELECTOR, 'article'))
        WebDriverWait(driver, 10).until(element_present)
        
        while True:
            # ここでデータを抽出する
            userId = driver.find_element(By.CSS_SELECTOR, '.style-r5dy7w').text
            name = driver.find_element(By.CSS_SELECTOR, '.style-15fzge').text
            # title = driver.find_element(By.CSS_SELECTOR, 'h2.style-be78dg > a').text
            
            # CSVにデータを書き込む
            writer.writerow([userId, name, title])

            # 次のページへのリンクをクリック
            next_button = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Next Page"]')
            if next_button:
                next_button.click()
                WebDriverWait(driver, 10).until(EC.staleness_of(next_button))
            else:
                break

    except TimeoutException:
        print("タイムアウトしました")

    finally:
        driver.quit()