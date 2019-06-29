from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import random
import time

class instagramBot():
  
  def __init__(self, email, password):
    self.browser = webdriver.Chrome()
    self.email = email
    self.password = password
    
  def signIn(self):
    self.browser.get('https://www.instagram.com/accounts/login/')
    self.emailInput = self.browser.find_elements_by_css_selector('form input')[0]
    self.passwordInput = self.browser.find_elements_by_css_selector('form input')[1]
    
    #send email and password to fill input sections
    self.emailInput.send_keys(self.email)
    self.passwordInput.send_keys(self.password)
    
    #press Enter
    self.passwordInput.send_keys(Keys.Enter)
    time.sleep(3)
    
    #click the not now option for the notifications pop-up that appears immediately after logging in
    self.notnow = self.browser.find_element_by_xpath('//button[text()="Not Now"]')
    self.notnow.click()
    
    #pic1: //*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[1]/div[2]/section[1]/span[1]/button/span
    #pic2: //*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[2]/div[2]/section[1]/span[1]/button/span
    #pic3: //*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[3]/div[2]/section[1]/span[1]/button/span
  
  
  def getXpathForHeart(self, number):
      return('//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[{}]/div[2]/section[1]/span[1]/button/span'.format(number))
      
  def likePic(self, number):
    while self.loop < number:
      self.hearts = self.browser.find_elements_by_xpath("//span[@class='fr66n']")

      for h in range(len(self.hearts)):
        print('liking the pic...')
        time.sleep(random.randint(2,5))
        ActionChains(self.browser).move_to_element(self.hearts[h]).click(self.hearts[h]).perform()
        self.loop = self.loop + 1
        
  def commentOnPic(self):
    
    
    #commentbutton2: 
    #commentbutton3: //*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[3]/div[2]/section[1]/span[2]/button/span
    
    #'Add a comment' - prompt = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div/form/textarea')
    
    #'Post comment' - postComment = browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/article/div[2]/section[3]/div[1]/form/button')
    # postComment.click()
    
  def goToProfile(self):
    self.profile = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
    self.profile.click()
    
  def selectImage(self, picType):
    if self.picType == 'Latest'
    elif self.picType == 'Second'
    elif self.picType == 'Random'
      #set element, select picture
    
