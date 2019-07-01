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
    self.likes = 0
    self.comments = 0
    self.profilesEngaged = []
    self.hashtagList = ['dachshund', 'dachshunds', 'dachshundsonly', 'dachshund_love',
                        'doxiesofig', 'doxiefever', 'dachshundgram', 'dachshundlife',
                        'dachshund_feature','dachshundnation','doxieofig','sausagedoges',
                        'cute', 'dachshundsarethebest','dachshundobsessed','doxies',
                        'dachshundoftheday','dachshundmoments','fluffy','dogs']
    
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
  
  def getXpathForHeart(self, number):
      return('//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[{}]/div[2]/section[1]/span[1]/button/span'.format(number))
  
  def getLikeButtons(self):
    self.hearts = self.browser.find_elements_by_xpath("//span[@class='fr66n']")
    return(self.hearts)
  
  def likePic(self, number = 1):
    self.loop = 0

    while self.loop <= number:
      self.hearts = self.getLikeButtons()

      for h in range(len(self.hearts)):
        print('liking the pic {}'.format(str(self.loop + 1)))
        self.delay()
        
        self.actions = ActionChains(self.browser)
        self.actions.move_to_element(self.hearts[h])
        self.actions.click(self.hearts[h])
        self.actions.perform()
        
        self.loop = self.loop + 1
        if self.loop > number:
          break
  
  def goToProfile(self, uname = self.email):
    if uname == None:
      uname = self.email
    self.browser.get('https://www.instagram.com/{}'.format(uname))
  
  def getUsername(self):
    uname = self.browser.find_elements_by_xpath("//a[@class='FPmhX notranslate nJAzx']")
    return(uname)
  
  def goToHashtag(self, hashtag):
    self.browser.get('https://www.instagram.com/explore/tags/{}/'.format(hashtag))
  
  def goToNextPic(self, iter):
    time.sleep(random.randint(1,3))
    if iter == 0:
      self.nextButton = self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a')
    else:
      self.nextButton = self.browser.find_element_by_xpath('/html/body/div[3]/div[1]/div/div/a[2]')
    #self.browser.find_elements_by_xpath("//*[contains(text(), 'Next')]")
    self.nextButton.click()
    
  #function that delays for random number of seconds and prints how long program is pausing
  def delay(self):
    sec = round(random.uniform(2,5), 3)
    sys.stdout.write("Pausing for " + str(sec) + " seconds")
    self.t = 0
    while self.t < sec:
      sys.stdout.write('.')
      sys.stdout.flush()
      time.sleep(sec/3)
      self.t = self.t + sec/3
    sys.stdout.write('\n')
    
  
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
    
