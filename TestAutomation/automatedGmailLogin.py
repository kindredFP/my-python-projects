from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
import os

# need to make sure to have access to the chrome driver
chromeDriverLocation = '..//resourceFiles/chromedriver'

chromeDriver = webdriver.Chrome(chromeDriverLocation)
chromeDriver.get("http://gmail.com")

#Firefox Browser
#browser = webdriver.Firefox()
#browser.get('http://msn.com')

assert 'Gmail' in chromeDriver.title

# credentials
user = 'jsmith@gmail.com'
pwd = 'password'

try:
    elem = chromeDriver.find_element_by_id('identifierId')
except:
    print("cannot find by id ")

# try:
#     elem = chromeDriver.find_element_by_name('identifier')
# except:
#     print("cannot find by element by name")

elem.send_keys(user)
elem.send_keys(Keys.RETURN)

chromeDriver.implicitly_wait(2000)
elemPass = chromeDriver.find_element_by_name("password")
#elemPass = chromeDriver.find_element_by_xpath("//*[@name='password']")

elemPass.send_keys(pwd)
elemPass.send_keys(Keys.RETURN)

print("Value of current url " + chromeDriver.current_url)

#get current window handle
#myWindowHandle = chromeDriver.current_window_handle
#myWindowHandle.title()
#print("Window Handle title " + myWindowHandle.title())

chromeDriver.close()

#for firefox browser
#browser.close()
