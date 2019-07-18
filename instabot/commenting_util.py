#!/usr/bin/env python

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

from xpaths import read_xpath
import random

word_options = ['Omg','So','Absolutely',"Holy fluff. You're", 'Awwww', "By our fluffy paws! You're "],
               ['so cute','adorable','lovely','so sweet','so so adorable','fabulous'],
               ['!','!!','!!!']]

def already_commented_on(users_email):
    already_commented = False

    comms = get_comments_on_post()
    
    for c in comms:
      if c.text == users_email:
        already_commented = True

    return(already_commented)
  
def create_comment():
  firstWord = wordOptions[0][random.randint(0,len(wordOptions[0])-1)]
  secondWord = wordOptions[1][random.randint(0,len(wordOptions[1])-1)]
  punctuation = self.wordOptions[2][random.randint(0,len(self.wordOptions[2])-1)]
  
  comment = firstWord + ' ' + secondWord + punctuation
  return(comment)

def get_comments_on_post(browser):
    return(browser.find_elements_by_xpath(read_xpath('pic_comments','comments')))

def get_number_of_comments():
  num_of_comments = len(get_comments_on_post()) - 1
  return(num_of_comments)

def get_username_on_comment(comments):
  comment_usernames = []
  
  for comm in comments:
    uname = comm.read_xpath(['comments']['username_of_comment'])
    comment_usernames.append(uname)
    
  return(comment_usernames)
  
def send_comment(comm):
   comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   time.sleep(1)
   comment_box.click()
   comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   comment_box.send_keys(comm)
   
   comment_box.send_keys(Keys.ENTER)
   comments = comments + 1

