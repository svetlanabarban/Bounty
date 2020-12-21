from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Firefox()
# Verify signing up as a Bounty Hunter user
driver.get("http://jobmight.com/session/partner/signup")
first_name = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "firstName"))))
first_name.send_keys("Svetlana")
last_name = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "lastName"))))
last_name.send_keys("Barban")
email = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "email"))))
email.send_keys("qwedfg@gmail.com")
password = WebDriverWait(driver, 20).until((EC.visibility_of_element_located((By.NAME, "password"))))
password.send_keys("123Qwe-dfg)")
next_button = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Next')]"))))
next_button.click()

recruiting_experience = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.NAME, "recruitingExperience"))))
recruiting_experience.click()
recruiting_experience_option = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//option[contains(@value,'0')]"))))
recruiting_experience_option.click()
check_box = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[@class='MuiIconButton-label']"))))
check_box.click()
close = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Close')]"))))
close.click()
sign_up = WebDriverWait(driver, 20).until((EC.element_to_be_clickable((By.XPATH, "//span[contains(text(),'Sign up')]"))))
sign_up.click()