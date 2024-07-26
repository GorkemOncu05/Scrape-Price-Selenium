from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://www.amazon.com.tr/")
WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")))
time.sleep(4)
input_element_by_name = driver.find_element(By.XPATH, "/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div[1]/input")
input_element_by_name.send_keys("samsung")
WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[4]/div/span/input")))
search_button = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[4]/div/span/input")
WebDriverWait(driver,4).until(expected_conditions.element_to_be_clickable((By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[4]/div/span/input")))
search_button.click()
WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "a-price-whole")))
price_list = driver.find_element(By.CLASS_NAME, "a-price-whole")
print([price_list.text for price_list in WebDriverWait(driver,20).until(EC.visibility_of_all_elements_located((By.CLASS_NAME, "a-price-whole")))])

while True:
    continue


