from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("http://jobmight.com/session/partner/signup")
first_name = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "firstName"))))
first_name.send_keys("Svetlana")
last_name = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "lastName"))))
last_name.send_keys("Barban")
email = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email.send_keys("abc@yahoo.com")
password = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("Ss-2101989")
next = WebDriverWait(driver, 20).until((EC.presence_of_element_located((By.NAME, "Next"))))
next.click()
check_button = WebDriverWait(driver, 20).until((EC.presence_of_element_located((By.NAME, "experience"))))
check_button.click()
check_button = WebDriverWait(driver, 20).until((EC.presence_of_element_located((By.NAME, "0"))))
check_button.click()
check_button = WebDriverWait(driver, 20).until((EC.presence_of_element_located((By.NAME, "agreement"))))
check_button.click()
close_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Close')]"))))
close_button.click()
sign_up = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//*[contains(text(),'Sign up')]"))))
sign_up.click()