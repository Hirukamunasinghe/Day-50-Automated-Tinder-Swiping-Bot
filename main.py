#NOTE: Below written is a python code which automates tinder. However, since I haven't yet met the regulations to login
#to Tinder(such as age restrictions), it might not respond effectively.
#Therefore, the main purpose of this project is to apply the selenium webdriver theory.

#importing modules and installation of selenium webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
import time


EMAIL ="timgeorge1234555@gmail.com"
PASSWORD ="tim123@12"

driver_service = Service(executable_path="C:\Development\chromedriver.exe")
driver = webdriver.Chrome(service=driver_service)

URL ="https://tinder.com/"
driver.get(URL)

time.sleep(2)
#Create account button
account_button = driver.find_element(By.XPATH,'//*[@id="c-1804602209"]/div/div[1]/div/main/div[1]/div/div/div/div/div[3]/div/div[2]/button')
account_button.click()

time.sleep(3)
#Login with Facebook
facebook_login_button = driver.find_element(By.XPATH,'//*[@id="c761984011"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login_button.click()

#Switch to Facebook login window
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

#Fb login
#Email
email = driver.find_element(By.NAME,"email")
email.send_keys(EMAIL)
time.sleep(1)

#Password
password = driver.find_element(By.NAME,"pass")
password.send_keys(PASSWORD)
time.sleep(1)
password.send_keys(Keys.ENTER)

#Switch to Tinder login window
driver.switch_to.window(base_window)
print(driver.title)

#Allow location
allow_location_button = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()

#Disallow notifications
notifications_button = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()

#Allow cookies
cookies = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

#Tinder free tier only allows 100 "Likes" per day. If you have a premium account, feel free to change to a while loop.
for n in range(100):

    #Add a 1 second delay between likes.
    time.sleep(1)

    try:
        print("called")
        like_button = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    #Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR,".itsAMatch a")
            match_popup.click()

        #Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            time.sleep(2)

driver.quit()