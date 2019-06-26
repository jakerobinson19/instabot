from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time

class instagramBot():
  
  def __init__(self, email, password):
    self.browser = webdriver.Chrome()
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
    time.sleep(3)
    
    #click the not now option for the notifications pop-up that appears immediately after logging in
    self.notnow = browser.find_element_by_xpath('//button[text()="Not Now"]')
    self.notnow.click()
    
    #pic1: //*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[1]/div[2]/section[1]/span[1]/button/span
    #pic2: //*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[2]/div[2]/section[1]/span[1]/button/span
    #pic3: //*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[3]/div[2]/section[1]/span[1]/button/span
  
  
  def likePic(self, limit):
    for i in range(limit):
      self.likeButton = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[' + i ']/div[2]/section[1]/span[1]/button/span')
      self.likeButton.click()
  
  def commentOnPic(self):
