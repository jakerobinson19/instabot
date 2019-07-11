#!/usr/bin/env python

from selenium import webdriver
import random
import emoji

word_options = [['Omg','So','Absolutely',"You're",],
               ['so flippin cute','adorable','lovely','so sweet','so so adorable','fabulous'],
               ['!','!!','!!!']]
emoji_options = [':heart:',':heartpulse:',':two_hearts:',':kissing_heart:',':heart_eyes:']

def check_if_comments_enabled():
  
def create_comment():
  firstWord = wordOptions[0][random.randint(0,len(wordOptions[0])-1)]
  secondWord = wordOptions[1][random.randint(0,len(wordOptions[1])-1)]
  punctuation = self.wordOptions[2][random.randint(0,len(self.wordOptions[2])-1)]
  #emoji = emojiOptions[random.randint(0,len(emojiOptions)-1)]
  
  comment = firstWord + ' ' + secondWord + punctuation
  return(comment)

def get_number_of_comments():
  number_of_comments = read_xpath(['comments']['comments_on_pic'])
  return(len(comments))
  #browser.find_elements_by_xpath("//ul[@class='Mr508']")
  
def get_comments(browser):
  comments = read_xpath(['comments']['comments_on_pic'])
  return(comments)
  #browser.find_elements_by_xpath("//ul[@class='Mr508']")

def get_username_on_comment(comments):
  comment_usernames = []
  
  for comm in comments:
    uname = comm.read_path(['comments']['username_of_comment'])
    comment_usernames.append(uname)
    
  return(comment_usernames)
  
  
def send_comment(self, comm):
   comment_box = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   time.sleep(1)
   comment_box.click()
   comment_box = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   comment_box.send_keys(comm)
   
   comment_box.send_keys(Keys.ENTER)
   comments = comments + 1

