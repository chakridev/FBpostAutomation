from selenium import webdriver
from secrete import email,pwd 
import time 

driver = webdriver.Chrome('chromedriver')

driver.get('https://www.facebook.com/')

usermail = driver.find_element_by_id('email')
usermail.send_keys(email)


userpwd = driver.find_element_by_id('pass')
userpwd.send_keys(pwd)

login = driver.find_element_by_id('u_0_b')
login.submit()


time.sleep(10)

body = driver.find_element_by_xpath('//*[@id="mount_0_0"]/div/div/div[1]/div[3]/div/div/div[1]/div[1]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div/div[1]/div[1]')
body.click()

time.sleep(10)

message = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[2]/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div/div/div/div')
message.send_keys('here we have enter our post link or img')

time.sleep(10)

post = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[1]/div[4]/div/div/div[1]/div/div[2]/div/div/div/form/div/div[1]/div/div[2]/div[3]/div[2]/div')
post.click()

