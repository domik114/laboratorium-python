from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from os import system

PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://bg.po.edu.pl/index.php")
search = driver.find_element(By.NAME, "ss_phrase")
search.send_keys("Python")
search.send_keys(Keys.RETURN)

try:
    time.sleep(5)
    #body = driver.find_element(By.TAG_NAME, "body")
    #container = WebDriverWait(body, 10).until(EC.presence_of_all_elements_located((By.TAG_NAME, "div")))
    #print("desc-o-mb-title" in driver.page_source)
    #container = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]")))
    #print(container.text)
    #div1 = WebDriverWait(body, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]")))
    #div2 = div1.find_element(By.XPATH, "//*[@id='results-panel']")
    #span = driver.find_element(By.CSS_SELECTOR, "#results-panel > div.found-records > div:nth-child(1) > div.record-description > div.record-meta > div.desc-opis > a > span")
    span = driver.find_element_by_xpath("//*[@id=\"results-panel\"]/div[2]/div[1]/div[2]/div[2]/div[1]/a/span/span[2]").text
    print(span)

    #print(span.text)
except:
    print("Błąd.")
finally:
    driver.quit()