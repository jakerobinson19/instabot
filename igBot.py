from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

class instagramBot():
  
  def __init__(self, email, password):
    self.browser = webdriver.Firefox()
    self.email = email
    self.password = password
    
  def signIn():
    self.browser.get('https://www.instagram.com/accounts/login/')
    self.emailInput = self.browser.find_elements_by_css_selector('form input')[0]
    self.passwordInput = self.browser.find_element_by_css_selector('form input')[1]
    
    #send email and password to fill input sections
    self.emailInput.send_keys(self.email)
    self.passwordInput.send_keys(self.password)
    
    #press Enter
    self.passwordInput.send_keys(Keys.Enter)
    
    #click the not now option for the notifications pop-up that appears immediately after logging in
    self.notnow = self.browser.find_element_by_css_selector('body > div:nth-child(13) > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
    self.notnow.click()
    
    
  def likePic():
  def commentOnPic():
  def 
