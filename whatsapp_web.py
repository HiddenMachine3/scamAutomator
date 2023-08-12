from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import random
import pyperclip

## Selenium web drivers
driver = None

def wait(web_opening_time=3):
	time.sleep(web_opening_time)

## load web driver for selenium : chrome
def web_driver_load():
	global driver
	driver = webdriver.Edge()
## quit web driver for selenium
def web_driver_quit():
	driver.quit()
	quit()

## actual login in hockey app site
def whatsapp_login():
	driver.get('https://web.whatsapp.com/');

	print("Login and click on necessary group chat")

	WebDriverWait(driver, 1000).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/header/div[2]/div[1]/div/span'))
    )



def rename_group(grp_name):
	time.sleep(2)
	print ('Attempting to rename group. Keep necessary group chat open already')

	print("opening group chat")
	grp_header = driver.find_element(By.XPATH,'//*[@id="main"]/header/div[2]/div[1]/div/span')
	grp_header.click()
	time.sleep(2)

	print("editing group name")
	# click on edit icon
	try:
		WebDriverWait(driver, 5).until(
			EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[1]/div/div[2]/div/div/span[2]/button'))
		)
	except Exception:
		print("Could not find by edit group name button...")
		exit(0)
	edit = driver.find_element(By.XPATH ,'//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[1]/div/div[2]/div/div/span[2]/button')
	edit.click()
	time.sleep(2)

	# # click on edit input
	edit_input_xpath = '//*[@id="app"]/div/div/div[6]/span/div/span/div/div/div/section/div[1]/div/div[2]/div/div[1]/div[3]/div/div/p'
	try:
		WebDriverWait(driver, 2).until(
			EC.presence_of_element_located((By.XPATH, edit_input_xpath))
		)
	except Exception:
		print("Could not find by xpath, trying to find by active element")
	inp = driver.switch_to.active_element
	inp.click()
	inp.send_keys(Keys.CONTROL + "a")
	inp.send_keys(Keys.BACK_SPACE)

	#type new group name:
	inp.send_keys(grp_name)
	time.sleep(0.5)
	inp.send_keys(Keys.RETURN)

def send_msg(msg):
	print(msg)
	# click on message box
	inp = driver.find_element(By.XPATH,'//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]/p')
	inp.click()

	#type message:
	#type new group name:
	pyperclip.copy(msg) # copying the grp na
	inp.send_keys(Keys.CONTROL + "v")
	time.sleep(0.5)
	inp.send_keys(Keys.RETURN)
	time.sleep(0.5)

def event_loop():
	while True:
		rename_group(f"group {random.randint(1,100)}")
		send_msg("hello")
		time.sleep(10)


### Main Method
if __name__ == "__main__":
	web_driver_load()

	whatsapp_login()
	event_loop()

	web_driver_quit()
