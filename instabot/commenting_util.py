#!/usr/bin/env python

#selenium modules
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

#instabot modules
from config import wordOptions
from config import commenting_params
from read_functions import read_xpath

#plus a little randomness
import random

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
  emoji = emoji_options[random.randint(0,len(emoji_options)-1)]
  
  comment = firstWord + ' ' + secondWord + punctuation + ' ' + emoji + ' '
  return(comment)

def get_comments_on_post(browser):
    try:
      comms = WebDriverWait(self.browser, 10).until(
      EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comment_section')))
      )   
    except TimeoutException:
      print("No comments or caption on this post")
      comms = None

    return(comms)

def get_number_of_comments():
  num_of_comments = len(get_comments_on_post()) - 1
  return(num_of_comments)

def get_username_on_comment(comments):
    try:
        comm_unames = WebDriverWait(browser, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, read_xpath('comments','comments_on_pic')))
        )
    except TimeoutException:
        print("Unable to grab usernames from comments - error occurred")
        comm_unames = None
    
    return(comm_unames)
  
def send_comment(browser, comm):
   comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   time.sleep(1)
   comment_box.click()
   comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "textarea.Ypffh")))
   browser.execute_script(
                "arguments[0].value = arguments[1];",
                comment_box, comm)

  comment_box.send_keys('\b')
  comment_box = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, read_selector('elements','comment_box'))))
  comment_box.send_keys(Keys.ENTER)
  comments = comments + 1

def is_commenting_disabled(browser):
    try:
        is_disabled = browser.execute_script("return window._sharedData.entry_data.PostPage[0].graphql.shortcode_media.comments_disabled")
    except:
        try:
            browser.execute_script("location.reload()")
            is_disabled = browser.execute_script("return window._sharedData.entry_data.PostPage[0].graphql.shortcode_media.comments_disabled")  
        except Exception as e:
            msg = ("Failed to check comments' status for verification!\n\t{}"
                   .format(str(e).encode("utf-8")))
            return False, msg
    
    if is_disabled:
      return True, 'Comment are disabled for this post'

    return False, "Comments Enabled"

def validate_commenting(post, media_type):
    if commenting_params['ENABLE_COMMENTS']:
        if commenting_params['COMMENT_ON_PICS'] and media_type == 'pic':
            comment_allowed = True
        elif commenting_params['COMMENT_ON_PICS'] and media_type == 'video':
            comment_allowed = True
        else:
            comment_allowed = False
            
    return(comment_allowed)
