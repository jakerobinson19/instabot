from selenium import webdriver
import random
import emoji

wordOptions = [['Omg','So','Absolutely',"You're",],
               ['so flippin cute','adorable','lovely','so sweet','so so adorable','fabulous'],
               ['!','!!','!!!']]
emojiOptions = [':heart:',':heartpulse:',':two_hearts:',':kissing_heart:',':heart_eyes:']

def createComment():
  firstWord = wordOptions[0][random.randint(0,len(wordOptions[0])-1)]
  secondWord = wordOptions[1][random.randint(0,len(wordOptions[1])-1)]
  punctuation = self.wordOptions[2][random.randint(0,len(self.wordOptions[2])-1)]
  #emoji = emojiOptions[random.randint(0,len(emojiOptions)-1)]
  
  comment = firstWord + ' ' + secondWord + punctuation
  return(comment)

def getNumberOfComments():

def getComments():

  
def sendComment(self, comm):
   comment_box = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   time.sleep(1)
   comment_box.click()
   comment_box = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   comment_box.send_keys(comm)
   
   comment_box.send_keys(Keys.ENTER)
   comments = comments + 1

