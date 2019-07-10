#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

import emoji
import random
import time
import sys

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
  
  def getFollowerCount(self):
    return(int(self.browser.find_element_by_partial_link_text("followers").find_element_by_xpath('span').get_attribute('title').replace(',','')))

  def getFollowingCount(self):
    return(self.browser.find_element_by_partial_link_text("following").find_element_by_xpath('span').text)
    
  def getXpathForHeart(self, number):
      return('//*[@id="react-root"]/section/main/section/div[2]/div[1]/div/article[{}]/div[2]/section[1]/span[1]/button/span'.format(number))
  
  def getLikeButtons(self):
    self.hearts = self.browser.find_elements_by_xpath("//span[@class='fr66n']")
    return(self.hearts)
  
  def getLikeButton(self):
    wait = WebDriverWait(self.browser, 10)
    like_button = wait.until(EC.visibility_of_element_located((By.XPATH, "//span[@class='fr66n']")))
    return(like_button)
  
  def notAlreadyLiked(self,element):
    self.not_liked = True
    #try to find the glyphSpriteHeart outline. 
    #If it doesnt exist, then the element must have changed to 'glyphSpriteHeart__filled' because it has already been liked
    
    try:
      heart_button = element.find_element_by_xpath("//button/span[@class='glyphsSpriteHeart__outline__24__grey_9 u-__7']")
    except NoSuchElementException:
      print('Picture already liked, moving on...')
      self.not_liked = False
      
    return(self.not_liked)
  
  def checkIfFollowing(self):
    status = self.browser.find_element_by_xpath("//*/button[contains(text(), 'Follow')]").text
    if status == 'Following':
      print('We are already following this user')
    else:
      print('We do not follow this user')

  def likePic(self):
    heart = self.getLikeButton()
    self.delay()
    try:
      if self.notAlreadyLiked(heart):
        heart.click()
      
  def likePic(self, number = 1):
    if checkIfPicAlreadyLiked():
      print("Pic already liked")
    self.loop = 1

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
  
  def goToProfile(self, uname = None):
    if uname == None:
      uname = self.email
    self.browser.get('https://www.instagram.com/{}'.format(uname))
  
  def getUsername(self):
    wait = WebDriverWait(self.browser, 10)
    uname = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'h2.BrX75')))
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
  
  def selectTopPicOnExplore(self):
    self.pic = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
    self.pic.click()
  
  def selectRecentPicOnExplore(self):
    self.pic = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a')
    self.pic.click()
  
  def selectPic(self, number = 1, type = 'Recent'):
    self.pic = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a')
    self.pic.click()
  
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
    
  def clickUsername(self):
    self.profile = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[3]/div/div[3]/a')
    self.profile.click()
    
  def alreadyLiked(self,element):
    self.liked = False
    if element.text == 'Unlike':
      print('Picture already liked, moving on...')
      self.liked = True

    return(liked)

  def printStats(self):
    print('\n--------Stats----------')
    print('Liked {} pictures across {} profiles'.format(self.likes,len(self.profilesEngaged)))
    print('{} errors handled'.format(self.errors_handled))
  
  def close(self):
    self.browser.close()
