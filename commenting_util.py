from selenium import webdriver
import random
import emoji

wordOptions = [['Omg','So','Absolutely','You are',],['the cutest','adorable','lovely','so sweet']]
emojiOptions = [':heart:',':heartpulse:',':two_hearts:',':kissing_heart:',':heart_eyes:','

def createComment():
  comment = None
  
  firstWord = wordOptions[0][random.randint(0,len(wordOptions[0])-1)]
  secondWord = wordOptions[1][random.randint(0,len(wordOptions[1])-1)]
  emoji = emojiOptions[random.randint(0,len(emojiOptions)-1)]
  
  comment = firstWord + ' ' + secondWord + ' ' + emoji
  return(comment)

def getNumberOfComments():

def getComments():

def sendComment(self, comm):
    self.commentInput = self.browser.find_element_by_class_name('Ypffh')
    self.commentInput.send_keys(comm)
    delay()
    #self.commentInputNew = self.browser.find_element_by_xpath("//div[@class='Mfkwx wUsz1']")
    self.commentInput.send_keys(Keys.ENTER)

